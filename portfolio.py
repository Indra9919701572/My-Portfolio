import streamlit as st
from pathlib import Path
import smtplib
from email.message import EmailMessage

# ---------------------------
# PAGE CONFIGURATION
# ---------------------------
st.set_page_config(page_title="Indra Prajapati | Data Science Portfolio", page_icon="💼", layout="wide")

# ---------------------------
# HEADER SECTION
# ---------------------------
st.title("💼 Data Science Portfolio")
st.write("### 👋 Hi, I'm **Indra Prajapati**, a Data Science and Machine Learning Enthusiast.")
st.write("""
I’m passionate about turning data into actionable insights and intelligent systems.  
Currently pursuing **BCA (Data Science specialization)** and building projects using **Machine Learning, Python, and Streamlit**.
""")

# ---------------------------
# PHOTO & INTRO VIDEO
# ---------------------------
col1, col2 = st.columns(2)
with col1:
    st.image("assets/myphoto.jpg", width=250, caption="Indra Prajapati")
with col2:
    st.subheader("🎥 My Introduction Video")
    st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_LINK")  # replace with your video link

# ---------------------------
# RESUME DOWNLOAD SECTION
# ---------------------------
st.markdown("---")
st.header("📄 Resume")
with open("assets/resume.pdf", "rb") as file:
    btn = st.download_button(
        label="⬇️ Download My Resume",
        data=file,
        file_name="Indra_Prajapati_Resume.pdf",
        mime="application/pdf"
    )

# ---------------------------
# SKILLS SECTION
# ---------------------------
st.markdown("---")
st.header("🧠 Skills")
skills = {
    "Programming": "Python, SQL, HTML, CSS, JavaScript",
    "Data Science": "Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn",
    "Machine Learning": "Regression, Classification, Clustering, Model Evaluation",
    "Other Tools": "Git, Streamlit, Power BI, Excel, VS Code"
}
for k, v in skills.items():
    st.write(f"**{k}:** {v}")

# ---------------------------
# PROJECTS SECTION
# ---------------------------
st.markdown("---")
st.header("🚀 Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Credit Scoring Model")
    st.write("""
    Predicts customer creditworthiness using financial data.  
    Algorithms used: Logistic Regression, Random Forest.  
    """)
    st.markdown("[🔗 View on GitHub](https://github.com/yourusername/credit-scoring-model)")

with col2:
    st.subheader("Customer Churn Prediction")
    st.write("""
    Predicts which customers are likely to stop using a service using classification models.  
    """)
    st.markdown("[🔗 View on GitHub](https://github.com/yourusername/churn-prediction)")

st.write("")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Movie Recommendation System")
    st.write("Built a recommendation system using cosine similarity and content-based filtering.")
    st.markdown("[🔗 View on GitHub](https://github.com/yourusername/movie-recommendation)")

with col4:
    st.subheader("Data Visualization Dashboard")
    st.write("Created interactive dashboards using Streamlit and Plotly.")
    st.markdown("[🔗 View on GitHub](https://github.com/yourusername/data-dashboard)")

# ---------------------------
# CERTIFICATIONS SECTION
# ---------------------------
st.markdown("---")
st.header("🏅 Certifications & Achievements")
st.write("""
- **Machine Learning Internship** — CodeAlpha  
- **Python for Data Science** — Coursera  
- **Data Analytics Certificate** — Kaggle  
- **Streamlit App Development** — Self Project
""")

# ---------------------------
# CONTACT FORM SECTION
# ---------------------------
st.markdown("---")
st.header("📬 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send Message")

    if submit:
        if name and email and message:
            # Email sending setup (use your own SMTP credentials)
            sender_email = "your_email@gmail.com"
            sender_password = "YOUR_APP_PASSWORD"  # use App Password (not main password)
            receiver_email = "your_email@gmail.com"

            msg = EmailMessage()
            msg.set_content(f"New message from {name} ({email}):\n\n{message}")
            msg["Subject"] = "New Portfolio Message"
            msg["From"] = sender_email
            msg["To"] = receiver_email

            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(sender_email, sender_password)
                    smtp.send_message(msg)
                st.success("✅ Message sent successfully! Thank you for reaching out.")
            except Exception as e:
                st.error(f"❌ Error sending message: {e}")
        else:
            st.warning("Please fill out all fields before submitting.")

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.write("Made with ❤️ by **Indra Prajapati** using [Streamlit](https://streamlit.io)")
