import streamlit as st

# Title of the Streamlit app
st.title("Checklist: 7 Reasons You Need a Website 🌐")

# Description
st.write("This checklist will guide you through the essential reasons for having a website, "
         "along with actionable steps to make the most of each benefit. Check off each task as you complete it!")

# Define the main reasons and their substeps
checklist_data = {
    "1. Build Instant Credibility 🌟": [
        "Set up a professional domain and email address.",
        "Include testimonials or case studies.",
        "Showcase credentials, awards, or partnerships."
    ],
    "2. Expand Your Reach 🌎": [
        "Optimize for SEO to rank higher in search results.",
        "Connect with social media to drive traffic.",
        "Target new customer demographics."
    ],
    "3. Showcase Your Expertise 🛍️": [
        "Create a portfolio or gallery of work.",
        "Write blog posts or articles on your niche.",
        "Add an 'About Us' section to highlight experience."
    ],
    "4. Stay Open 24/7 🕒": [
        "Ensure mobile compatibility for ease of access.",
        "Add contact forms for inquiries any time.",
        "Set up automated responses or chatbots."
    ],
    "5. Convenience for Your Customers 💬": [
        "Implement online booking or ordering.",
        "Add a FAQ section to answer common questions.",
        "Provide clear contact info and location details."
    ],
    "6. Unlock Marketing Power 📈": [
        "Install analytics to track visitor data.",
        "Set up email subscription forms.",
        "Run online promotions and offers."
    ],
    "7. Stand Out from the Crowd 🏆": [
        "Design a unique, branded visual identity.",
        "Highlight what makes your business different.",
        "Share success stories or client feedback."
    ]
}

# Render checklist for each reason
for reason, steps in checklist_data.items():
    with st.expander(reason):
        for step in steps:
            st.checkbox(step)
