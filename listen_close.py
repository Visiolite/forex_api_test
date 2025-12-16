#--------------------------------------------------------------------------------- Location
# listen_close.py

#--------------------------------------------------------------------------------- Description
# listen_close

#--------------------------------------------------------------------------------- Import
#--------------------------------------------- Forex
from forexconnect import ForexConnect, fxcorepy
from forexconnect.TableListener import TableListener
import forexconnect.lib
import datetime
import time
from myLib.logic_global import config, load_forex_api, list_close
load_forex_api()
from myLib.logic_global import forex_apis

#--------------------------------------------------------------------------------- Listen_Close
class Listen_Close:
    #--------------------------------------------- __init__
    def __init__(self, forex_api, items):
        self.forex_api = forex_api
        self.items = items
        self.listener = None
        self.close_table = None
        self.is_running = False
        
    #--------------------------------------------- CloseTradesListener
    class CloseTradesListener(TableListener):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            
        def on_added(self, row_id, row):
            item = {
                "date": datetime.datetime.now().timestamp(), 
                "order_id": row.open_order_id, 
                "profit": row.gross_pl
            }
            self.parent.items.append(item)
            print(f"Trade closed: {item}")
    
    #--------------------------------------------- start
    def start(self):
        if self.is_running:
            print("Listener is already running.")
            return
            
        print("Initializing listener...")
        self.listener = self.CloseTradesListener(self)
        table_manager = self.forex_api.fx.table_manager
        
        # Wait for tables to load
        while table_manager.status != forexconnect.lib.fxcorepy.O2GTableManagerStatus.TABLES_LOADED:
            time.sleep(0.1)
        
        # Subscribe to closed trades
        self.close_table = table_manager.get_table(ForexConnect.CLOSED_TRADES)
        self.close_table.subscribe_update(fxcorepy.O2GTableUpdateType.INSERT, self.listener)
        self.is_running = True
        
        print("Listening for trade close events... Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping listener...")
            self.stop()
    
    #--------------------------------------------- stop
    def stop(self):
        if self.close_table and self.listener:
            self.close_table.unsubscribe_update(fxcorepy.O2GTableUpdateType.INSERT, self.listener)
        if self.forex_api:
            self.forex_api.logout()
        self.is_running = False
        print("Listener stopped.")

#--------------------------------------------------------------------------------- Main
if __name__ == "__main__":
    listener_close = Listen_Close(forex_api=forex_apis[1], items=list_close)
    listener_close.start()