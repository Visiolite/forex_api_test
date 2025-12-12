#--------------------------------------------------------------------------------- Location
# models/model_live_order.py

#--------------------------------------------------------------------------------- Description
# model_live_order

#--------------------------------------------------------------------------------- Import
from sqlalchemy import Column, Integer, String, Boolean,Float
from sqlalchemy.inspection import inspect
from myLib.database_orm import BaseModel as BaseModel_db
from pydantic import BaseModel as BaseModel_py
from typing import Optional

#--------------------------------------------------------------------------------- Database
class model_live_order_db(BaseModel_db):
    #---Name
    __tablename__ = 'live_order'
    #---Items
    id = Column(Integer, primary_key=True, autoincrement=True)
    execute_id = Column(Integer, default=0)
    order_id = Column(Integer, default=0)
    symbol = Column(String, default='')
    action = Column(String, default='')
    amount = Column(Integer, default=0)
    bid = Column(Float, default=0.0)
    ask = Column(Float, default=0.0)
    tp = Column(Float, default=0.0)
    sl = Column(Float, default=0.0)
    profit = Column(Float, default=0.0)
    status = Column(String, default='')
    description = Column(String, default='')
    enable = Column(Boolean, default=True)
    #---Display
    def __repr__(self) : return f"{self.toDict()}"
    #---Json
    def toDict(self) : return {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}

#--------------------------------------------------------------------------------- Python
class model_live_order_py(BaseModel_py):
    id : int = 0
    execute_id : int = 0
    order_id : int = ''
    symbol : str = ''
    action : str = ''
    amount : int = 0
    bid : float = 0
    ask : float = 0
    tp : float = 0
    sl : float = 0
    profit : float = 0
    status : str = ''
    description : Optional[str] = ''
    enable : bool = True