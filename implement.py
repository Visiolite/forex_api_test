#--------------------------------------------------------------------------------- Location
# implement.py

#--------------------------------------------------------------------------------- Description
# Implement

#--------------------------------------------------------------------------------- Import
import os,sys, time
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{root_dir}/myLib")
from myLib.log import Log
from myLib.database import Database
from myLib.implementation import Implementation
from myLib.database_orm import Database_Orm

#--------------------------------------------------------------------------------- Variable
start_time = time.time()

#--------------------------------------------------------------------------------- Log
db = Database_Orm()
db.create_tables()

#--------------------------------------------------------------------------------- Log
log = Log()
log.fileClear()
log.table(drop=True, create=True, add=True)

#--------------------------------------------------------------------------------- Implementation
db = Database.instance()
db.open(name="Implement")
impelment = Implementation(db=db)

#-------------------- Instrument
impelment.instrument(drop=True, create=True,truncate=True, add=True)
impelment.account(drop=True, create=True,truncate=True, add=True)
impelment.strategy(drop=True, create=True,truncate=True, add=True)
impelment.strategy_item(drop=True, create=True,truncate=True, add=True)