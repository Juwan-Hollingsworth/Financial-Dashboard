import streamlit as st
import pandas as pd
import numpy as np
import requests 

# st.title("This is the title")
# st.header("this is a header")
# st.write("this is regular text")

""""""
#header
##subheader
""""""

# some_dictionary = {
#     "key":"value",
#     "key2": "value2"
# }

# st.write(some_dictionary)

# st.sidebar.title("Dashboard Options")

# df = pd.DataFrame(np.random.randn(50,20), columns=('col %d' % i for i in range(20)))

# st.dataframe(df)

option = st.sidebar.selectbox(
    "Which dashboard would you like?", ('Twitter', 'WallStreetBets', 'Stocktwits','Chart', 'Pattern')
)

st.header(option)

if option == 'Twitter':
    st.subheader("twitter dashboard logic")

if option == 'Chart':
    st.subheader("Chart dashboard logic")

if option == 'WallStreetBets':
    st.subheader("WSB dashboard logic")

if option == 'Stocktwits':
    symbol = st.sidebar.text_input('Symbol', value='QQQ', max_chars=5)
    # st.subheader("Stocktwits dashboard logic")

    r = requests.get(f'https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json')

    data = r.json()

    for message in data['messages']:
       
        st.write(message['created_at'])
        st.write(message['user']['username'])
        st.image(message['user']['avatar_url'])
        st.write(message['body'])


    # st.write(data)



if option == 'Pattern':
    st.subheader("Pattern dashboard logic")


