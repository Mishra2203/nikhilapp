import streamlit as st
st.title("UTTAR PRADESH")
st.header("{JAAT},{PANDIT}")
image_file = st.file_uploader("D:\\NIKHIL\\pandit.jpeg", type=['jpeg', 'png'])
image_file = st.file_uploader("D:\\NIKHIL\\jaat.jpeg", type=['jpeg', 'png'])
if image_file is not None:
    img = Image.open(image_file)
    st.image(img)
video_file = st.file_uploader("Upload the song you want to hear and after that fill below all the details", type=['mp4'])
st.video(video_file,start_time=5)




 
