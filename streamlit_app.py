import streamlit as st
import datetime

st.balloons()

st.info('This is a Streamlit Test Application', icon="ℹ️")

with st.echo():
    st.write('This is how text is displayed in Streamlit')

title = st.text_input('Enter your POD', 'Database Security and Authentication Management')
st.write('We are working in POD - ', title)

with st.container():
    st.write('New Section')
    
    color = st.color_picker('Pick A Color', '#00f900')
    st.write('The current color is', color)


d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

# Import python packages

# Write directly to the app
st.title("Example Streamlit App :balloon:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

# Get the current credentials
session = get_active_session()


answer = prompt('Give me some input: ')
print('You said: %s' % answer)
st.write(answer)
