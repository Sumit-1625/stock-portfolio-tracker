import streamlit as st

# Hardcoded stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "MSFT": 330, "GOOG": 140, "AMZN": 135}

st.title("📈 Stock Portfolio Tracker")
portfolio = {}
total_value = 0

# Input section
stock = st.selectbox("Choose a stock:", list(stock_prices.keys()))
qty = st.number_input("Quantity", min_value=1, value=1)
if st.button("Add Stock"):
    portfolio[stock] = portfolio.get(stock, 0) + qty
    st.session_state["portfolio"] = portfolio

# Display section
if "portfolio" in st.session_state:
    st.subheader("Portfolio Summary")
    for s, q in st.session_state["portfolio"].items():
        value = stock_prices[s] * q
        total_value += value
        st.write(f"{s}: {q} shares → ${value}")
    st.write(f"*Total Investment Value:* ${total_value}")