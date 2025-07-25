from indicators import get_rsi, get_macd

def get_signal(ticker):
    rsi = get_rsi(ticker)
    macd, macd_signal = get_macd(ticker)

    if rsi is None or macd is None or macd_signal is None:
        return "⚠️ Bibi says: Something’s off.", "Couldn’t fetch data right now. Try another symbol or wait a moment."

    try:
        if rsi < 30 and macd > macd_signal:
            return "🌱 Bibi says: Time to Grow!", "Looks strong for a swing entry — slowly increase your position."
        elif rsi > 70 and macd < macd_signal:
            return "⚠️ Bibi says: Pause the Ride", "It feels stretched — consider taking some profits."
        else:
            return "☁️ Bibi says: Just Breathe", "No clear signal — let’s wait together."
    except Exception as e:
        return "😕 Bibi says: Hmmm.", f"Something went wrong while reading the market: {e}"
