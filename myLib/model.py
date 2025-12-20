#--------------------------------------------------------------------------------- Location
# code/myLib/model.py

#--------------------------------------------------------------------------------- Description
# Model

#--------------------------------------------------------------------------------- Import
from pydantic import BaseModel
from typing import Any

#--------------------------------------------------------------------------------- Action
class model_output(BaseModel):
    class_name : str = ''
    method_name : str = ''
    status : bool = True
    time : int = 0
    data : Any = {}
    message : Any = {}