#--------------------------------------------------------------------------------- Location
# models/strategy_item.py

#--------------------------------------------------------------------------------- Description
# strategy_item

#--------------------------------------------------------------------------------- Import
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.inspection import inspect
from myLib.database_orm import BaseModel as BaseModel_db
from pydantic import BaseModel as BaseModel_py
from pydantic import BaseModel
from typing import Optional

#--------------------------------------------------------------------------------- Database
class strategy_item_model_db(BaseModel_db):
    #---Name
    __tablename__ = 'strategy_item'
    #---Items
    id = Column(Integer, primary_key=True, autoincrement=True)
    strategy_id = Column(Integer, default=0)
    name = Column(String, default='')
    params = Column(String, default='')
    description = Column(String, default='')
    enable = Column(Boolean, default=False)
    #---Display
    def __repr__(self) : return f"{self.toDict()}"
    #---Json
    def toDict(self) : return {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}

#--------------------------------------------------------------------------------- Python
class strategy_item_model_py(BaseModel_py):
    id : int = 0
    strategy_id : int = 0
    name : str = ''
    params : dict = {}
    description : Optional[str] = ''
    enable : bool = True