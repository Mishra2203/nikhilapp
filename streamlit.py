import streamlit as st
name=st.text_input['Enter your name']
st.write("Hello",name)
st.subheader("chosoe your gender")
st.radio('select',('male','female'))
st.subheader("enter your current education")
st.selectbox("education:",['10','12','Btech','Mbbs','others','nalla'])
like=st.slider('you like this site',1,100,step=1)
st.write('thanks for your answer',like)
if(st.button('i am not a robot')):
 st.write("i know you are human")
