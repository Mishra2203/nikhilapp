import streamlit as st
audio_file=st.file_uploader("Upload the song you want to hear and after that fill below all the details",type=['mp3'])

# Get user's name
name = st.text_input('Enter your name')
st.write(f"Hello, {name}!")

st.subheader("Enter your age")
st.number_input('Select your age',0,100)
st.date_input('Date')

# Get user's gender
st.subheader("Choose your gender")
gender = st.radio('Select', ['Not preffered to say','Male', 'Female','Others'])

# Get user's current education
st.subheader("Enter your current education")
education = st.selectbox("Education:", ['10', '12', 'B.Tech', 'MBBS', 'Others', 'NAllA'])

# Get user's liking for the site
like = st.slider('How much do you like this site?', 1, 100, step=1)
st.write(f'Thanks for your answer: {like}')

# Check if user is not a robot
if st.button('I am not a robot'):
    st.write("I know you are human!")

textarea=st.text_area('Write something about yourself')
st.write(textarea)

