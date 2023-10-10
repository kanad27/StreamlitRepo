import streamlit as st
import cv2
import numpy as np

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





img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)
