#--------------------------------------------------------------------------------- Location
# myLib/test.py

#--------------------------------------------------------------------------------- Description
# test

#--------------------------------------------------------------------------------- Import
from myLib.logic_global import load_forex_api
from myLib.logic_management import Logic_Management
from myLib.forex import Forex
from forexconnect import ForexConnect, fxcorepy
load_forex_api()
from myLib.logic_global import forex_apis

#--------------------------------------------------------------------------------- Action  : Order cloese
def run() :
    command = fxcorepy.Constants.Commands.CREATE_ORDER
    order_type = fxcorepy.Constants.Orders.TRUE_MARKET_OPEN

    fx = forex_apis[1]
    request = fx.fx.create_order_request(
        ACCOUNT_ID=fx.id,
        command=command, 
        order_type=order_type,
        BUY_SELL= "B",
        SYMBOL = "EUR/USD",
        AMOUNT= 1000
    )
    response = fx.fx.send_request_async(request)
    order_id = getattr(response, "order_id", None) if response else None
    print(order_id)

run()

