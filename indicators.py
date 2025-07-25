import yfinance as yf
import pandas as pd

def get_rsi(ticker, period=14):
    try:
        data = yf.download(ticker, period="1mo", interval="1d")
        if data.empty:
            return None
        delta = data['Close'].diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi.dropna().iloc[-1]
    except:
        return None

def get_macd(ticker):
    try:
        data = yf.download(ticker, period="1mo", interval="1d")
        if data.empty:
            return None, None
        exp1 = data['Close'].ewm(span=12, adjust=False).mean()
        exp2 = data['Close'].ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        return macd.dropna().iloc[-1], signal.dropna().iloc[-1]
    except:
        return None, None
