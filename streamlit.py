import streamlit as st
from PIL import Image
img = Image.open('D:\\NIKHIL\\up.jpg')
st.image(img)
st.button("Enter IN UTTAR PRADESH")
st.title("UTTAR PRADESH")
st.header("JAAT,PANDIT,GURJAR,THAKUR")
video_file = st.file_uploader("Upload the song you want to hear and after that fill below all the details", type=['mp4'])



