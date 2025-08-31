import openai
import streamlit as st
from openai import OpenAI, api_key

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

st.title("OMEN by sourav lenka")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-4o
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Add assistant reply to chat
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Display assistant reply
    with st.chat_message("assistant"):
        st.markdown(reply)
