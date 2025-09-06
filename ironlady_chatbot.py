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
    else:
        return random.choice([
            "Hmm, I’m not sure about that. Can you rephrase?",
            "Interesting question! Could you ask in another way?",
            "I’ll get back to you on that—currently I can answer about programs, duration, mode, certificates, or mentors."
        ])

# --- Streamlit UI ---
st.set_page_config(page_title="Iron Lady Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Iron Lady FAQ Chatbot")
st.write("Hello! I’m the Iron Lady Assistant. Ask me about our leadership programs ✨")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💬 Ask your question:")

if user_input:
    answer = get_answer(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
