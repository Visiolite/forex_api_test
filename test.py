#--------------------------------------------------------------------------------- Location
# myLib/store.py

#--------------------------------------------------------------------------------- Description
# Store

#--------------------------------------------------------------------------------- Import
import os,sys, ast
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{root_dir}/myLib")
sys.path.insert(0, f"{root_dir}/myModel")
sys.path.insert(0, f"{root_dir}/myStrategy")
from myLib.utils import database_management
from myLib.data_orm import Data_Orm
from myLib.forex import Forex
from myLib.forex_api import Forex_Api
from myModel import *
from myStrategy import *


#--------------------------------------------------------------------------------- Action
data_orm = Data_Orm(database=database_management)
forex_accounts = data_orm.items(model=model_account_db)


forex_api = None
forex_accounts = data_orm.items(model=model_account_db, enable=True)
for acc in forex_accounts.data :
    forex_api = Forex_Api(name=acc.name, type=acc.type, username=acc.username, password=acc.password, url=acc.url, key=acc.key)
    forex_api.login()
forex = Forex(forex_api = forex_api)
forex.account_info()

strategy_item = data_orm.items(model=model_strategy_item_db, id=1)
strategy_params = ast.literal_eval(strategy_item.data[0].params)
strategy_instance = ST_01(forex=forex, params=strategy_params)
strategy_instance.end(execute_id=1)




# #--------------------------------------------------------------------------------- Action
# forex = Forex(account="acc-trade")
# forex.api.login()
# result = forex.account_info()
# print(result)
# forex.api.logout()

#--------------------------------------------------------------------------------- Database_orm
# db = database_orm()
# db.create_tables()
# data_orm = Data_Orm()

# obj = model_strategy_db(name="strategy_01", description="", enable=True)
# data_orm.add(model=model_strategy_db, item=obj)
# obj = model_strategy_db(name="strategy_02", description="", enable=True)
# data_orm.add(model=model_strategy_db, item=obj)

# params = {
#     "symbol": "EUR/USD",
#     "amount": 10000,
#     "tp_pips": 1,
#     "st_pips": 10,
# }
# obj = model_strategy_item_db(strategy_id=1, name="EURUSD", description="", enable=True, params=str(params))
# data_orm.add(model=model_strategy_item_db, item=obj)

# params = {
#     "symbol": "EUR/USD",
#     "amount": 10000,
#     "tp_pips": 1,
#     "st_pips": 10,
# }
# obj = model_strategy_item_db(strategy_id=2, name="EURUSD", description="", enable=True, params=str(params))
# data_orm.add(model=model_strategy_item_db, item=obj)

#--------------------------------------------------------------------------------- Action
data = Data_Orm()
forex_api = Forex_Api(account="acc-trade")
forex_api.login()
forex = Forex(forex_api = forex_api)
forex.account_info()

strategy_item = data.item(model=model_strategy_item_db, id=2)
strategy_params = ast.literal_eval(strategy_item.data[0].params)
strategy_params["item_id"] = 2
strategy_instance = ST_02(forex=forex, params=strategy_params)
strategy_instance.start()

forex.api.logout()