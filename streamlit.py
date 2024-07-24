import streamlit as st
from PIL import Image
image_file = st.file_uploader("D:\\NIKHIL\\up.jpg", type=['jpg', 'png'])
if image_file is not None:
    img = Image.open(image_file)
    st.image(img)

st.title("UTTAR PRADESH")
st.header("JAAT,PANDIT,GURJAR,THAKUR")



video_file = st.file_uploader("Upload the song you want to hear and after that fill below all the details", type=['mp4'])
if video_file is not None:
    st.video(video_file.read(),5)


