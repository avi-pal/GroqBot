import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# -------------------------
# Load ENV
# -------------------------
load_dotenv()

from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    api_key = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=api_key)

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Groq AI Chat",
    page_icon="✨",
    layout="centered"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #1e293b 100%
    );
    color: white;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 0;
    color: white;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 2rem;
}

/* Chat bubbles */
.user-bubble {
    background: #2563eb;
    padding: 12px 18px;
    border-radius: 18px 18px 4px 18px;
    margin: 8px 0;
    color: white;
}

.bot-bubble {
    background: #1e293b;
    padding: 12px 18px;
    border-radius: 18px 18px 18px 4px;
    margin: 8px 0;
    border: 1px solid #334155;
    color: white;
}

/* Input box */
.stChatInput input {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid #334155 !important;
}

/* Hide Streamlit Menu/Footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------
st.markdown(
    "<h1 class='main-title'>✨ Groq AI Chat</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Fast AI chatbot powered by Groq + Streamlit</p>",
    unsafe_allow_html=True
)

# -------------------------
# Session State
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Display Messages
# -------------------------
for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(
            f"""
            <div class="user-bubble">
                🧑‍💻 {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f"""
            <div class="bot-bubble">
                🤖 {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------
# User Input
# -------------------------
prompt = st.chat_input("Message Groq AI...")

if prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Show user message instantly
    st.markdown(
        f"""
        <div class="user-bubble">
            🧑‍💻 {prompt}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Assistant container
    response_container = st.empty()

    full_response = ""

    # Streaming response
    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages,
        stream=True
    )

    # Stream chunks
    for chunk in stream:

        if chunk.choices[0].delta.content is not None:

            content = chunk.choices[0].delta.content
            full_response += content

            response_container.markdown(
                f"""
                <div class="bot-bubble">
                    🤖 {full_response}▌
                </div>
                """,
                unsafe_allow_html=True
            )

    # Final response
    response_container.markdown(
        f"""
        <div class="bot-bubble">
            🤖 {full_response}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })