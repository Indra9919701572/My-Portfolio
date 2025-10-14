import streamlit as st
from PIL import Image

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="My Portfolio", page_icon="🎯", layout="wide")

# ------------------------------
# HEADER SECTION
# ------------------------------
st.title("👋 Welcome to My Portfolio Website")
st.write("Created with ❤️ using Streamlit")

# Add a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Skills", "Projects", "Certifications", "Contact"])

# ------------------------------
# HOME SECTION
# ------------------------------
if page == "Home":
    st.header("🏠 Home")
    col1, col2 = st.columns([1, 2])

    with col1:
        # Replace with your image path
        image = Image.open("resume pic.jpg")   # <-- put your photo in the same folder
        st.image(image, width=250)

    with col2:
        st.subheader("Hello! I'm Indra Kumar Prajapati")
        st.write("""
        🎓 I'm a passionate **Data Science / Machine Learning / Web Development** enthusiast.  
        💡 I love building intelligent systems and data-driven applications.  
        🌱 I’m constantly learning new tools and technologies to improve my skills.
        """)

        st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")  # <-- replace with your YouTube link

# ------------------------------
# SKILLS SECTION
# ------------------------------
elif page == "Skills":
    st.header("💼 Skills")
    st.write("""
    - **Programming Languages:** Python, C++, Java  
    - **Web Development:** HTML, CSS, JavaScript, Streamlit, Flask  
    - **Data Science & ML:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn  
    - **Databases:** MySQL, MongoDB  
    - **Tools:** Git, VS Code, Jupyter Notebook  
    """)

# ------------------------------
# PROJECTS SECTION
# ------------------------------
elif page == "Projects":
    st.header("🚀 Projects")
    st.write("""
    ### 📊 Customer Churn Prediction
    - **Description:** Predicted whether a customer will leave the company using logistic regression.  
    - **Tech Stack:** Python, Pandas, Scikit-learn, Matplotlib  
    - **GitHub:** [View Project](https://github.com/yourusername/yourproject)

    ### 🤖 Movie Recommendation System
    - **Description:** Suggested movies based on user preferences using content-based filtering.  
    - **Tech Stack:** Python, Streamlit, NLP  
    - **GitHub:** [View Project](https://github.com/yourusername/yourproject2)
    """)

# ------------------------------
# CERTIFICATIONS / ACHIEVEMENTS
# ------------------------------
elif page == "Certifications":
    st.header("🏅 Certifications & Achievements")
    st.write("""
    - 🧠 **Machine Learning with Python** – Coursera  
    - 🌐 **Web Development Bootcamp** – Udemy  
    - 🥇 **Top Performer in Data Science Hackathon**  
    - 📜 **Python for Data Analysis** – Kaggle  
    """)

# ------------------------------
# CONTACT SECTION
# ------------------------------
elif page == "Contact":
    st.header("📞 Contact Me")

    st.write("Feel free to reach out for collaboration or any queries!")

    contact_form = """
    <form action="https://formsubmit.co/YOUR_EMAIL" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    st.write("📧 Email: 9919indrakumar@gmail.com")
    st.write("🌐 LinkedIn: [linkedin.com/in/indra-prajapati-1099888280](https://linkedin.com/in/indra-prajapati-1099888280)")
    st.write("💻 GitHub: [github.com/Indra9919701572](https://github.com/Indra9919701572)")

# ------------------------------
# CUSTOM CSS
# ------------------------------
st.markdown("""
<style>
    form input, form textarea {width: 100%; padding: 10px; margin: 5px 0; border-radius: 10px; border: 1px solid #ccc;}
    form button {background-color: #0078ff; color: white; border: none; padding: 10px 20px; border-radius: 10px;}
    form button:hover {background-color: #005fcc;}
</style>
""", unsafe_allow_html=True)

