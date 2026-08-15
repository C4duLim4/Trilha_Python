import streamlit as st
import pandas as pd

st.title('Hello, World')
st.write('This is my first app with StreamLit')

st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a simply text')

st.markdown('*Streamlit* is **really** ***cool***.')

st.markdown('''
...     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
...     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')

data = {
    'nome': ['Carlos', 'Eduardo', 'Lima'],
    'Idade': [22, 23, 19],
    'Salário': [8000, 9000, 10000]
}

df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)
