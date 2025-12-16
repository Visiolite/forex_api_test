#--------------------------------------------------------------------------------- Location
# mylib/listen_close_execute.py

#--------------------------------------------------------------------------------- Description
# Listen_Close_Execute

#--------------------------------------------------------------------------------- Import
import time

#--------------------------------------------------------------------------------- Listen_Close_Execute
class Listen_Close_Execute:
    #--------------------------------------------- __init__
    def __init__(self, forex_api, items):
        self.forex_api = forex_api
        self.items = items
    
    #--------------------------------------------- start
    def start(self):
        while True:
            time.sleep(5)
            for item in self.items:
                print(f"Processing closed trade: {item}")