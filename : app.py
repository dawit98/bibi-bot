import random
quotes = [
    "Make money, be happy — Bibi 💖",
    "The market loves the calm — stay steady 📉📈",
    "No panic, just patience 🧘‍♀️",
    "You win when you wait 🕰️",
    "Every dip is a blessing in disguise 🌧️→🌞"
import streamlit as st
from bibi_bot import get_signal
from datetime import date

st.title("BIBI Bot 🌸")
st.write("_\"Make money, be happy\"_ — Bibi’s mantra", unsafe_allow_html=True)

ticker = st.text_input("Enter a ticker (e.g. BTC-USD, AAPL)")
if st.button("Get Today’s Bibi Signal"):
    if not ticker:
        st.error("Please enter a ticker.")
    else:
        signal, advice = get_signal(ticker)
        st.subheader(signal)
        st.write(advice)
        st.write(f"*Generated on {date.today()}*")
