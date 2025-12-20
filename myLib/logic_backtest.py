#--------------------------------------------------------------------------------- Location
# myLib/logic_backtest.py

#--------------------------------------------------------------------------------- Description
# logic_backtest

#--------------------------------------------------------------------------------- Import
import inspect, time, ast
from myLib.logic_global import debug, list_instrument, log_instance, data_instance
from myLib.utils import model_output, sort, get_tbl_name
from myLib.log import Log
from myLib.data_sql import Data_SQL
from myLib.data_orm import Data_Orm
from myLib.logic_management import Logic_Management
from myModel.model_back_order import model_back_order_db

#--------------------------------------------------------------------------------- Action
class Logic_BackTest:
    #--------------------------------------------- init
    def __init__(self, execute_id, data_sql:Data_SQL=None, management_sql:Data_SQL=None, management_orm:Data_Orm=None, log:Log=None):
        #--------------------Variable
        self.this_class = self.__class__.__name__
        self.execute_id = execute_id
        self.strategy = None
        self.data = None
        self.orders = None
        #--------------------Instance
        self.management_orm = management_orm if management_orm else data_instance["management_orm"]
        self.management_sql = management_sql if management_sql else data_instance["management_sql"]
        self.data_sql = data_sql if data_sql else data_instance["data_sql"]
        self.log = log if log else log_instance
        self.logic_management = Logic_Management()

    #--------------------------------------------- run
    def run(self):
        #-------------- Description
        # IN     : order_id
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        start_time = time.time()
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method

        try:
            #--------------Detaile
            execute_detaile:model_output = self.logic_management.execute_detaile(id=self.execute_id, mode="back")
            detaile = execute_detaile.data
            self.strategy_name = detaile.get("strategy_name")
            self.status = detaile.get("status")
            self.date_from = detaile.get("date_from")
            self.date_to = detaile.get("date_to")
            self.params = ast.literal_eval(detaile.get("params"))
            #--------------Data
            self.symbols = self.params.get("symbols", "").split(',')
            self.data = self.get_data(symbols=self.symbols, date_from=self.date_from, date_to=self.date_to).data
            #--------------Strategy
            self.strategy = self.logic_management.get_strategy_instance(self.strategy_name).data
            self.strategy.params = self.params
            #--------------Start
            result_start:model_output = self.start()
            #--------------Next
            result_next:model_output = self.next()
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 12)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output

    #--------------------------------------------- strategy_start
    def start(self):
        #-------------- Description
        # IN     : order_id
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        start_time = time.time()
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method

        try:
            #--------------Data
            result_strategy: model_output = self.strategy.start()
            #--------------Items
            for item in result_strategy.data :
                item["ask"] = self.data[item.get("symbol")][0][2]
                item["bid"] = self.data[item.get("symbol")][0][3]
            #--------------Action
            result_action:model_output = self.action(items=result_strategy.data)
            #--------------Database
            cmd = f"UPDATE back_execute SET status='start' WHERE id={self.execute_id}"
            result_database:model_output = self.management_sql.db.execute(cmd=cmd)

            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.data = None
            output.status = f"{result_strategy.status} | {result_action.status} | {result_database.status}"
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 12)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output
    
    #--------------------------------------------- next
    def next(self):
        #-------------- Description
        # IN     : order_id
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        start_time = time.time()
        #-------------- Output
        output = model_output()
        result = model_output()
        output.class_name = self.this_class
        output.method_name = this_method
        #-------------- Variable
        fire = False

        try:
            #--------------Action
            for symbol in self.data:
               for row in self.data[symbol]:
                   fire = False
                   date = row[0]
                   date = row[1]
                   ask = row[2]
                   bid = row[3]
                   for order in self.orders :
                       order_id = order[0]
                       order_symbol = order[6]
                       if order_symbol == symbol :
                            order_action = order[7]
                            order_amount = order[8]
                            price_open = order[11]
                            order_tp = order[13]
                            order_sl = order[14]
                            #--------------Check TP/SL
                            #---Buy
                            if order_action == "buy":
                                if bid >= order_tp and order_tp > 0 : fire = True
                                if bid <= order_sl and order_sl > 0 : fire = True
                            #---Sell
                            if order_action == "sell":
                                if ask <= order_tp and order_tp > 0 :fire = True
                                if ask >= order_sl and order_sl > 0 : fire = True
                            #---Fire
                            if fire :
                                item = {"id":order_id, "action":order_action, "amount":order_amount, "price_open":price_open, "ask":ask, "bid":bid}
                                self.order_close(item =item)
                                order_detaile = self.logic_management.order_detaile(order_id=order_id, mode="back").data
                                result_strategy:model_output = self.strategy.order_close(order_detaile=order_detaile)
                                for item in result_strategy.data :
                                    item["ask"] = ask
                                    item["bid"] = bid
                                    result_action:model_output = self.action(items=result_strategy.data)
            #--------------Output
            output = result
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 12)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output
    
    #--------------------------------------------- get_data
    def get_data(self, symbols, date_from, date_to):
        #-------------- Description
        # IN     : order_id
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        start_time = time.time()
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method
        #-------------- Variable
        output.data = {}

        try:
            #--------------Action
            for symbol in symbols:
                table = get_tbl_name(symbol, "t1")
                cmd = f"SELECT id, date, ask, bid FROM {table} WHERE date>='{date_from}' and date<='{date_to}' ORDER BY date ASC"
                result:model_output = self.data_sql.db.items(cmd=cmd)
                if result.status == True :
                    output.data[symbol] = result.data
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.message = f"{date_from} | {date_to} | {len(symbols)}"
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 12)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output
    
    #--------------------------------------------- action
    def action(self, items:dict)-> model_output:
        #-------------- Description
        # IN     : order_id
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        start_time = time.time()
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method

        try:
            #--------------Action
            for item in items :
                run = item.get("run")
                #---order_open
                if run == "order_open":
                    result:model_output =self.order_open(item=item)
                #---order_close
                if run == "order_close":
                    result:model_output = self.order_close(item=item)
            #--------------Output
            output = result
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 12)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output
    
    #--------------------------------------------- order_open
    def order_open(self, item:dict)-> model_output:
        #-------------- Description
        # IN     :
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        start_time = time.time()
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method

        try:
            #-------------- Data
            symbol = item.get("symbol")
            buy_sell = item.get("buy_sell")
            amount = item.get("amount")
            tp_pips = item.get("tp_pips")
            sl_pips = item.get("sl_pips")
            ask = item.get("ask")
            bid = item.get("bid")
            #-------------- TP/SL
            if tp_pips or sl_pips:
                point_size = list_instrument[symbol]["point_size"]
                digits = list_instrument[symbol]["digits"]
                if buy_sell == "buy":
                    price_open = ask
                    tp = float(f"{ask + tp_pips * point_size:.{digits}f}")
                    sl = float(f"{bid - sl_pips * point_size:.{digits}f}")
                elif buy_sell == "sell":
                    price_open = bid
                    tp = float(f"{bid - tp_pips * point_size:.{digits}f}")
                    sl = float(f"{ask + sl_pips * point_size:.{digits}f}")
            #-------------- Action
            obj = model_back_order_db()
            obj.execute_id = self.execute_id
            obj.symbol = symbol
            obj.action = buy_sell
            obj.amount = amount
            obj.bid = bid
            obj.ask = ask
            obj.price_open = price_open
            obj.tp = tp
            obj.sl = sl
            obj.status = 'open'
            result:model_output = self.management_orm.add(model=model_back_order_db, item=obj)
            #-------------- Orders
            self.orders = self.management_sql.db.items(cmd=f"select * FROM back_order WHERE execute_id='{self.execute_id}' AND status='open'").data
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.status = result.status
            output.data = None
            output.message = f"{symbol} | {buy_sell} | {amount} | {price_open} | {tp} | {sl}"
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 12)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output
    
    #--------------------------------------------- order_close
    def order_close(self, item:dict)-> model_output:
        #-------------- Description
        # IN     :
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        start_time = time.time()
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method

        try:
            #-------------- Data
            id = item.get("id")
            action = item.get("action")
            amount = (item.get("amount"))
            price_open = (item.get("price_open"))
            ask = (item.get("ask"))
            bid = (item.get("bid"))
            #-------------- Profit
            if action == "buy":
                price_close = bid
                profit = round(bid - price_open, 6)
                profit = profit * amount
            elif action == "sell":
                price_close = ask
                profit = round(price_open - ask, 6)
                profit = profit * amount
            #-------------- Action
            cmd = f"UPDATE back_order SET date_close=CURRENT_TIMESTAMP, price_close={price_close}, profit={profit}, status='close' WHERE id='{id}'"
            result:model_output = self.management_sql.db.execute(cmd=cmd)
            #-------------- Orders
            self.orders = self.management_sql.db.items(cmd=f"select * FROM back_order WHERE execute_id='{self.execute_id}' AND status='open'").data
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.status = result.status
            output.data = None
            output.message = f"{id} | {profit}"
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 12)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output