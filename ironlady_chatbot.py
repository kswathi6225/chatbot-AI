import streamlit as st
import openai

# --- Configure OpenAI ---
openai.api_key = st.secrets["OPENAI_API_KEY"]  # store key safely in Streamlit Cloud

# --- FAQ Database (still keep for reference / fallback) ---
FAQS = {
    "programs": "🌟 Iron Lady offers:\n- Leadership Development Programs\n- Confidence Building Workshops\n- Career Acceleration Programs\n- Executive Coaching Sessions",
    "duration": "⏳ Program durations vary:\n- Short workshops: 2–3 days\n- Core programs: 6–8 weeks\n- Advanced leadership journeys: 3 months",
    "mode": "💻 All programs are conducted **online** via live interactive sessions with mentors and peers.",
    "certificate": "🎓 Yes! Participants receive an official **Iron Lady Certificate** upon successful completion of the program.",
    "mentors": "👩‍🏫 Our mentors include certified leadership coaches, industry professionals, and global thought leaders with decades of experience."
}

# --- Helper: AI-powered answer ---
def get_ai_answer(user_input):
    try:
        prompt = f"""
        You are Iron Lady’s official assistant chatbot. 
        Answer user questions in a friendly and engaging way. 
        Use the following FAQ details if relevant:

        {FAQS}

        User asked: {user_input}
        """

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "You are a helpful FAQ assistant for Iron Lady."},
                      {"role": "user", "content": prompt}]
        )

        return response.choices[0].message["content"]

    except Exception as e:
        return f"⚠️ Sorry, I couldn’t connect to AI service. ({e})"

# --- Streamlit UI ---
st.set_page_config(page_title="Iron Lady Chatbot", page_icon="👩‍💼", layout="centered")
st.title("👩‍💼 Iron Lady FAQ Chatbot")
st.write("✨ Welcome! I’m the Iron Lady Assistant. Ask me about our leadership programs!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💬 Type your question:")

if user_input:
    answer = get_ai_answer(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))

# --- Clear Chat ---
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()

# --- Show chat ---
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div style='background:#ffdae0;padding:8px;border-radius:10px;text-align:right'>🧑 {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background:#e3e6ff;padding:8px;border-radius:10px;text-align:left'>🤖 {msg}</div>", unsafe_allow_html=True)
