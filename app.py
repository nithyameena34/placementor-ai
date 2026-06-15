
import streamlit as st
from chatbot import get_gemini_response
from database import save_message, get_messages

# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="PlaceMentor AI",
    page_icon="🤖",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

/* Main App */
.stApp {
    transition: 0.3s;
}

/* Headings */
h1, h2, h3 {
    color: #00ADB5 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: rgba(20, 20, 20, 0.05);
}

/* Buttons */
div.stButton > button {
    background-color: #00ADB5;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
}

div.stButton > button:hover {
    background-color: #008C9E;
    color: white;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
}

/* Metrics */
[data-testid="metric-container"] {
    border-radius: 10px;
    padding: 15px;
}

/* Inputs */
textarea, input {
    border-radius: 10px !important;
}

/* Remove forced white text */
html, body, [class*="css"] {
    color: inherit !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🤖 PlaceMentor AI")

st.sidebar.markdown("""
### AI Placement Assistant

Prepare for:
- Technical Interviews
- Aptitude
- HR Interviews
- Resume Building
- Career Guidance
""")

page = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Technical Prep",
        "Aptitude",
        "HR Interview",
        "Resume Tips",
        "Career Guidance"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Built using Python + Streamlit + Groq AI")

# =========================
# HOME PAGE
# =========================
if page == "Home":

    st.title("🤖 PlaceMentor AI")
    st.subheader("AI-Powered Placement Preparation Chatbot")

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AI Model", "Llama 3")

    with col2:
        st.metric("Modules", "6")

    with col3:
        st.metric("Platform", "Streamlit")

    st.markdown("---")

    # =========================
    # LOAD CHAT HISTORY
    # =========================
    if "messages" not in st.session_state:

        st.session_state.messages = []

        previous_messages = get_messages()

        for role, message in previous_messages:

            st.session_state.messages.append({
                "role": role,
                "content": message
            })

    # =========================
    # DISPLAY CHAT HISTORY
    # =========================
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # =========================
    # USER INPUT
    # =========================
    user_input = st.chat_input(
        "Ask your placement question..."
    )

    if user_input:

        # Save User Message in Session
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Save User Message in Database
        save_message("user", user_input)

        # Display User Message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate AI Response
        with st.spinner("Generating AI response..."):

            ai_response = get_gemini_response(user_input)

        # Save AI Response in Session
        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_response
        })

        # Save AI Response in Database
        save_message("assistant", ai_response)

        # Display AI Response
        with st.chat_message("assistant"):
            st.markdown(ai_response)

# =========================
# TECHNICAL PREP
# =========================
elif page == "Technical Prep":

    st.title("💻 Technical Interview Preparation")

    topic = st.selectbox(
        "Select Topic",
        [
            "Python",
            "Java",
            "DBMS",
            "Operating Systems",
            "Computer Networks",
            "OOPs",
            "Data Structures"
        ]
    )

    difficulty = st.selectbox(
        "Select Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("Generate Questions"):

        prompt = f"""
        Generate 5 {difficulty} level interview questions
        for {topic}.

        Also provide short answers.
        """

        with st.spinner("Generating Questions..."):

            response = get_gemini_response(prompt)

        st.markdown(response)

# =========================
# APTITUDE PAGE
# =========================
elif page == "Aptitude":

    st.title("🧠 Aptitude Preparation")

    category = st.selectbox(
        "Select Aptitude Category",
        [
            "Quantitative Aptitude",
            "Logical Reasoning",
            "Verbal Ability"
        ]
    )

    difficulty = st.selectbox(
        "Select Difficulty Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("Generate Aptitude Questions"):

        prompt = f"""
        Generate 5 {difficulty} level aptitude questions
        for {category}.

        Also provide:
        - Correct answers
        - Short explanations
        """

        with st.spinner("Generating Questions..."):

            response = get_gemini_response(prompt)

        st.markdown(response)

# =========================
# HR INTERVIEW PAGE
# =========================
elif page == "HR Interview":

    st.title("🗣️ HR Interview Preparation")

    hr_topic = st.selectbox(
        "Select HR Topic",
        [
            "Tell Me About Yourself",
            "Strengths and Weaknesses",
            "Why Should We Hire You?",
            "Leadership",
            "Teamwork",
            "Conflict Management",
            "Career Goals"
        ]
    )

    if st.button("Generate HR Questions & Answers"):

        prompt = f"""
        Generate HR interview questions and professional answers
        for the topic: {hr_topic}.

        Also provide:
        - Communication tips
        - Confidence tips
        - Common mistakes to avoid
        """

        with st.spinner("Generating HR Content..."):

            response = get_gemini_response(prompt)

        st.markdown(response)

# =========================
# RESUME ANALYZER
# =========================
elif page == "Resume Tips":

    st.title("📄 AI Resume Analyzer")

    st.write(
        "Paste your resume content below for AI analysis."
    )

    resume_text = st.text_area(
        "Paste Resume Content",
        height=300
    )

    if st.button("Analyze Resume"):

        prompt = f"""
        Analyze the following resume.

        Provide:
        - Resume strengths
        - Resume weaknesses
        - Missing skills
        - ATS improvement tips
        - Project suggestions
        - Career improvement suggestions

        Resume:
        {resume_text}
        """

        with st.spinner("Analyzing Resume..."):

            response = get_gemini_response(prompt)

        st.markdown(response)

# =========================
# CAREER GUIDANCE
# =========================
elif page == "Career Guidance":

    st.title("🚀 Career Guidance")

    career = st.selectbox(
        "Select Career Domain",
        [
            "Software Development",
            "Data Science",
            "Artificial Intelligence",
            "Web Development",
            "Cybersecurity",
            "Cloud Computing",
            "UI/UX Design"
        ]
    )

    if st.button("Get Career Guidance"):

        prompt = f"""
        Provide complete career guidance for {career}.

        Include:
        - Required skills
        - Learning roadmap
        - Recommended technologies
        - Certifications
        - Project ideas
        - Future scope
        - Placement preparation tips
        """

        with st.spinner("Generating Career Guidance..."):

            response = get_gemini_response(prompt)

        st.markdown(response)

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown(
    "© 2026 PlaceMentor AI | Built with Python, Streamlit & Groq"
)
