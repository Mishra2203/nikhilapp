import streamlit as st
st.heading("UTTAR PRADESH")
st.heading("JAAT,PANDIT,GURJAR,THAKUR")
st.image(gettyimages-1372098408-612x612.jpg, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")









video_file = st.file_uploader("Upload the song you want to hear and after that fill below all the details", type=['mp4'])
if video_file is not None:
    st.video(video_file.read())


