import google.generativeai as geneai
import os
import streamlit as st

GOOGLE_API_KEY = "AIzaSyACfutFXyc7mylwC8hxjZIyofpnuEwdTik"

geneai.configure(api_key=GOOGLE_API_KEY)

# MOdel Initiate

model = geneai.GenerativeModel('gemini-1.5-flash')



def getResponseFromMOdel(user_input):
    response = model.generate_content(user_input)
    return response.text


st.title("🤓 Chat Bot 🤓")
st.write("it uses Google api")

if "history" not in st.session_state:
    st.session_state["history"] = []


if st.session_state.history:
        for entry in st.session_state.history:
            st.write(f"**User:** {entry['user']}")
            st.write(f"**Bot:** {entry['bot']}")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = getResponseFromMOdel(user_input)
            #st.session_state.history.append((user_input, response))
            st.session_state.history.append({'user': user_input, 'bot': response})
            #st.write(response)
            st.write(f"**User:** {user_input}")
            st.write(f"**Bot:** {response}")
        else:
            st.warning("Enter a prompt")

#user_input = input("Enter your Prompt = ")
#output = getResponseFromMOdel(user_input)

#print(output)