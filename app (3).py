# app.py
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="International Business Marketing Prompt App",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 International Business Marketing Prompt Application")

st.write("""
This application generates professional international marketing content 
using Generative AI-style prompt engineering techniques.
""")

# User Input
product_name = st.text_input("Enter Product Name")

# Generate Button
if st.button("Generate Marketing Content"):

    if product_name.strip() == "":
        st.warning("Please enter a product name.")
    else:

        # 1. Global Product Title
        global_title = f"GlobalX {product_name} Pro"

        # 2. Marketing Slogan
        slogan = f"Experience the Future of {product_name} Worldwide!"

        # 3. Advertising Descriptions
        expert1 = f"""
### 🌟 Expert Perspective 1 – Brand Strategist
{product_name} is designed to redefine modern lifestyles with innovation, 
quality, and global appeal. Built for international markets, it delivers 
premium performance while maintaining customer trust and brand excellence.
"""

        expert2 = f"""
### 📈 Expert Perspective 2 – Digital Marketing Specialist
Promote your business globally with {product_name}, a smart and reliable 
solution crafted for today’s fast-moving digital world. Its user-friendly 
features and advanced capabilities make it ideal for worldwide consumers.
"""

        expert3 = f"""
### 💡 Expert Perspective 3 – Consumer Psychology Expert
{product_name} creates emotional engagement through comfort, convenience, 
and innovation. Customers across cultures can connect with its value, 
making it a strong product for international branding and long-term loyalty.
"""

        # Display Results
        st.success("Marketing Content Generated Successfully!")

        st.subheader("1️⃣ Global-Ready Product Title")
        st.write(global_title)

        st.subheader("2️⃣ Powerful Marketing Slogan")
        st.write(slogan)

        st.subheader("3️⃣ Product Advertising Descriptions")
        st.markdown(expert1)
        st.markdown(expert2)
        st.markdown(expert3)

        # AI Prompt Template
        st.subheader("🧠 Prompt Engineering Template")

        prompt = f"""
Generate international business marketing content for the product: {product_name}

Requirements:
1. Create a professional global-ready product title.
2. Generate a powerful and memorable marketing slogan.
3. Write three advertising descriptions from:
   - Brand Strategist Perspective
   - Digital Marketing Specialist Perspective
   - Consumer Psychology Expert Perspective

Ensure:
- International marketing standards
- Emotional engagement
- Persuasive branding
- Global audience compatibility
"""

        st.code(prompt, language="text")
