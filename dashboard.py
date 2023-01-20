import streamlit as st
import pandas as pd
import numpy as np
import requests 
import tweepy
import yfinance as yf
import json
import config

# init tweepy api
auth = tweepy.OAuthHandler(
   config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET
)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN,config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


option = st.sidebar.selectbox(
    "Which dashboard would you like?", ('Twitter', 'WallStreetBets', 'Stocktwits','Chart', 'Pattern', 'Finance News')
)

st.header(option)

if option == 'Twitter':
    st.subheader("twitter dashboard logic")
    
    tweets = api.user_timeline(screen_name= 'delatone')
    st.write(tweets)




if option == 'Chart':
    st.subheader("Chart dashboard logic")

if option == 'WallStreetBets':
    st.subheader("WSB dashboard logic")

if option == 'Finance News':
    st.subheader("Trending News:")
    symbol = st.sidebar.text_input('Symbol', value='QQQ', max_chars=5)

    desiredSymbol = yf.Ticker(symbol)

    data =desiredSymbol.news

    # st.write(data)

    st.write('1. ' + data[0]['title'])
    st.write( data[0]['link'])
    st.write('2. ' + data[1]['title'])
    st.write( data[1]['link'])
    st.write('3. ' + data[2]['title'])
    st.write( data[2]['link'])
    st.write('4. ' + data[3]['title'])
    st.write( data[3]['link'])
    st.write('5. ' + data[4]['title'])
    st.write( data[4]['link'])

    st.write('6. ' + data[5]['title'])
    st.write( data[5]['link'])
    st.write('7. ' + data[6]['title'])
    st.write( data[6]['link'])
    st.write('8. ' + data[7]['title'])
    st.write( data[7]['link'])

 
if option == 'Stocktwits':
    #read text ("ticker symbol") from the sidebar 
    #default value 'QQQ'
    symbol = st.sidebar.text_input('Symbol', value='QQQ', max_chars=5)
    # st.subheader("Stocktwits dashboard logic")


# Get symbol specific stream data from stocktwits via API request
# return all the recent mentions of specified symbol
    r = requests.get(f'https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json')

# Get response as json
    data = r.json()

    for message in data['messages']:    
        st.image(message['user']['avatar_url'])
        st.write(message['user']['username'])
        st.write(message['created_at'])
        st.write(message['body'])


    # st.write(data)



if option == 'Pattern':
    st.subheader("Pattern dashboard logic")


