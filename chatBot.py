import streamlit as st
import google.generativeai as genai
genai.configure(api_key="Your_Api_key here")
# initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')
def inputFromUser(userInput):
 response = model.generate_content(userInput)
 return response.text

st.title("Gemmini ChatBot")
user_input = st.text_input("Enter your Prompt")
if st.button("Get Response"):
   if user_input:
    output = inputFromUser(user_input)
    st.write("Gemmini Response Here:")
    st.write(output)
   else:
    st.write("Please enter your Prompt")


