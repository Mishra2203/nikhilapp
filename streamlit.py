import streamlit as st
st.title("UTTAR PRADESH")
st.header("JAAT,PANDIT,GURJAR,THAKUR")
st.image(r'D:\\NIKHIL\\up.jpg')









video_file = st.file_uploader("Upload the song you want to hear and after that fill below all the details", type=['mp4'])
if video_file is not None:
    st.video(video_file.read())


