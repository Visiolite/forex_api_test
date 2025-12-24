#--------------------------------------------------------------------------------- Location
# models/model_live_execute.py

#--------------------------------------------------------------------------------- Description
# model_live_execute

#--------------------------------------------------------------------------------- Import
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.inspection import inspect
from myLib.database_orm import BaseModel as BaseModel_db
from pydantic import BaseModel as BaseModel_py
from typing import Optional

#--------------------------------------------------------------------------------- Database
class model_live_execute_db(BaseModel_db):
    #---Name
    __tablename__ = 'live_execute'
    #---Items
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, default='')
    strategy_item_id = Column(Integer, default=1)
    account_id = Column(Integer, default=1)
    count = Column(Integer, default=1)
    status = Column(String, default='')
    description = Column(String, default='')
    enable = Column(Boolean, default=True)
    #---Display
    def __repr__(self) : return f"{self.toDict()}"
    #---Json
    def toDict(self) : return {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}

#--------------------------------------------------------------------------------- Python
class model_live_execute_py(BaseModel_py):
    id : int = 0
    name : str = ''
    strategy_item_id : int = 1
    account_id : int = 1
    count : int = 1
    status : str = ''
    description : Optional[str] = ''
    enable : bool = True