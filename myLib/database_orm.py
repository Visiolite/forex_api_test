#--------------------------------------------------------------------------------- Location
# myLib/database_orm.py

#--------------------------------------------------------------------------------- Description
# database_orm

#--------------------------------------------------------------------------------- Import
import inspect
from myLib.utils import config, debug
from myLib.model import model_output
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_

#--------------------------------------------------------------------------------- Variable
BaseModel = declarative_base()
dbData = {}
dbCfg = config.get("database", {}).get("main", {})
host = dbCfg.get("host", "127.0.0.1")
port = dbCfg.get("port", "5432")
username = dbCfg.get("user", "forex")
password= dbCfg.get("pass", "&WnA8v!(THG%)czK")
name = dbCfg.get("name", "forex")

#--------------------------------------------------------------------------------- Instance
engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{name}", echo=False, pool_size=100, max_overflow=100)
session = sessionmaker(bind=engine)()

#--------------------------------------------------------------------------------- Class
class database_orm:
    #-------------------------- [Init]
    def __init__(self, type=None, verbose: bool = False, log: bool = False):
        #--------------Variable
        self.this_class = self.__class__.__name__
        self.modoule = "database_orm"
        self.verbose = verbose
        self.log = log

    #-------------------------- [Create tables]
    def create_tables(self) -> model_output:
        import myModel
        BaseModel.metadata.create_all(engine)

    #-------------------------- [Add]
    def add(self, model, item, **filters) -> model_output:
        #--------------Description
        # IN     : model
        # OUT    : model_output
        # Action : add model to database
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            output = model_output()
            #--------------Variable
            #session = sessionmaker(bind=engine)()
            #--------------Data
            query = session.query(model)
            if filters:
                for attr, value in filters.items() : query = query.filter(getattr(model, attr) == value)
                item_exist = query.first()
            else:
                item_exist = query.filter(model.id == item.id).first()
            #--------------Action
            if not item_exist:
                session.add(item)
                session.commit()
                output.status = True
                output.data = {model.__name__: 'added'}
            else:
                output.status = False
                output.data = {model.__name__: 'exist'}
        except Exception as e:  
            #--------------Error
            output.status = False
            output.data = {"class":self.this_class, "method":this_method, "error": str(e)}
            print(output)
        # finally:
        #         session.close()
        #--------------Verbose
        if self.verbose : print(output)
        #--------------Log
        if self.log : print(output)
        #--------------Output
        return output
        
    #-------------------------- [Items]
    def items(self, model, **filters) -> model_output:
        #--------------Description
        # IN     : 
        # OUT    : model_output
        # Action : return list of models
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            output = model_output()
            #--------------Variable
            #session = sessionmaker(bind=self.engine)()
            #--------------Data
            query = session.query(model)
            if filters:
                for attr, value in filters.items() : 
                    query = query.filter(getattr(model, attr) == value)
            query = query.order_by(model.id)
            result = query.all()
            #--------------Output
            output.status = True if result else False
            output.data = result
        except Exception as e:  
            #--------------Error
            output.status = False
            output.data = {"class":self.this_class, "method":this_method, "error": str(e)}
            print(output)
        # finally:
        #         session.close()
        #--------------Verbose
        if self.verbose : print(output)
        #--------------Log
        if self.log : print(output)
        #--------------Output
        return output

    #-------------------------- [Update]
    def update(self, model, item) -> model_output:
        #--------------Description
        # IN     : model
        # OUT    : model_output
        # Action : update model on database
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            output = model_output()
            #--------------Variable
            #session = sessionmaker(bind=self.engine)()
            #--------------Action
            source = session.query(model).filter(model.id == item.id).first()
            if source:
                for key, value in item.toDict().items():
                    if hasattr(source, key) : setattr(source, key, value)
                session.commit()
                output.status = True
                output.data = {model.__name__: f'updated:{item.id}'}
            else:
                output.status = False
                output.data = {model.__name__: f'updated:{item.id}'}
        except Exception as e:  
            #--------------Error
            output.status = False
            output.data = {"class":self.this_class, "method":this_method, "error": str(e)}
            print(output)
        # finally:
        #         session.close()
        #--------------Verbose
        if self.verbose : print(output)
        #--------------Log
        if self.log : print(output)
        #--------------Output
        return output

    #-------------------------- [Delete]
    def delete(self, model, id) -> model_output:
        #--------------Description
        # IN     : id
        # OUT    : model_output
        # Action : delete model from database
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            output = model_output()
            #--------------Variable
            #session = sessionmaker(bind=self.engine)()
            #--------------Data
            item = session.query(model).filter(model.id == id).first()
            #--------------Action
            if item:
                session.delete(item)
                session.commit()
                output.status = True
                output.data = {model.__name__: f'deleted:{id}'}
            else:
                output.status = False
                output.data = {model.__name__: f'not-exist:{id}'}
        except Exception as e:  
            #--------------Error
            output.status = False
            output.data = {"class":self.this_class, "method":this_method, "error": str(e)}
            print(output)
        # finally:
        #         session.close()
        #--------------Verbose
        if self.verbose : print(output)
        #--------------Log
        if self.log : print(output)
        #--------------Output
        return output

    #-------------------------- [Execute]
    def execute(self, model, cmd, values) -> model_output:
        #--------------Description
        # IN     : model
        # OUT    : model_output
        # Action : update model on database
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            output = model_output()
            #--------------Variable
            #session = sessionmaker(bind=self.engine)()
            #--------------Action
            sql = text(cmd)
            session.execute(sql, values)
            session.commit()
            output.data = {model.__name__: 'execute'}
        except Exception as e:  
            #--------------Error
            output.status = False
            output.data = {"class":self.this_class, "method":this_method, "error": str(e)}
            print(output)
        # finally:
        #         session.close()
        #--------------Verbose
        if self.verbose : print(output)
        #--------------Log
        if self.log : print(output)
        #--------------Output
        return output
    
    #-------------------------- [clear]
    def clear(self, model, **filters) -> model_output:
        #--------------Description
        # IN     : 
        # OUT    : model_output
        # Action : return list of models
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            output = model_output()
            #--------------Variable
            #session = sessionmaker(bind=self.engine)()
            #--------------Data
            query = session.query(model)
            if filters:
                for attr, value in filters.items() : 
                    query = query.filter(getattr(model, attr) == value)
            result = query.delete()
            session.commit()
            #--------------Output
            output.status = True if result else False
            output.data = result
        except Exception as e:  
            #--------------Error
            output.status = False
            output.data = {"class":self.this_class, "method":this_method, "error": str(e)}
            print(output)
        # finally:
        #         session.close()
        #--------------Verbose
        if self.verbose : print(output)
        #--------------Log
        if self.log : print(output)
        #--------------Output
        return output

    #-------------------------- [truncate]
    def truncate(self, model) -> model_output:
        #--------------Description
        # IN     : 
        # OUT    : model_output
        # Action : return list of models
        try:
            #--------------Debug
            this_method = inspect.currentframe().f_code.co_name
            output = model_output()
            #--------------Variable
            #session = sessionmaker(bind=self.engine)()
            #--------------Action
            session.execute(text(f"DELETE FROM {model.__tablename__}"))
            session.commit()
            #--------------Output
            output.data = {model.__name__: f'Truncate:{model.__tablename__}'}
        except Exception as e:  
            #--------------Error
            output.status = False
            output.data = {"class":self.this_class, "method":this_method, "error": str(e)}
            print(output)
        # finally:
        #         session.close()
        #--------------Verbose
        if self.verbose : print(output)
        #--------------Log
        if self.log : print(output)
        #--------------Output
        return output
    
    #-------------------------- [pydantic_to_sqlalchemy]
    def pydantic_to_sqlalchemy(self, pydantic_instance, sqlalchemy_model):
        return sqlalchemy_model(**pydantic_instance.dict())

    #-------------------------- [sqlalchemy_to_pydantic]
    def sqlalchemy_to_pydantic(self, sqlalchemy_instance, pydantic_model):
        return pydantic_model(**sqlalchemy_instance.dict())