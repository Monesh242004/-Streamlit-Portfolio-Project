import streamlit as st

st.set_page_config(page_title="Contact Us | My Portfolio", page_icon="📩", layout="wide")

st.title("📩 Contact Us")
st.write("I'd love to hear from you! Fill out the form below or reach me directly through the links provided.")

st.divider()

left_col, right_col = st.columns([1.3, 1], gap="large")

with left_col:
    st.subheader("Send me a message")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name *")
        email = st.text_input("Your Email *")
        subject = st.text_input("Subject")
        message = st.text_area("Message *", height=150)

        submitted = st.form_submit_button("Send Message")

        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all required fields marked with *.")
            else:
                st.success(f"Thank you, {name}! Your message has been received. "
                            "I'll get back to you soon at " + email)

with right_col:
    st.subheader("Get in touch")

    st.markdown("📍 **Location:** Pune, Maharashtra, India")
    st.markdown("📧 **Email:** [monesh2004chaudhari@gmail.com]")
    st.markdown("📱 **Phone:** +91-8390915522")

    st.write("")
    st.markdown("🔗 **Connect with me:**")
    st.markdown("- [LinkedIn](https://www.linkedin.com/in/monesh-chaudhari-4a9732377/)")
    st.markdown("- [GitHub](https://github.com/Monesh242004)")
   

    st.write("")
    with st.container(border=True):
        st.markdown("**Availability**")
        st.write("Open to internships, freelance projects, and collaboration opportunities.")

st.divider()
