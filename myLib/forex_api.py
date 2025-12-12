#--------------------------------------------------------------------------------- Location
# myLib/forex_api.py

#--------------------------------------------------------------------------------- Description
# forexconnect

#--------------------------------------------------------------------------------- Import
import inspect, time
from myLib.model import model_output
from myLib.utils import debug, sort
from forexconnect import ForexConnect, fxcorepy
from myLib.log import Log

#--------------------------------------------------------------------------------- Action
class Forex_Api:
    #--------------------------------------------- init
    def __init__(self, name=None,type=None, username=None, password=None, url=None, key=None, instance_log:Log =None):
        #--------------------Variable
        self.this_class = self.__class__.__name__
        self.id = None
        self.name = name
        self.server = type
        self.username = username
        self.password = password
        self.url = url
        self.key = key
        #--------------------Instance
        self.instance_log = instance_log if instance_log else Log()
        self.fx = ForexConnect()

    #--------------------------------------------- on_status_changed
    def session_status_changed(self, session: fxcorepy.O2GSession, status: fxcorepy.AO2GSessionStatus.O2GSessionStatus):
        print("Trading session status: " + str(status))

    #--------------------------------------------- login
    def login(self):
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method

        try:
            #--------------Variable
            start_time = time.time()
            #--------------Action
            self.fx.login(self.username, self.password, self.url, self.server, self.session_status_changed)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.message = self.name
            #--------------Verbose
            if verbose : self.instance_log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.instance_log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.instance_log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.instance_log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output

    #--------------------------------------------- logout
    def logout(self):
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method

        try:
            #--------------Variable
            start_time = time.time()
            #--------------Action
            self.fx.logout()
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.message = self.name
            #--------------Verbose
            if verbose : self.instance_log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.instance_log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.instance_log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.instance_log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output