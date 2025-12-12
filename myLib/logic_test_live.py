#--------------------------------------------------------------------------------- Location
# myLib/logic_test_live.py

#--------------------------------------------------------------------------------- Description
# logic_test_live

#--------------------------------------------------------------------------------- Import
import inspect, time, ast
from myLib.model import model_output
from myLib.utils import config
from myLib.log import Log
from myLib.utils import debug, sort, get_strategy_instance
from myLib.data_orm import Data_Orm
from myLib.forex_api import Forex_Api
from myLib.forex import Forex
from myModel import *

#--------------------------------------------------------------------------------- Variable
database = config.get("general", {}).get("database_management", {})

#--------------------------------------------------------------------------------- Action
class Logic_Test_Live:
    #--------------------------------------------- init
    def __init__(self, verbose:bool=False, log:bool=False, instance_log:Log =None, instance_data_orm:Data_Orm =None):
        #--------------------Variable
        self.this_class = self.__class__.__name__
        self.log = log
        self.verbose = verbose
        #--------------------Instance
        self.instance_log = instance_log if instance_log else Log()
        self.instance_data_orm = instance_data_orm if instance_data_orm else Data_Orm(database=database)

    #--------------------------------------------- start
    def start(self, id:int) -> model_output:
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method
        #--------------Variable
        start_time = time.time()
        #--------------Data
        data = self.instance_data_orm.items(model=model_test_live_db, id=id)

        try:
            #--------------Action
            item = data.data[0]
            status = item.status
            account_id = item.account_id
            strategy_item = self.instance_data_orm.items(model=model_strategy_item_db, id=item.strategy_item_id).data[0]
            strategy = self.instance_data_orm.items(model=model_strategy_db, id=strategy_item.strategy_id).data[0]
            
            account = self.instance_data_orm.items(model=model_account_db, id=account_id).data[0]
            forex_api = Forex_Api(name=account.name, type=account.type, username=account.username, password=account.password, url=account.url, key=account.key)

            forex = Forex(forex_api = forex_api)
            forex_api.login()
            forex.account_info()

            strategy_instance = get_strategy_instance(strategy=strategy.name, forex=forex, params=ast.literal_eval(strategy_item.params))

            if status != "start":
                strategy_instance.start(code = item.id)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            #--------------Verbose
            if verbose : self.instance_log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.instance_log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.instance_log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.instance_log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output

    #--------------------------------------------- end
    def end(self, id:int) -> model_output:
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method
        #--------------Variable
        start_time = time.time()
        #--------------Data
        item = self.instance_data_orm.items(model=model_test_live_db, id=id)

        try:
            #--------------Action
            print(item)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            #--------------Verbose
            if verbose : self.instance_log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.instance_log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.instance_log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.instance_log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output
    
    #--------------------------------------------- order_close
    def order_close(self, id:int) -> model_output:
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method
        #--------------Variable
        start_time = time.time()
        #--------------Data
        item = self.instance_data_orm.items(model=model_test_live_db, id=id)

        try:
            #--------------Action
            print(item)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            #--------------Verbose
            if verbose : self.instance_log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.instance_log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.instance_log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.instance_log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output
    
    #--------------------------------------------- price_change
    def price_change(self, id:int) -> model_output:
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method
        #--------------Variable
        start_time = time.time()
        #--------------Data
        item = self.instance_data_orm.items(model=model_test_live_db, id=id)

        try:
            #--------------Action
            print(item)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            #--------------Verbose
            if verbose : self.instance_log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.instance_log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.instance_log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.instance_log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output