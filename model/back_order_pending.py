#--------------------------------------------------------------------------------- Location
# models/model_back_order_pending.py

#--------------------------------------------------------------------------------- Description
# model_back_order_pending

#--------------------------------------------------------------------------------- Import
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.inspection import inspect
from logic.database_orm import BaseModel as BaseModel_db
from pydantic import BaseModel as BaseModel_py
from typing import Optional

#--------------------------------------------------------------------------------- Database
class model_back_order_pending_db(BaseModel_db):
    #---Name
    __tablename__ = 'back_order_pending'
    #---Items
    id = Column(Integer, primary_key=True, autoincrement=True)
    father_id = Column(Integer, default=0)
    execute_id = Column(Integer, default=1)
    step = Column(Integer, default=1)
    symbol = Column(String, default='')
    action = Column(String, default='')
    amount = Column(Float, default=0.0)
    date = Column(DateTime)
    price = Column(Float, default=0.0)
    tp_pips = Column(Float, default=0.0)
    sl_pips = Column(Float, default=0.0)
    pending_limit = Column(Integer, default=0)
    status = Column(String, default='')
    description = Column(String, default='')
    enable = Column(Boolean, default=True)
    #---Display
    def __repr__(self) : return f"{self.toDict()}"
    #---Json
    def toDict(self) : return {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}

#--------------------------------------------------------------------------------- Python
class model_back_order_pending_py(BaseModel_py):
    id : int = 0
    father_id : int = 0
    execute_id : int = 0
    step : int = 1
    symbol : str = ''
    action : str = ''
    amount : float = 0
    date : Optional[str] = ''
    price : float = 0
    tp_pips : float = 0
    sl_pips : float = 0
    pending_limit : int = 0
    status : Optional[str] = ''
    description : Optional[str] = ''
    enable : bool = True
