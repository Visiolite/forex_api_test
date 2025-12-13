#--------------------------------------------------------------------------------- Location
# myLib/data_sql.py

#--------------------------------------------------------------------------------- Description
# data_sql

#--------------------------------------------------------------------------------- Import
import inspect, time
from myLib.model import model_output
from myLib.logic_global import config, debug, log_instance
from myLib.utils import sort, get_tbl_name
from myLib.log import Log
from myLib.database_sql import Database_SQL

#--------------------------------------------------------------------------------- Action
class Data_SQL:
    #-------------------------- [Init]
    def __init__(self, database, log=log_instance):
        #--------------------Variable
        self.this_class = self.__class__.__name__
        self.log:Log = log
        #--------------------Data
        database_cfg = config.get("database", {}).get(database, {})
        #--------------------Instance
        self.db = Database_SQL(
            server=database_cfg.get("server"), 
            host=database_cfg.get("host"), 
            port=database_cfg.get("port"), 
            username=database_cfg.get("username"), 
            password=database_cfg.get("password"), 
            database=database_cfg.get("database"), 
            log=self.log
        )

    #-------------------------- [get_max_min]
    def get_max_min(self, instrument, timeframe, mode, filed) -> model_output:
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        start_time = time.time()
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method

        try:
            #-------------- Data
            tblName = get_tbl_name(instrument, timeframe)
            if mode == "max" : query = f"SELECT max({filed}) FROM {tblName}"
            if mode == "min" : query = f"SELECT min({filed}) FROM {tblName}"
            #--------------Action
            result = self.db.item(query)
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.data = result.data
            output.message=f"{instrument} | {timeframe} | {mode} | {filed}"
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output

    #-------------------------- [save]
    def save(self, instrument, timeframe, data, bulk=False) -> model_output:
        #-------------- Description
        # IN     : 
        # OUT    : 
        # Action :
        #-------------- Debug
        this_method = inspect.currentframe().f_code.co_name
        verbose = debug.get(self.this_class, {}).get(this_method, {}).get('verbose', False)
        log = debug.get(self.this_class, {}).get(this_method, {}).get('log', False)
        log_model = debug.get(self.this_class, {}).get(this_method, {}).get('model', False)
        start_time = time.time()
        #-------------- Output
        output = model_output()
        output.class_name = self.this_class
        output.method_name = this_method

        try:
            #-------------- Data
            tblName = get_tbl_name(instrument, timeframe)
            if timeframe == "t1":
                query = f'INSERT INTO {tblName} (date, bid, ask) VALUES '
            else:
                query = f'INSERT INTO {tblName} (date, bidopen, bidclose, bidhigh, bidlow, askopen, askclose, askhigh, asklow) VALUES '
            #--------------Action
            if timeframe == "t1":
                if bulk :
                    data = data.drop_duplicates(subset=["Date"], keep="first")
                    for index, row in data.iloc[::-1].iterrows(): 
                        query += f"('{row['Date']}',{row['Bid']},{row['Ask']}),"
                        iter += 1
                        insert += 1
                    if iter > 0 : query = query[:-1]
                    output.status = self.db.execute(query)
                    if not output.status : insert = 0
                else:
                    for index, row in data.iloc[::-1].iterrows(): 
                        q = query + (f"('{row['Date']}',{row['Bid']},{row['Ask']})")
                        iter += 1
                        if self.db.execute(q) : 
                            insert += 1
                        else:
                            pass
            else:
                if bulk :
                    for index, row in data.iloc[::-1].iterrows(): 
                        query += f"('{row['Date']}',{row['BidOpen']},{row['BidClose']},{row['BidHigh']},{row['BidLow']},{row['AskOpen']},{row['AskClose']},{row['AskHigh']},{row['AskLow']}),"
                        iter += 1
                        insert += 1
                    if iter > 0 : query = query[:-1]
                    output.status = self.db.execute(query)
                    if not output.status : insert = 0
                else:
                    for index, row in data.iloc[::-1].iterrows(): 
                        q = query + (f"('{row['Date']}',{row['BidOpen']},{row['BidClose']},{row['BidHigh']},{row['BidLow']},{row['AskOpen']},{row['AskClose']},{row['AskHigh']},{row['AskLow']})")
                        iter += 1
                        if self.db.execute(q) : insert += 1
            #--------------Output
            output.time = sort(f"{(time.time() - start_time):.3f}", 3)
            output.message =f"{instrument} | {timeframe} | {sort(insert, 6)}"
            #--------------Verbose
            if verbose : self.log.verbose("rep", f"{sort(self.this_class, 8)} | {sort(this_method, 8)} | {output.time}", output.message)
            #--------------Log
            if log : self.log.log(log_model, output)
        except Exception as e:  
            #--------------Error
            output.status = False
            output.message = {"class":self.this_class, "method":this_method, "error": str(e)}
            self.log.verbose("err", f"{self.this_class} | {this_method}", str(e))
            self.log.log("err", f"{self.this_class} | {this_method}", str(e))
        #--------------Return
        return output