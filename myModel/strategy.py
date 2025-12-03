#--------------------------------------------------------------------------------- Location
# models/strategy.py

#--------------------------------------------------------------------------------- Description
# strategy

#--------------------------------------------------------------------------------- Import
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.inspection import inspect
from myLib.database_orm import BaseModel as BaseModel_db
from pydantic import BaseModel as BaseModel_py
from typing import Optional

#--------------------------------------------------------------------------------- Database
class strategy_model_db(BaseModel_db):
    #---Name
    __tablename__ = 'strategy'
    #---Items
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, default='')
    description = Column(String, default='')
    enable = Column(Boolean, default=False)
    #---Display
    def __repr__(self) : return f"{self.toDict()}"
    #---Json
    def toDict(self) : return {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}

#--------------------------------------------------------------------------------- Python
class strategy_model_py(BaseModel_py):
    id : int = 0
    name : str = ''
    description : Optional[str] = ''
    enable : bool = True