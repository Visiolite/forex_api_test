#--------------------------------------------------------------------------------- Location
# myLib/logic_management.py

#--------------------------------------------------------------------------------- Description
# logic_management

#--------------------------------------------------------------------------------- Import
import inspect, time
from myLib.model import model_output
from myLib.logic_global import debug, log_instance, data_instance
from myLib.utils import sort
from myLib.log import Log
from myLib.data_orm import Data_Orm
from myLib.data_sql import Data_SQL
from myModel import *

#--------------------------------------------------------------------------------- Class
class Logic_Management:
    #-------------------------- [Init]
    def __init__(self, data_orm=None, data_sql=None, log=None):
        #--------------------Variable
        self.this_class = self.__class__.__name__
        self.log:Log = log if log else log_instance
        self.data_orm:Data_Orm = data_orm if data_orm else data_instance["management_orm"]
        self.data_sql:Data_SQL = data_sql if data_sql else data_instance["management_sql"]

    #-------------------------- [order_close]
    def order_close(self, order_id) -> model_output:
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
            cmd = f"UPDATE live_order SET status='close' WHERE order_id = '{order_id}';"
            result:model_output = self.data_sql.db.execute(cmd=cmd)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.data = order_id
            output.message=f"{order_id}"
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
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
    
    #-------------------------- [order_detaile]
    def order_detaile(self, order_id) -> model_output:
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
        detaile = {}

        try:
            #--------------Action
            cmd = f"SELECT strategy.id AS strategy_id, strategy_item.id AS strategy_item_id, live_execute.id AS live_execute_id, live_order.id AS live_order_id, live_order.date, live_order.symbol, live_order.action, live_order.amount, live_order.bid, live_order.ask, live_order.tp, live_order.sl, live_order.profit, live_order.status FROM strategy JOIN strategy_item ON strategy.id = strategy_item.strategy_id JOIN live_execute ON strategy_item.id = live_execute.strategy_item_id JOIN live_order ON live_order.execute_id = live_execute.id WHERE live_order.order_id = '{order_id}';"
            result:model_output = self.data_sql.db.items(cmd=cmd)
            #--------------Data
            if result.status and len(result.data) > 0 :
                detaile["strategy_id"] = result.data[0][0]
                detaile["strategy_item_id"] = result.data[0][1]
                detaile["live_execute_id"] = result.data[0][2]
                detaile["date"] = result.data[0][3]
                detaile["symbol"] = result.data[0][4]
                detaile["action"] = result.data[0][5]
                detaile["amount"] = result.data[0][6]
                detaile["bid"] = result.data[0][7]
                detaile["ask"] = result.data[0][8]
                detaile["tp"] = result.data[0][9]
                detaile["sl"] = result.data[0][10]
                detaile["profit"] = result.data[0][11]
                detaile["status"] = result.data[0][12]
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.data = detaile
            output.message=f"{order_id}"
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
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