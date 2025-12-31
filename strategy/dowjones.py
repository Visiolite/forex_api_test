#--------------------------------------------------------------------------------- Location
# strategy/dowjones.py

#--------------------------------------------------------------------------------- Description
# dowjones

#--------------------------------------------------------------------------------- Import
import inspect, time
from logic.logic_global import debug, log_instance, Strategy_Run, list_instrument
from logic.logic_util import model_output, sort
from logic.logic_log import Logic_Log
from datetime import datetime

#--------------------------------------------------------------------------------- Action
class Dowjones:
    #--------------------------------------------- init
    def __init__(self, params:dict=None, log:Logic_Log=None):
        #-------------- Variable
        self.this_class = self.__class__.__name__
        self.params = params
        #-------------- Instance
        self.log = log if log else log_instance
        #-------------- Params
        self.symbols = self.params.get("symbols").split(',')
        self.actions = self.params.get("actions").split(',')
        self.amount = self.params.get("amount")
        self.tp_pips = self.params.get("tp_pips")
        self.sl_pips = self.params.get("sl_pips")
        self.limit_trade = int(self.params.get("limit_trade"))
        self.limit_profit = int(self.params.get("limit_profit"))
        self.limit_loss = int(self.params.get("limit_loss"))
        self.params = self.params.get("params")
        self.time_start = datetime.strptime(self.params.get("time_start"), "%H:%M:%S").time()
        self.time_end = datetime.strptime(self.params.get("time_end"), "%H:%M:%S").time()
        self.change_pip = self.params.get("change_pip")
        self.order_pip = self.params.get("order_pip")
        self.down = self.params.get("down")
        self.up = self.params.get("up")
        self.ask = None
        self.bid = None
        self.price = None
        self.set_price = False
        self.date = None
        
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
        
        try:
            #--------------Action
            pass
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.data = items
            output.message = None
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 12)} | {output.time}", output.message)
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

        try:
            #--------------Action
            item = {
                "run": Strategy_Run.ORDER_CLOSE_ALL, 
                "state": this_method
            }
            items.append(item)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.data = items
            output.message = output.status
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 12)} | {output.time}", output.message)
            output.data = items
            output.message = None
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
    def order_close(self, order_detaile):
        #-------------- Description
        # IN     : execute_id
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

        try:
            #--------------Action
            pass
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.data = items
            output.message = None
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 12)} | {output.time}", output.message)
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

    #--------------------------------------------- price_change
    def price_change(self, price_data, order_close, order_open):
        #-------------- Description
        # IN     : execute_id
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

        try:
            for symbol in self.symbols:
                #--------------Data
                date = price_data[symbol].get("date")
                ask = price_data[symbol].get("ask")
                bid = price_data[symbol].get("bid")
                digits = list_instrument.get(symbol, {}).get("digits")
                #--------------Check time
                
                if self.time_start <= date.time() <= self.time_end:
                    if not self.set_price:
                        self.set_price = True
                        self.ask = ask
                        self.bid = bid
                        self.date = date
                    disagreement = ask - self.ask


                    if ask - self.ask >= self.change_pip:
                        item = {
                            "run": Strategy_Run.ORDER_CLOSE,
                            "state": this_method,
                            "symbol": symbol,
                            "action": "sell",
                            "price": bid,
                            "amount": self.amount,
                            "tp_pips": self.tp_pips,
                            "sl_pips": self.sl_pips,
                            "description": f"Price Change Up {self.change_pip} pips"
                        }
                        items.append(item)
                        self.ask = ask

                    print(date)
            #--------------Rule

            #--------------Action

            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.data = items
            output.message = None
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 15)} | {sort(this_method, 12)} | {output.time}", output.message)
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