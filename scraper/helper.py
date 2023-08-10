import yfinance as yf
import pandas as pd
def getStockData(stock_name,start_timestamp=None):
    try:
        if start_timestamp:
            st_name = stock_name + '.NS'
            data = yf.download(st_name) #yfinance is imported as yf 
            d = dict()
            d['symbol'] = stock_name
            dd=dict()
            for ind in range(len(data)):
                if data.index[ind]>=pd.Timestamp(start_timestamp):
                    ddd = dict()
                    ddd['open'] = data['Open'][ind]
                    ddd['high'] = data['High'][ind]
                    ddd['low'] = data['Low'][ind]
                    ddd['adjClose'] = data['Adj Close'][ind]
                    ddd['close'] = data['Close'][ind]
                    ddd['volume'] = data['Volume'][ind]

                    ddkey = str(data.index[ind])
                    dd[ddkey] = ddd 
                d['dates'] = dd
                return d 
        else:
            st_name = stock_name + '.NS'
            data = yf.download(st_name) #yfinance is imported as yf 
            d = dict()
            d['symbol'] = stock_name
            dd=dict()
            for ind in range(len(data)):
                ddd = dict()
                ddd['open'] = data['Open'][ind]
                ddd['high'] = data['High'][ind]
                ddd['low'] = data['Low'][ind]
                ddd['adjClose'] = data['Adj Close'][ind]
                ddd['close'] = data['Close'][ind]
                ddd['volume'] = data['Volume'][ind]

                ddkey = str(data.index[ind])
                dd[ddkey] = ddd 
            d['dates'] = dd
            return d 
    except :
        print("Failed")