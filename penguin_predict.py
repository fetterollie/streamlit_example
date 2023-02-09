import streamlit as st
import pandas as pd
import numpy as np
import joblib

from PIL import Image

# usually use this for personal info with apps etc.
#can put titles headers etc on sidebar
st.sidebar.title('Sidebar')

st.title('This is a title')

st.image('images/penguins.jpg', use_column_width='always')

col1, col2 = st.columns(2)
col1.subheader('Col1')
col2.header('Col2')

#

st.markdown['Markdown **syntax** *works*']
st.write('<h2 style="text-align:center">Text aligned with HTML</h2', unsafe_allow_html=True)

'# magic'
'**Markdown**'
'you can actually just write like this to display'

button1 = st.button('Click me')
if button1:
    st.write('Button was clicked')

check_box1 = st.checkbox('Check box plz')
if check_box1:
    st.write('Box was checked')

test_input = st.number_input('Please enter your age')
st.write(f'You are {test_input} years old')

num_pets = st.slider('How many pets do you have?')