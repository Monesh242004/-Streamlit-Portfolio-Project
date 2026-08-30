import streamlit as st

st.set_page_config(page_title="Education | My Portfolio", page_icon="🎓", layout="wide")

st.title("🎓 Education")
st.write("Here's a summary of my academic background and qualifications.")

st.divider()

education_data = [
    {
        "level": "Bachelor's Degree",
        "institution": "Hindi Seva Mandals Shri Sant Gadge Baba College of Engineering, Bhusawal",
        "duration": "2022 - 2026",
        "details": "Bachelor of Technology / Science in Computer Science / IT, "
                    "with a focus on programming, data structures, and software development.",
        "score": "CGPA: 7.10 / 10"
    },
    {
        "level": "Higher Secondary (12th Grade)",
        "institution": "Bhusawal Arts, Science and P.O. Nahata College of Commerce, Bhusawal",
        "duration": "2020 - 2022",
        "details": "Completed Higher Secondary education with a focus on Science (PCM).",
        "score": "Percentage: 72.83%"
    },
    {
        "level": "Secondary School (10th Grade)",
        "institution": "St. Aloysius Convent High School, Bhusawal",
        "duration": "2019 - 2020",
        "details": "Completed Secondary School Education (SSC).",
        "score": "Percentage: 79.40%"
    },
]

for edu in education_data:
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader(edu["level"])
            st.write(f"**Institution:** {edu['institution']}")
            st.write(edu["details"])
        with col2:
            st.write(f"📅 {edu['duration']}")
            st.write(f"🏆 {edu['score']}")
    st.write("")

st.divider()

st.header("Certifications & Courses")

cert1, cert2, cert3 = st.columns(3)

with cert1:
    with st.container(border=True):
        st.markdown("**Python Programing**")
        st.caption("Issued by: Innomatics Research Lab")
        st.write("Year: 2026")

with cert2:
    with st.container(border=True):
        st.markdown("**Exploratory Data Analysis**")
        st.caption("Issued by: Futureskills Prime")
        st.write("Year: 2025")

with cert3:
    with st.container(border=True):
        st.markdown("**introduction to Quantum Computing**")
        st.caption("Issued by: NPTEL")
        st.write("Year: 2025")

st.divider()
