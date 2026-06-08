import streamlit as st
import google.generativeai as genai 
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("SMART EMAIL WRITER")
prompt=st.text_input("Enter your message:")
if st.button("submit"):
    response=model.generate_content(prompt+"Read the provided email and generate a professional reply. Create a suitable subject line, maintain an appropriate tone based on the email context, and write a clear, polite, and well-structured response. Ensure the reply is concise, professional, and ready to send.")
    st.write(response.text)
