import streamlit as st

# Title of the Streamlit app
st.title("Ultimate Checklist: 7 Reasons You Need a Website 🌐")

# Description
st.write(
    "This checklist will guide you through the essential reasons for having a website, "
    "along with actionable steps to make the most of each benefit. "
    "Check off each task as you complete it to ensure you're on the right track to maximizing your online potential!"
)

# Define the main reasons and their detailed substeps
checklist_data = {
    "1. Build Instant Credibility 🌟": [
        "Set up a professional domain that reflects your brand.",
        "Create a business email address using your domain.",
        "Include customer testimonials prominently on your homepage.",
        "Showcase case studies that highlight your success.",
        "Display industry certifications or awards.",
        "Add a press section with media coverage or mentions.",
        "Feature your team’s qualifications and experiences.",
        "Integrate social proof, like follower counts or user reviews.",
        "Ensure your website has a professional, polished design.",
        "Implement SSL certificates to secure your site and build trust."
    ],
    "2. Expand Your Reach 🌎": [
        "Optimize your website for local and global SEO.",
        "Research keywords relevant to your business and integrate them.",
        "Utilize social media platforms to promote your content.",
        "Create a blog to attract organic traffic.",
        "Use Google My Business to enhance local visibility.",
        "Run targeted ad campaigns on platforms like Facebook or Google.",
        "Collaborate with influencers to reach new audiences.",
        "Participate in online communities related to your industry.",
        "Utilize email marketing to reach out to subscribers.",
        "Analyze your website traffic to identify potential markets."
    ],
    "3. Showcase Your Expertise 🛍️": [
        "Develop a comprehensive portfolio or gallery of your work.",
        "Write informative blog posts that demonstrate your knowledge.",
        "Create video tutorials or webinars to share your expertise.",
        "Offer downloadable resources, like eBooks or guides.",
        "Engage in guest blogging on reputable sites within your niche.",
        "Create an FAQ section addressing common questions in your field.",
        "Include a detailed services page explaining your offerings.",
        "Highlight successful projects with before-and-after visuals.",
        "Host live Q&A sessions to interact with your audience.",
        "Participate in online forums and contribute valuable insights."
    ],
    "4. Stay Open 24/7 🕒": [
        "Ensure your website is mobile-friendly for all devices.",
        "Set up an online booking system for appointments.",
        "Implement a contact form for inquiries available at all times.",
        "Provide comprehensive FAQs to assist visitors at any hour.",
        "Use chatbots for instant customer support responses.",
        "Make your services available for online purchase.",
        "Feature a clear business hours display on your site.",
        "Integrate a calendar system for client bookings.",
        "Offer downloadable content that can be accessed anytime.",
        "Regularly update content to keep it fresh and relevant."
    ],
    "5. Convenience for Your Customers 💬": [
        "Simplify navigation with a clear and user-friendly menu.",
        "Add a live chat feature for immediate support.",
        "Ensure all contact information is easy to find.",
        "Include clear call-to-action buttons throughout the site.",
        "Create a customer feedback form to gather insights.",
        "Integrate social media sharing buttons for easy access.",
        "Offer multiple payment options for e-commerce.",
        "Create guides or videos explaining how to use your services.",
        "Optimize page load speed to enhance user experience.",
        "Make sure all links work correctly and lead to relevant pages."
    ],
    "6. Unlock Marketing Power 📈": [
        "Install Google Analytics to track website performance.",
        "Utilize heatmaps to understand user behavior on your site.",
        "Create landing pages for specific campaigns or promotions.",
        "Incorporate email sign-up forms for building your list.",
        "Run A/B tests to determine the most effective strategies.",
        "Use retargeting ads to bring back previous visitors.",
        "Leverage social media advertising to reach specific audiences.",
        "Analyze competitor websites to identify gaps in your strategy.",
        "Create promotional content that drives traffic to your site.",
        "Regularly review and adjust your marketing strategies based on data."
    ],
    "7. Stand Out from the Crowd 🏆": [
        "Develop a unique brand identity with a memorable logo.",
        "Create high-quality, original content that showcases your voice.",
        "Utilize color schemes and fonts that reflect your brand personality.",
        "Highlight your unique selling propositions on your homepage.",
        "Share success stories that differentiate you from competitors.",
        "Engage with your audience through polls or surveys.",
        "Use professional photography to enhance visual appeal.",
        "Participate in industry events to network and promote your brand.",
        "Regularly update your website to reflect current trends.",
        "Implement a loyalty program or special offers to retain customers."
    ]
}

# Render checklist for each reason with expanded substeps
for reason, steps in checklist_data.items():
    with st.expander(reason):
        for step in steps:
            st.checkbox(step)
