import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from yfinance import ticker


st.write("""
#                   STOCK PRICE DATA
Shown are the stock opening price, closing price and the volume of Microsoft!
""")

#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1m', start='2010-5-31', end='2021-5-31')

selected = st.selectbox("Stock data", list(['Closing Price','Opening Price','Volume','High','Low','Dividends','Stock Splits']))


if (selected == "Opening Price"):
    st.write("""
    ## Opening Price
    """)
    st.line_chart(tickerDf.Open)

if (selected == "Closing Price"):
    st.write("""
    ## Closing Price
    """)

    st.line_chart(tickerDf.Close)

if (selected == 'Volume'):
    st.write("""
    ## Volume
    """)
    st.line_chart(tickerDf.Volume)

if (selected == 'High'):
    st.write("""
    ## High point
    """)
    st.line_chart(tickerDf.High)

if (selected == 'Low'):
    st.write("""
    ## Low point
    """)
    st.line_chart(tickerDf.Volume)

if (selected == 'Dividends'):
    st.write("""
    ## Dividends
    """)
    st.line_chart(tickerDf.Dividends)

if (selected == 'Stock Splits'):
    st.write("""
    ## Stock Splits
    """)
    st.line_chart(tickerDf["Stock Splits"])



dataframe = pd.DataFrame(tickerDf)

st.write(""""
# For Those Who Love Tables!!

""")

st.dataframe(dataframe)

ticker.print_function

# def plot_graphs():
#     d1 = [1,2,3,4]
#     d2 = [1,2,3,4]
#     plt.plot(d1, d2)
#     plt.show


# plot_graphs()
# plt.plot(dataframe["Close"], dataframe["Open"])
# plt.xlabel("Closing price")
# plt.ylabel("Open price")
# plt.show()

#Open	High	Low	Close	Volume	Dividends	Stock Splits
