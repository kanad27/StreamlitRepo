import streamlit as st

st.balloons()

st.info('This is a Streamlit Test Application', icon="ℹ️")

with st.echo():
    st.write('This is how text is displayed in Streamlit')

title = st.text_input('Enter your POD', 'Database Security and Authentication Management')
st.write('We are working in POD - ', title)

st.write('New Section')

color = st.color_picker('Pick A Color', '#00f90f')
st.write('The current color is', color)
