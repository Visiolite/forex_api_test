#--------------------------------------------------------------------------------- Location
# models/model_back_order.py

#--------------------------------------------------------------------------------- Description
# model_back_order

#--------------------------------------------------------------------------------- Import
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.inspection import inspect
from logic.database_orm import BaseModel as BaseModel_db
from pydantic import BaseModel as BaseModel_py
from typing import Optional
from datetime import datetime

#--------------------------------------------------------------------------------- Database
class model_back_execute_detaile_db(BaseModel_db):
    #---Name
    __tablename__ = 'back_execute_detaile'
    #---Items
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    execute_id = Column(Integer, default=0)
    count = Column(Integer, default=0)
    profit = Column(Float, default=0)
    loss = Column(Float, default=0)
    #---Display
    def __repr__(self) : return f"{self.toDict()}"
    #---Json
    def toDict(self):
        data = {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}
        if data.get('date') and isinstance(data['date'], datetime) : data['date'] = data['date'].strftime('%Y-%m-%d %H:%M:%S')
        return data

#--------------------------------------------------------------------------------- Python
class model_back_execute_detaile_py(BaseModel_py):
    id : int = 0
    date : Optional[str] = ''
    execute_id : int = 0
    count : int = 0
    profit : float = 0
    loss : float = 0