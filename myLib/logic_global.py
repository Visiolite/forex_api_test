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

#--------------------------------------------------------------------------------- Action
config = load_config()
debug = config.get("debug", {})
log_instance = load_log()
data_instance = load_data()
forex_apis = {}