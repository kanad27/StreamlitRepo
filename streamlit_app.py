import streamlit as st

st.balloons()

st.info('This is a Streamlit Test Application', icon="ℹ️")

with st.echo():
    st.write('This is how text is displayed in Streamlit')
