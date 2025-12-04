#--------------------------------------------------------------------------------- Location
# myLib/data_orm.py

#--------------------------------------------------------------------------------- Description
# data_orm

#--------------------------------------------------------------------------------- Import
import inspect
from myLib.database_orm import database_orm as database 
from myLib.model import model_output
from myLib.utils import debug, sort
from myLib.log import Log

#--------------------------------------------------------------------------------- Class
class Data_Orm:
    #-------------------------- [Init]
    def __init__(self, verbose: bool = False, log: bool = False):
        self.this_class = self.__class__.__name__
        self.modoule = "strategy"
        self.verbose = verbose
        self.log = log
        self.log_instance = Log()
        self.db = database()

    #-------------------------- [Add]
    def add(self, model, item) -> model_output:
        #--------------Description
        # IN     : model
        # OUT    : model_output
        # Action : Add model to
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
            log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
            log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
            output = model_output()
            #--------------Action
            output = self.db.add(model=model, item=item)
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{self.this_class} | {this_method}", output.message)
            #--------------Log
            if log : self.log_instance.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log_instance.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output

    #--------------------------[Items]
    def items(self, model, **filters) -> model_output:
        #--------------Description
        # IN     : 
        # OUT    : model_output
        # Action : Get models from database and return them
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
            log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
            log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
            output = model_output()
            #--------------Action
            output = self.db.items(model=model, **filters)
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{self.this_class} | {this_method}", output.message)
            #--------------Log
            if log : self.log_instance.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log_instance.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output

    #--------------------------[Item]
    def item(self, model, id:int) -> model_output:
        #--------------Description
        # IN     : id
        # OUT    : model_output
        # Action : Get model from database and return it
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
            log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
            log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
            output = model_output()
            #--------------Action
            output = self.db.items(model=model, id=id)
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{self.this_class} | {this_method}", output.message)
            #--------------Log
            if log : self.log_instance.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log_instance.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output
    
    #--------------------------[Update]
    def update(self, model, item) -> model_output:
        #--------------Description
        # IN     : model
        # OUT    : model_output
        # Action : Get model and update to database
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
            log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
            log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
            output = model_output()
            #--------------Action
            output = self.db.update(model=model, item=item)
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{self.this_class} | {this_method}", output.message)
            #--------------Log
            if log : self.log_instance.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log_instance.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output

    #--------------------------[Delete]
    def delete(self, model, id:int) -> model_output:
        #--------------Description
        # IN     : id
        # OUT    : model_output
        # Action : delete model from database
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
            log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
            log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
            output = model_output()
            #--------------Action
            output = self.db.delete(model=model, id=id)
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{self.this_class} | {this_method}", output.message)
            #--------------Log
            if log : self.log_instance.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log_instance.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output