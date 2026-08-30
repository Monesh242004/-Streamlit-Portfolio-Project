import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="👋",
    layout="wide"
)

#------------ HERO Section ---------------------
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image("https://i.pinimg.com/736x/b8/42/58/b842583b2176aace3eab9547d28d1239.jpg", width=200)

with col2:
    st.title("Hi, I'm Monesh Chaudhari 👋")
    st.subheader("Aspiring Data Analyst / Data Science Engineer")
    st.write(
        """
        Hello! I’m Monesh Chaudhari, a final-year B.Tech student passionate about Data Analyst and Data Science. I enjoy transforming raw data
        into meaningful insights through data analysis and visualization techniques. I have hands-on experience in Python, Exploratory Data Analysis 
        (EDA), Power BI, and data preprocessing. I am continuously improving my technical skills through projects and practical 
        learning experiences,with the goal of contributing to real-world data-driven solutions. 
        """
    )
    st.write("📍 Location: Pune, Maharashtra, India")

st.divider()

# ---------- ABOUT ME ----------
st.header("About Me")
st.write(
    """
    I am currently pursuing my studies with a strong interest in technology,
    programming, and data science. I love learning new tools and frameworks,
    and I enjoy working on projects that combine creativity with technical
    problem-solving.
    """
)

st.divider()

# ---------- SKILLS ----------
st.header("Skills")

skill_col1, skill_col2, skill_col3 = st.columns(3)

with skill_col1:
    st.markdown("### 💻 Programming")
    st.write("- Python")
    st.write("- EDA")
    st.write("- C")

with skill_col2:
    st.markdown("### 📊 Data & Tools")
    st.write("- Pandas, NumPy, EDA")
    st.write("- Streamlit")
    st.write("- Power BI / Excel")

with skill_col3:
    st.markdown("### 🌐 Other")
    st.write("- Git & GitHub")
    st.write("- HTML/CSS")
    st.write("- Problem Solving")

st.divider()

# ---------- PROJECTS ----------
st.header("Featured Projects")

proj1, proj2 = st.columns(2)

with proj1:
    with st.container(border=True):
        st.subheader("📈 IMDb Movie Sales Dashboard")
        st.write(
            "An interactive dashboard built with Streamlit to visualize "
            "sales trends, KPIs, and regional performance."
        )
        st.write("**Tech:** PowerBi, DAX, Power Query Formula ")

with proj2:
    with st.container(border=True):
        st.subheader("📱 QR Code Generator")
        st.write(
            "A web application that generates customized QR codes for "
            "text, URLs, contact details, and other information instantly."
        )
        st.write("**Tech:** Python, qrcode, Pillow")

st.divider()
