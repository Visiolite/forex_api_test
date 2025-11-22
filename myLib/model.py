#--------------------------------------------------------------------------------- Location
# code/myLib/model.py

#--------------------------------------------------------------------------------- Description
# Model

#--------------------------------------------------------------------------------- Import
from pydantic import BaseModel
from enum import Enum
from typing import Dict, Any, Optional, List

#--------------------------------------------------------------------------------- Action
class model_output(BaseModel):
    status : bool = True
    data : Any = {}
    message : Any = {}