import streamlit as st
import random

# --- FAQ Database ---
FAQS = {
    "programs": "Iron Lady offers leadership programs, confidence-building workshops, and career acceleration programs tailored for women.",
    "duration": "Most programs run between 6 weeks to 3 months, depending on the module.",
    "mode": "All programs are conducted online with live interactive sessions.",
    "certificate": "Yes! Participants receive an official Iron Lady certificate upon completion.",
    "mentors": "Our mentors are certified leadership coaches, industry professionals, and global thought leaders."
}

# --- Helper function ---
def get_answer(user_input):
    user_input = user_input.lower()

    # Greeting responses
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    if any(greet in user_input for greet in greetings):
        return random.choice([
            "Hello 👋 I’m the Iron Lady Assistant! How can I help you today?",
            "Hi there! 😊 Ask me about our leadership programs.",
            "Hey! I can answer FAQs about Iron Lady’s programs, duration, mode, certificates, or mentors."
        ])

    # FAQ matching
    if "program" in user_input:
        return FAQS["programs"]
    elif "duration" in user_input:
        return FAQS["duration"]
    elif "online" in user_input or "offline" in user_input or "mode" in user_input:
        return FAQS["mode"]
    elif "certificate" in user_input:
        return FAQS["certificate"]
    elif "mentor" in user_input or "coach" in user_input:
        return FAQS["mentors"]

    # Fallback
    return random.choice([
        "Hmm 🤔 I’m not sure about that. Can you try asking about programs, duration, mode, certificates, or mentors?",
        "Interesting question! Currently, I can answer FAQs about Iron Lady’s programs.",
        "Could you ask me about programs, duration, mode, certificates, or mentors? 😊"
    ])

# --- Streamlit UI ---
st.set_page_config(page_title="Iron Lady Chatbot", page_icon="🤖", layout="centered")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f9c5d1, #9796f0);
        font-family: 'Trebuchet MS', sans-serif;
    }
    .stTextInput>div>div>input {
        border: 2px solid #FF69B4;
        border-radius: 10px;
    }
    .chat-bubble {
        padding: 10px 15px;
        border-radius: 15px;
        margin: 8px 0;
        display: inline-block;
        max-width: 80%;
    }
    .user-bubble {
        background-color: #ffdae0;
        color: black;
        text-align: right;
        float: right;
        clear: both;
    }
    .bot-bubble {
        background-color: #e3e6ff;
        color: black;
        text-align: left;
        float: left;
        clear: both;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Iron Lady FAQ Chatbot")
st.write("✨ Welcome! I’m the Iron Lady Assistant. Ask me about our leadership programs!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💬 Type your question:")

if user_input:
    answer = get_answer(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))

# Display styled chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div class='chat-bubble user-bubble'>🧑 {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot-bubble'>🤖 {msg}</div>", unsafe_allow_html=True)
