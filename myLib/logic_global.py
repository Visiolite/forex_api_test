#--------------------------------------------------------------------------------- Location
# myLib/logic_global.py

#--------------------------------------------------------------------------------- Description
# logic_global

#--------------------------------------------------------------------------------- Method
#-------------------------- load_config
def load_config():
    import os, yaml
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.environ.get("CONFIG_PATH", os.path.join(root_dir, "config.yaml"))
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

#-------------------------- load_log
def load_log():
    from myLib.log import Log
    return Log()

#-------------------------- load_data
def load_data():
    from myLib.data_orm import Data_Orm
    from myLib.data_sql import Data_SQL
    data_instance = {}
    database_management = config.get("general", {}).get("database_management", {})
    database_data = config.get("general", {}).get("database_data", {})
    data_instance['management_orm'] = Data_Orm(database=database_management)

    data_sql = Data_SQL(database=database_management)
    data_sql.db.open()
    data_instance['management_sql'] = data_sql
    
    return data_instance

#-------------------------- load_forex
def load_forex():
    from myLib.forex_api import Forex_Api
    from myModel.model_account import model_account_db
    from myLib.data_orm import Data_Orm
    from myLib.data_sql import Data_SQL
    forex_apis = {}
    data_orm = Data_Orm()
    forex_accounts = data_orm.items(model=model_account_db, enable=True)
    for acc in forex_accounts.data :
        forex_api = Forex_Api(name=acc.name, type=acc.type, username=acc.username, password=acc.password, url=acc.url, key=acc.key)
        forex_api.login()
        forex_apis[acc.id] = forex_api
    return forex_apis

#--------------------------------------------------------------------------------- Debug
debug = {
    "Database_Orm" : 
    {
        "add":{"log":False, "verbose":False, "model":"Database_Orm"},
        "items":{"log":False, "verbose":False, "model":"Database_Orm"},
        "update":{"log":False, "verbose":False, "model":"Database_Orm"},
        "delete":{"log":False, "verbose":False, "model":"Database_Orm"},
        "create_all_tables":{"log":False, "verbose":False, "model":"Database_Orm"},
        "create":{"log":False, "verbose":False, "model":"Database_Orm"},
        "truncate":{"log":False, "verbose":False, "model":"Database_Orm"},
        "drop":{"log":False, "verbose":False, "model":"Database_Orm"},
    },
    "Database_SQL" : 
    {
        "add":{"log":False, "verbose":False, "model":"Database_Orm"},
        "items":{"log":False, "verbose":False, "model":"Database_Orm"},
        "update":{"log":False, "verbose":False, "model":"Database_Orm"},
        "delete":{"log":False, "verbose":False, "model":"Database_Orm"},
        "create_all_tables":{"log":False, "verbose":False, "model":"Database_Orm"},
        "create":{"log":False, "verbose":False, "model":"Database_Orm"},
        "truncate":{"log":False, "verbose":False, "model":"Database_Orm"},
        "drop":{"log":False, "verbose":False, "model":"Database_Orm"},
    },
    "Data_Orm" : 
    {
        "add":{"log":False, "verbose":False, "model":"Database_Orm"},
        "items":{"log":False, "verbose":False, "model":"Database_Orm"},
        "update":{"log":False, "verbose":False, "model":"Database_Orm"},
        "delete":{"log":False, "verbose":False, "model":"Database_Orm"},
        "create_all_tables":{"log":False, "verbose":False, "model":"Database_Orm"},
        "create":{"log":False, "verbose":False, "model":"Database_Orm"},
        "truncate":{"log":False, "verbose":False, "model":"Database_Orm"},
        "drop":{"log":False, "verbose":False, "model":"Database_Orm"},
    },
    "Data_SQL" : 
    {
        "add":{"log":False, "verbose":False, "model":"Database_Orm"},
        "items":{"log":False, "verbose":False, "model":"Database_Orm"},
        "update":{"log":False, "verbose":False, "model":"Database_Orm"},
        "delete":{"log":False, "verbose":False, "model":"Database_Orm"},
        "create_all_tables":{"log":False, "verbose":False, "model":"Database_Orm"},
        "create":{"log":False, "verbose":False, "model":"Database_Orm"},
        "truncate":{"log":False, "verbose":False, "model":"Database_Orm"},
        "drop":{"log":False, "verbose":False, "model":"Database_Orm"},
    },
    "Implementation_Management" : 
    {
        "instrument":{"log":False, "verbose":True, "model":"Implementation"},
        "account":{"log":False, "verbose":True, "model":"Implementation"},
        "strategy":{"log":False, "verbose":True, "model":"Implementation"},
        "strategy_item":{"log":False, "verbose":True, "model":"Implementation"},
        "live_execute":{"log":False, "verbose":True, "model":"Implementation"},
    },
    "Logic_Management" : 
    {
        "order_detaile":{"log":False, "verbose":False, "model":"Implementation"},
    },
    "Forex_Api" : 
    {
        "login":{"log":False, "verbose":True, "model":"Forex"},
        "logout":{"log":False, "verbose":True, "model":"Forex"},
    },
    "Forex" : 
    {
        "store":{"log":False, "verbose":True, "model":"Forex"},
        "symbol":{"log":False, "verbose":True, "model":"Forex"},
        "history":{"log":False, "verbose":True, "model":"Forex"},
        "account_info":{"log":False, "verbose":True, "model":"Forex"},
        "trade_list":{"log":False, "verbose":True, "model":"Forex"},
        "trade_open":{"log":False, "verbose":True, "model":"Forex"},
        "order_close":{"log":False, "verbose":True, "model":"Forex"},
        "order_close_all":{"log":False, "verbose":True, "model":"Forex"},
    },
    "Data" : 
    {
        "save":{"log":False, "verbose":True, "model":"Data"},
        "get_max_min":{"log":False, "verbose":False, "model":"Data"},
    },
    "ST_01" : 
    {
        "start":{"log":False, "verbose":True, "model":"Data"},
        "order_close":{"log":False, "verbose":True, "model":"Data"},
        "price_change":{"log":False, "verbose":True, "model":"Data"},
        "end":{"log":False, "verbose":True, "model":"Data"}
    },
    "ST_02" : 
    {
        "start":{"log":False, "verbose":True, "model":"Data"},
        "order_close":{"log":False, "verbose":True, "model":"Data"},
        "price_change":{"log":False, "verbose":True, "model":"Data"},
        "end":{"log":False, "verbose":True, "model":"Data"}
    },
    "ST_03" : 
    {
        "start":{"log":False, "verbose":True, "model":"Data"},
        "order_close":{"log":False, "verbose":True, "model":"Data"},
        "price_change":{"log":False, "verbose":True, "model":"Data"},
        "end":{"log":False, "verbose":True, "model":"Data"}
    },
    "ST_04" : 
    {
        "start":{"log":False, "verbose":True, "model":"Data"},
        "order_close":{"log":False, "verbose":True, "model":"Data"},
        "price_change":{"log":False, "verbose":True, "model":"Data"},
        "end":{"log":False, "verbose":True, "model":"Data"}
    },
    "ST_05" : 
    {
        "start":{"log":False, "verbose":True, "model":"Data"},
        "order_close":{"log":False, "verbose":True, "model":"Data"},
        "price_change":{"log":False, "verbose":True, "model":"Data"},
        "end":{"log":False, "verbose":True, "model":"Data"}
    },
}

#--------------------------------------------------------------------------------- Action
config = load_config()
log_instance = load_log()
data_instance = load_data()
forex_apis = {}