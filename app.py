import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Streamlit page config
st.set_page_config(
    page_title="Groq Streaming Chatbot",
    page_icon="🤖"
)

st.title("🤖 Groq Streaming Chatbot")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):

        message_placeholder = st.empty()
        full_response = ""

        # Streaming response from Groq
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages,
            stream=True
        )

        # Read streamed chunks
        for chunk in stream:

            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content

                full_response += content

                # Typing effect
                message_placeholder.markdown(full_response + "▌")

        # Final response without cursor
        message_placeholder.markdown(full_response)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )