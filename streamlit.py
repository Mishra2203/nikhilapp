import streamlit as st
st.title("UTTAR PRADESH")
st.header("JAAT,PANDIT,GURJAR,THAKUR")
video_file = st.file_uploader("Upload the song you want to hear and after that fill below all the details", type=['mp4'])
st.video(video_file,start_time=5)




 
