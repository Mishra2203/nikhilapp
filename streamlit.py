import streamlit as st

# Get user's name
name = st.text_input('Enter your name')
st.write(f"Hello, {name}!")

# Get user's gender
st.subheader("Choose your gender")
gender = st.radio('Select', ['Male', 'Female'])

# Get user's current education
st.subheader("Enter your current education")
education = st.selectbox("Education:", ['10', '12', 'B.Tech', 'MBBS', 'Others', 'N/A'])

# Get user's liking for the site
like = st.slider('How much do you like this site?', 1, 100, step=1)
st.write(f'Thanks for your answer: {like}')

# Check if user is not a robot
if st.button('I am not a robot'):
    st.write("I know you are human!")

