from indicators import get_rsi, get_macd

def get_signal(ticker):
    rsi_series = get_rsi(ticker)
    macd_series, macd_signal_series = get_macd(ticker)

    if rsi_series is None or macd_series is None or macd_signal_series is None:
        return "⚠️ Bibi says: Something’s off.", "Couldn’t fetch data right now. Try another symbol or wait a moment."

    try:
        # Get last value from the series
        rsi = float(rsi_series)
        macd = float(macd_series)
        macd_signal = float(macd_signal_series)

        if rsi < 30 and macd > macd_signal:
            return "🌱 Bibi says: Time to Grow!", "Looks strong for a swing entry — slowly increase your position."
        elif rsi > 70 and macd < macd_signal:
            return "⚠️ Bibi says: Pause the Ride", "It feels stretched — consider taking some profits."
        else:
            return "☁️ Bibi says: Just Breathe", "No clear signal — let’s wait together."

    except Exception as e:
        return "😕 Bibi says: Hmmm.", f"Something went wrong while reading the market: {e}"
