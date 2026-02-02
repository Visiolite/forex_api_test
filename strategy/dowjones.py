#--------------------------------------------------------------------------------- Location
# strategy/dowjones.py

#--------------------------------------------------------------------------------- Description
# dowjones

#--------------------------------------------------------------------------------- Import
import inspect, time
from datetime import datetime
from logic.startup import debug, log_instance, Strategy_Run, list_instrument, Strategy_Action, Strategy_Run
from logic.util import model_output, sort, time_change_utc_newyork, cal_price_pips, cal_size, get_tbl_name
from logic.log import Logic_Log
from logic.data_sql import Data_SQL

#--------------------------------------------------------------------------------- Action
class Dowjones:
    #--------------------------------------------- init
    def __init__(
            self, 
            params:dict=None, 
            log:Logic_Log=None
        ):
        #-------------- Debug
        self.this_class = self.__class__.__name__
        #-------------- Instance
        self.log = log if log else log_instance
        #-------------- Input
        self.execute_id = params["execute_id"]
        self.money_management_id = params["money_management_id"]
        self.profit_manager_id = params["profit_manager_id"]
        self.symbols = params["symbols"].split(',')
        self.actions = params["actions"].split(',')
        self.amount = params["amount"]
        self.tp_pips = params["tp_pips"]
        self.sl_pips = params["sl_pips"]
        self.date_from = params["date_from"]
        self.date_to = params["date_to"]
        self.step = params["step"]
        self.trade_limit_profit= params["trade_limit_profit"]
        self.time_start = datetime.strptime(params["params"]["time_start"], "%H:%M:%S").time()
        self.time_end = datetime.strptime(params["params"]["time_end"], "%H:%M:%S").time()
        self.change_pip = params["params"]["change_pip"]
        self.order_pip = params["params"]["order_pip"]
        self.down = params["params"]["down"]
        self.up = params["params"]["up"]
        self.pending_limit = params["params"]["pending_limit"]
    
        #-------------- Variable
        self.balance = None
        self.risk = None
        self.set_price = None
        self.set_order = None
        self.date = None
        self.ask = None
        self.bid = None
        self.price = None

    #--------------------------------------------- start
    def start(self):
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action : Just buy|sell order
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
        #--------------Variable
        items = []
        #--------------Action
        try:
            pass
        except Exception as e:  
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Output
        output.time = sort(f"{(time.time() - start_time):.3f}", 3)
        output.data = items
        output.message = None
        #--------------Verbose
        if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 25)} | {output.time}", output.message)
        #--------------Log
        if log : self.log.log(log_model, output)
        #--------------Return
        return output

    #--------------------------------------------- stop
    def stop(self):
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
        #--------------Variable
        items = []
        #--------------Action
        try:
            items.append({"run": Strategy_Run.ORDER_CLOSE_ALL})
        except Exception as e:  
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Output
        output.time = sort(f"{(time.time() - start_time):.3f}", 3)
        output.data = items
        output.message = output.status
        #--------------Verbose
        if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 25)} | {output.time}", output.message)
        #--------------Log
        if log : self.log.log(log_model, output)
        #--------------Return
        return output
    
    #--------------------------------------------- order_close
    def order_close(self, order_detaile):
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action : Just buy|sell order
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
        #--------------Variable
        items = []
        #--------------Action
        try:
            pass
        except Exception as e:  
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Output
        output.time = sort(f"{(time.time() - start_time):.3f}", 3)
        output.data = items
        output.message = None
        #--------------Verbose
        if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 25)} | {output.time}", output.message)
        #--------------Log
        if log : self.log.log(log_model, output)
        #--------------Return
        return output

    #--------------------------------------------- price_change
    def price_change(
            self,
            symbol,
            date,
            ask,
            bid,
            digits,
            point_size,
            father_id, 
            step,
        ):
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
        #--------------Variable
        items = []
        #--------------Action
        try:
            #---------Everyday
            if (self.set_order is None) or (self.set_order is False) or (date.date()> self.date.date()):
                ny_date = time_change_utc_newyork(date)
                #---------Time
                if self.time_start <= ny_date.time() <= self.time_end:
                    #---Set_Price
                    if not self.set_price or date.date()> self.date.date():
                        self.set_order = False
                        self.set_price = True
                        self.ask = ask
                        self.bid = bid
                        self.date = date
                    #---Check_Price
                    if self.set_price: 
                        movement = abs(ask - self.ask)
                        if movement >= self.change_pip:
                            self.set_order = True
                            self.set_price = False
                            action = self.up if ask > self.ask else self.down
                            if action == "buy":
                                price = cal_price_pips(self.ask, -self.order_pip , digits, point_size)
                            else:
                                price = cal_price_pips(self.bid, self.order_pip , digits, point_size)
                            if self.risk > 0 :
                                amount = cal_size(balance=self.balance, price=price, pips=self.sl_pips, risk=self.risk, digits=digits, point_size=point_size)
                            else:
                                amount = self.amount
                            amount = float(f"{amount:.{2}f}")
                            item = {
                                "state": Strategy_Action.PRICE_CHANGE,
                                "run": Strategy_Run.ORDER_PENDING,
                                "digits": digits, 
                                "point_size": point_size,
                                "father_id": father_id,
                                "execute_id": self.execute_id,
                                "tp_pips": self.tp_pips, 
                                "sl_pips": self.sl_pips,
                                "step": step,
                                "symbol": symbol, 
                                "action": action, 
                                "amount": amount, 
                                "date": date,
                                "ask": price,
                                "bid": price,
                                "pending_limit": self.pending_limit
                            }
                            items.append(item)
        except Exception as e:  
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Output
        output.time = sort(f"{(time.time() - start_time):.3f}", 3)
        output.data = items
        output.message = f"{symbol} | {date} | {ask} | {bid} | {digits} | {point_size}"
        #--------------Verbose
        if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 25)} | {output.time}", output.message)
        #--------------Log
        if log : self.log.log(log_model, output)
        #--------------Return
        return output

    #--------------------------------------------- back
    def back(
            self, 
            mng_sql:Data_SQL=None, 
            data_sql:Data_SQL=None
        ):
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
        #-------------- Import
        from logic.back import Logic_Back
        logic_back = Logic_Back()
        #-------------- Variable
        data = {}
        order_open_accept = True
        check_tp_sls = []
        #-------------- Data
        cmd = f"SELECT * FROM profit_manager_item WHERE profit_manager_id={self.profit_manager_id} ORDER BY value DESC"
        profit_manager_items = mng_sql.db.items(cmd=cmd).data 
        cmd = f"SELECT balance, risk, limit_profit, limit_loss, limit_trade, limit_stop FROM money_management WHERE id={self.money_management_id}"
        money_management = mng_sql.db.items(cmd=cmd).data[0]
        #--------------Action
        try:
            #------Data
            for symbol in self.symbols:
                table = get_tbl_name(symbol, "t1")
                cmd = f"SELECT id, date, ask, bid FROM {table} WHERE date>='{self.date_from}' and date<='{self.date_to}' ORDER BY date ASC"
                result:model_output = data_sql.db.items(cmd=cmd)
                if result.status == True : data[symbol] = result.data
            #------Next
            for i in range(self.step):
                #---Step
                step = mng_sql.db.item(cmd=f"SELECT MAX(step) FROM back_order WHERE execute_id={self.execute_id}").data
                step = (step + 1) if step else 1
                #---Verbose
                output.time = sort(f"{(time.time() - start_time):.3f}", 3)
                output.message = f"exi({self.execute_id}) | stg({self.this_class}) | sym({self.symbols}) | stp({step})"
                if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 25)} | {output.time}", output.message)
                #---Rest
                self.balance = money_management[0]
                self.risk = money_management[1]
                #---money_management
                account_limit_profit = money_management[2]
                account_limit_loss = money_management[3]
                account_limit_trade = money_management[4]
                account_limit_stop = money_management[5]
                #---variable
                account_profit_close = 0
                account_profit_open = 0
                list_order_open = []
                list_order_close = []
                list_order_pending = []
                keep = True
                #---Start
                result_start:model_output = self.start()
                mng_sql.db.execute(cmd=f"UPDATE back_execute SET status='{Strategy_Action.START}' WHERE id={self.execute_id}")
                #---Next
                for symbol in self.symbols:
                    digits = list_instrument[symbol]["digits"]
                    point_size = list_instrument[symbol]["point_size"]
                    for row in data[symbol]:
                        #------price_data
                        date = row[1]
                        ask = float(row[2])
                        bid = float(row[3])
                        #------check_pending_order
                        if len(list_order_pending)>0 :
                            result:model_output = logic_back.check_pending_order(list_order_pending, symbol, date, ask, bid)
                            if len(result.data)>0:
                                list_order_open = mng_sql.db.items(cmd=f"select * FROM back_order WHERE execute_id='{self.execute_id}' and step='{step}' AND status='open'").data
                        #------profit_manager
                        if len(list_order_open)>0 : 
                            result:model_output = logic_back.profit_manager(list_order_open, symbol, date, ask, bid, digits, point_size, profit_manager_items, self.tp_pips, self.sl_pips)
                            if len(result.data)>0:
                                list_order_open = mng_sql.db.items(cmd=f"select * FROM back_order WHERE execute_id='{step}' and step='{step}' AND status='open'").data
                        #------check_tp_sl
                        if len(list_order_open)>0 : 
                            check_tp_sls = logic_back.check_tp_sl(list_order_open, symbol, date, ask, bid)
                            if len(check_tp_sls)>0:
                                for item in check_tp_sls:
                                    self.balance = self.balance + item["profit"]
                                    account_profit_close = account_profit_close + item["profit"]
                                list_order_open = mng_sql.db.items(cmd=f"select * FROM back_order WHERE execute_id='{self.execute_id}' and step='{step}' AND status='open'").data
                                list_order_close = mng_sql.db.items(cmd=f"select * FROM back_order WHERE execute_id='{self.execute_id}' and step='{step}' AND status='close'").data
                        #------check_limit
                        logic_back.check_limit(
                            list_order_open, 
                            list_order_close, 
                            account_limit_profit, 
                            account_limit_loss, 
                            account_limit_trade, 
                            account_limit_stop, 
                            self.trade_limit_profit, 
                            ask, 
                            bid, 
                            date, 
                            digits, 
                            point_size
                        )
                        # if not self.keep : 
                        #     break
                        #------order_close
                        if order_open_accept:
                            for check_tp_sl in check_tp_sls :
                                result_strategy:model_output = self.order_close(order_detaile=check_tp_sl)
                                for item in result_strategy.data :
                                    item["father_id"] = check_tp_sl.get("id")
                                    item["date"] = self.date
                                    item["ask"] = self.ask
                                    item["bid"] = self.bid
                                    self.action(items=result_strategy.data)
                        #------price_change
                        result_strategy_price_change:model_output = self.price_change(
                            symbol=symbol, 
                            date=date,
                            ask=ask, 
                            bid=bid, 
                            digits=digits,
                            point_size=point_size,
                            father_id=-1,
                            step=step
                        )
                        if result_strategy_price_change.data:
                            logic_back.action(items=result_strategy_price_change.data)
                            list_order_open = mng_sql.db.items(cmd=f"select * FROM back_order WHERE execute_id='{self.execute_id}' and step='{self.step}' AND status='open'").data
                            list_order_pending = mng_sql.db.items(cmd=f"select * FROM back_order_pending WHERE execute_id='{self.execute_id}' and step='{self.step}' and status='place'").data
                    #--------------Stop
                    result_strategy:model_output = self.stop()
                    for item in result_strategy.data :
                        logic_back.action(items=result_strategy.data)
        except Exception as e:  
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Output
        output.time = sort(f"{(time.time() - start_time):.3f}", 3)
        output.data = None
        output.message = f"{self.execute_id} | {self.this_class} | {self.symbols} | {result_start.status}"
        #--------------Verbose
        if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 25)} | {output.time}", output.message)
        #--------------Log
        if log : self.log.log(log_model, output)
        #--------------Return
        return output