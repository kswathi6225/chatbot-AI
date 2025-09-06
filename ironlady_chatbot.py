import streamlit as st
import random

# --- FAQ Database ---
FAQS = {
    "programs": "🌟 Iron Lady offers:\n- Leadership Development Programs\n- Confidence Building Workshops\n- Career Acceleration Programs\n- Executive Coaching Sessions",
    "duration": "⏳ Program durations vary:\n- Short workshops: 2–3 days\n- Core programs: 6–8 weeks\n- Advanced leadership journeys: 3 months",
    "mode": "💻 All programs are conducted **online** via live interactive sessions with mentors and peers.",
    "certificate": "🎓 Yes! Participants receive an official **Iron Lady Certificate** upon successful completion of the program.",
    "mentors": "👩‍🏫 Our mentors include certified leadership coaches, industry professionals, and global thought leaders with decades of experience."
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
    elif "duration" in user_input or "long" in user_input or "time" in user_input:
        return FAQS["duration"]
    elif "online" in user_input or "offline" in user_input or "mode" in user_input:
        return FAQS["mode"]
    elif "certificate" in user_input or "certificates" in user_input:
        return FAQS["certificate"]
    elif "mentor" in user_input or "coach" in user_input or "trainer" in user_input:
        return FAQS["mentors"]

    # Fallback
    return random.choice([
        "Hmm 🤔 I’m not sure about that. Try asking about programs, duration, mode, certificates, or mentors.",
        "Currently, I can answer FAQs about Iron Lady’s leadership programs. 😊",
        "Could you ask me about programs, duration, mode, certificates, or mentors?"
    ])

# --- Streamlit UI ---
st.set_page_config(page_title="Iron Lady Chatbot", page_icon="👩‍💼", layout="centered")

# --- Sidebar Theme Selector ---
st.sidebar.title("🎨 Customize Theme")
theme = st.sidebar.radio(
    "Choose a theme:",
    ["Elegant Gradient", "Professional Dark Mode", "Iron Lady Brand Colors"]
)

# --- Apply Theme ---
if theme == "Elegant Gradient":
    st.markdown(
        """
        <style>
        .stApp { background: linear-gradient(135deg, #f9c5d1, #9796f0); font-family: 'Trebuchet MS', sans-serif; }
        .stTextInput>div>div>input { border: 2px solid #FF69B4; border-radius: 10px; }
        .chat-bubble { padding: 10px 15px; border-radius: 15px; margin: 8px 0; display: inline-block; max-width: 80%; font-size: 16px; }
        .user-bubble { background-color: #ffdae0; color: black; text-align: right; float: right; clear: both; }
        .bot-bubble { background-color: #e3e6ff; color: black; text-align: left; float: left; clear: both; }
        </style>
        """,
        unsafe_allow_html=True
    )
elif theme == "Professional Dark Mode":
    st.markdown(
        """
        <style>
        .stApp { background: #1e1e1e; color: #f5f5f5; font-family: 'Trebuchet MS', sans-serif; }
        .stTextInput>div>div>input { border: 2px solid #888; border-radius: 10px; background: #333; color: #fff; }
        .chat-bubble { padding: 10px 15px; border-radius: 15px; margin: 8px 0; display: inline-block; max-width: 80%; font-size: 16px; }
        .user-bubble { background-color: #444; color: white; text-align: right; float: right; clear: both; }
        .bot-bubble { background-color: #666; color: white; text-align: left; float: left; clear: both; }
        </style>
        """,
        unsafe_allow_html=True
    )
else:  # Iron Lady Brand Colors
    st.markdown(
        """
        <style>
        .stApp { background: #fff0f5; color: #d63384; font-family: 'Trebuchet MS', sans-serif; }
        .stTextInput>div>div>input { border: 2px solid #d63384; border-radius: 10px; }
        .chat-bubble { padding: 10px 15px; border-radius: 15px; margin: 8px 0; display: inline-block; max-width: 80%; font-size: 16px; }
        .user-bubble { background-color: #ffd6e8; color: black; text-align: right; float: right; clear: both; }
        .bot-bubble { background-color: #ffe6f2; color: black; text-align: left; float: left; clear: both; }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Header with branding ---
st.image("https://ironlady.in/wp-content/uploads/2022/03/logo.png", width=180)  # Iron Lady Logo
st.title("👩‍💼 Iron Lady FAQ Chatbot")
st.write("✨ Welcome! I’m the Iron Lady Assistant. Ask me about our leadership programs!")

# --- Chat handling ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("💬 Type your question:")

if user_input:
    answer = get_answer(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))

# --- Clear Chat Button ---
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.success("Chat cleared!")
    st.experimental_rerun()

# --- Display styled chat history ---
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div class='chat-bubble user-bubble'>🧑 {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot-bubble'>🤖 {msg}</div>", unsafe_allow_html=True)
