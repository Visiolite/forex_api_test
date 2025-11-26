#--------------------------------------------------------------------------------- Location
# myLib/store.py

#--------------------------------------------------------------------------------- Description
# Store

#--------------------------------------------------------------------------------- Import
import os,sys
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{root_dir}/myLib")
from myLib.forexconnect_api import Forex
from forexconnect import ForexConnect, fxcorepy

#--------------------------------------------------------------------------------- Action
def session_status_changed(self, session: fxcorepy.O2GSession, status: fxcorepy.AO2GSessionStatus.O2GSessionStatus):
    print("Trading session status: " + str(status))

with ForexConnect() as fx:
    fx.login(
        "52035534",
        "fjf0tzq",
        "http://www.fxcorporate.com/Hosts.jsp",
        "Demo",
        session_status_changed
    )


    instrument="EUR/USD"
    command=fxcorepy.Constants.Commands.CREATE_ORDER,
    order_type=fxcorepy.Constants.Orders.TRUE_MARKET_OPEN,
    buy_sell=fxcorepy.Constants.BUY
    account_id = fx.get_table(ForexConnect.ACCOUNTS)[0].account_id
    offer_id = 1
    amount=10000


    request = fx.create_order_request(
        command=command,
        order_type=order_type,
        BUY_SELL=buy_sell,
        account_id=account_id,
        offer_id=offer_id,
        amount=amount,
        time_in_force="FOK"
    )


    if request is None:
        raise Exception("Cannot create order request")

    # Send request
    response = fx.send_request(request)

    print("Order sent. RequestID:", response.request_id)



# fx = Forex(account="acc-history1")
# fx.login()
# fx.info = fx.account_info().data
# instruments =fx.instruments().data
# open = fx.trade_open(OFFER_ID=instruments["EUR/USD"], buy_sell="B", amount=2000)
# close = fx.trade_close_all()
# fx.logout()
