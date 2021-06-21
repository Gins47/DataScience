import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock price Application 

 """)


def get_user_name():
    return 'John'


# with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

def get_punctuation():
    return '!!!'


greeting = "Hi there, "
value = get_user_name()
punctuation = get_punctuation()

st.write(greeting, value, punctuation)


tickerSymbol = input(f"Enter the symbol of the company ")
#tickerSymbol = 'GOOGL'
# Get data for google
tickerData = yf.Ticker(tickerSymbol)

# Get historical data for Google.
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2021-5-31')


# Open High Low Close Volume Dividends Stock Splits

st.write("Currently showing close data of ", tickerSymbol)
st.line_chart(tickerDf.Close)
st.write("Currently showing volume of  ", tickerSymbol)
st.line_chart(tickerDf.Volume)
st.write("Currently showing high value of  ", tickerSymbol)
st.line_chart(tickerDf.High)
