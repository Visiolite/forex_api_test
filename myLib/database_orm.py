#--------------------------------------------------------------------------------- Location
# myLib/database_orm.py

#--------------------------------------------------------------------------------- Description
# database_orm

#--------------------------------------------------------------------------------- Import
import inspect, time
from myLib.model import model_output
from myLib.log import Log
from myLib.utils import config, debug, sort
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_

#--------------------------------------------------------------------------------- Variable
BaseModel = declarative_base()

#--------------------------------------------------------------------------------- Class
class Database_Orm:
    #-------------------------- [Init]
    def __init__(self, database='main', verbose: bool = False, log: bool = False, instance_log=None):
        #--------------------Variable
        self.this_class = self.__class__.__name__
        self.log = log
        self.verbose = verbose
        #--------------------Instance
        self.instance_log = instance_log if instance_log else Log()
        #--------------------Engine
        cfg = config.get("database", {}).get(database, {})
        host = cfg.get("host")
        port = cfg.get("port")
        username = cfg.get("user")
        password= cfg.get("pass",)
        name = cfg.get("name")
        self.engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{name}", echo=False, pool_size=100, max_overflow=100)
        self.session = sessionmaker(bind=self.engine)()

    #-------------------------- [Create tables]
    def create_tables(self) -> model_output:
        import myModel
        BaseModel.metadata.create_all(self.engine)

    #-------------------------- [Add]
    def add(self, model, item, **filters) -> model_output:
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
            #--------------Data
            query = self.session.query(model)
            if filters:
                for attr, value in filters.items() : query = query.filter(getattr(model, attr) == value)
                item_exist = query.first()
            else:
                item_exist = query.filter(model.id == item.id).first()
            #--------------Action
            if not item_exist:
                self.session.add(item)
                self.session.commit()
                output.status = True
            else:
                output.status = False
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
    
    #-------------------------- [Items]
    def items(self, model, **filters) -> model_output:
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
            #--------------Action
            query = self.session.query(model)
            if filters:
                for attr, value in filters.items() : 
                    query = query.filter(getattr(model, attr) == value)
            query = query.order_by(model.id)
            result = query.all()
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.status = True if result else False
            output.message =f"{model}"
            output.data = result
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

    #-------------------------- [Update]
    def update(self, model, item) -> model_output:
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
            #--------------Action
            source = self.session.query(model).filter(model.id == item.id).first()
            if source:
                for key, value in item.toDict().items():
                    if hasattr(source, key) : setattr(source, key, value)
                self.session.commit()
                output.status = True
            else:
                output.status = False
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

    #-------------------------- [Delete]
    def delete(self, model, id) -> model_output:
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
            #--------------Data
            item = self.session.query(model).filter(model.id == id).first()
            #--------------Action
            if item:
                self.session.delete(item)
                self.session.commit()
                output.status = True
            else:
                output.status = False
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
    
    #-------------------------- [truncate]
    def truncate(self, model) -> model_output:
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
            #--------------Action
            self.session.execute(text(f"TRUNCATE TABLE {model.__tablename__} RESTART IDENTITY CASCADE"))
            self.session.commit()
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)            
            output.message = f"Truncate table : {model.__tablename__}"
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
    
    #-------------------------- [create]
    def create(self, model) -> model_output:
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
            #--------------Action
            model.__table__.create(self.engine, checkfirst=True)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.message =f"Create table : {model.__tablename__}"
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
    
    #-------------------------- [drop]
    def drop(self, model) -> model_output:
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
            #--------------Action
            model.__table__.drop(self.engine, checkfirst=True)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.message =f"Drop table : {model.__tablename__}"
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