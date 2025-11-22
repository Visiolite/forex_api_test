import time

class Tools:
    """ Tools class"""

    #------------------------------------------------------------------- [ Speed ]
    @classmethod
    def speed(func):
        def wrapper(*args, **kwargs):
            start_time = time.time() 
            result = func(*args, **kwargs)
            print(f"Time : {'{:.0f}'.format(time.time() - start_time)} Seccond")
            return result
        return wrapper

    #------------------------------------------------------------------- [ getTblName ]
    @classmethod
    def getTblName(cls, symbol, timeFrame):
        """ return table name """

        #-----------------------------Variable
        methodName = "getTblName"
        symbol=symbol.replace('/', '')
        symbol=symbol.replace('.', '')
        #-----------------------------Execute
        res = f"{symbol}_{timeFrame}"
        if res[0].isdigit() :
            res = f'"{res}"'

        return res

    #------------------------------------------------------------------- [ getTblName ]
    @classmethod
    def getLogFormat(cls, model, data):
        """ return log format data """

        #-----------------------------Variable
        methodName = "getLogFormat"
        #-----------------------------Execute
        if model == "symbol" : return '{:<7}'.format(data)
        if model == "timeFrame" : return '{:<3}'.format(data)
        if model == "report" : return '{:<19}'.format(data)
        if model == "date" :
            if len(str(data))>19:
                return f"{str(data)[:19]}"
            else:
                return '{:<19}'.format(f'{data}')