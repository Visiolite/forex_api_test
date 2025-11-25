#--------------------------------------------------------------------------------- Location
# myLib/store.py

#--------------------------------------------------------------------------------- Description
# Store

#--------------------------------------------------------------------------------- Import
import os,sys
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{root_dir}/myLib")
from myLib.forexconnect_api import Forex

#--------------------------------------------------------------------------------- Action
fx = Forex(account="acc-trade")
fx.login()
fx.info = fx.account_info().data
open = fx.trade_open(symbol="EUR/USD", buy_sell="B", amount=2000)
close = fx.trade_close_all()
fx.logout()
