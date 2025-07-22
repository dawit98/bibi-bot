from indicators import get_rsi, get_macd

def get_signal(ticker):
    rsi = get_rsi(ticker)
    macd, macd_signal = get_macd(ticker)
    if rsi < 30 and macd > macd_signal:
        return "🌱 Bibi says: Time to Grow!", "Looks strong for a swing entry — slowly increase your position."
    elif rsi > 70 and macd < macd_signal:
        return "⚠️ Bibi says: Pause the Ride", "It feels stretched — consider taking some profits."
    else:
        return "☁️ Bibi says: Just Breathe", "No clear signal — let’s wait together."
