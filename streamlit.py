import streamlit as st
import numpy as np

# Display a chat message and write statement
st.chat_message("user")
st.write("Hello ")

# Display a line chart
st.line_chart(np.random.randn(30, 3))

# Display a chat input widget
st.chat_input("Say something")

# File uploader for video
video_file = st.file_uploader("Upload the song you want to hear and after that fill below all the details", type=['mp4'])
if video_file is not None:
    st.video(video_file.read())

# Display an image
st.subheader("Upload image")
st.image("https://youtu.be/YkGFaQQQsvQ?feature=shared.jpg")

# Get user's name
name = st.text_input('Enter your name')
st.write(f"Hello, {name}!")

# Get user's age
st.subheader("Enter your age")
st.number_input('Select your age', 0, 100)

# Get date input
st.date_input('Date')
# Get user's gender
st.subheader("Choose your gender")
gender = st.radio('Select', ['Not preferred to say', 'Male', 'Female', 'Others'])

# Get user's current education
st.subheader("Enter your current education")
education = st.selectbox("Education:", ['10', '12', 'B.Tech', 'MBBS', 'Others', 'N/A'])

# Get user's liking for the site
like = st.slider('How much do you like this site?', 1, 100, step=1)
st.write(f'Thanks for your answer: {like}')

# Check if user is not a robot
if st.button('I am not a robot'):
    st.write("I know you are human!")

# Text area for user input
textarea = st.text_area('Write something about yourself')
st.write(textarea)





