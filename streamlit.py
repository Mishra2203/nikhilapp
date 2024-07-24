import streamlit as st
from PIL import Image
st.button("Enter IN UTTAR PRADESH")
st.title("UTTAR PRADESH")
st.header("JAAT,PANDIT,GURJAR,THAKUR")


    img = Image.open("D:\\NIKHIL\\up.jpg")
    st.image(img)




video_file = st.file_uploader("Upload the song you want to hear and after that fill below all the details", type=['mp4'])
if video_file is not None:
    st.video(video_file.read())


