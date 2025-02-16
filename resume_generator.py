import streamlit as st
from fpdf import FPDF
from PIL import Image
import os

# Streamlit app styling
st.set_page_config(page_title="AI Resume Generator", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f9f9f9;
    }
    .header {
        text-align: center;
        font-size: 40px;
        color: #4CAF50;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subheader {
        color: #333;
        font-size: 20px;
        font-weight: bold;
    }
    .label {
        font-size: 16px;
        font-weight: bold;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.markdown('<div class="header">AI Resume Generator</div>', unsafe_allow_html=True)

# Layout for input form
with st.container():
    st.markdown('<div class="subheader">Fill in your details:</div>', unsafe_allow_html=True)
    name = st.text_input("Name", placeholder="Enter your full name")
    qualification = st.text_input("Qualification", placeholder="Enter your qualification")
    internships = st.text_area("Internships", placeholder="Describe your internships")
    projects = st.text_area("Projects", placeholder="Describe your projects")
    grants = st.text_area("Grants/Funds Received", placeholder="List grants or funds received")
    photo = st.file_uploader("Upload Passport Size Photo", type=["jpg", "png"])

# Generate Resume button
if st.button("Generate Resume"):
    if name and qualification:
        # Load default company logo
        company_logo = r"C:\Users\aditya\Desktop\sbhvsh\images.jpeg"

        # PDF customization
        pdf = FPDF()
        pdf.add_page()

        # Colors and Fonts
        pdf.set_text_color(0, 51, 102)  # Dark Blue
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="RESUME", ln=True, align="C")

        # Add border
        pdf.set_draw_color(0, 51, 102)  # Blue border
        pdf.rect(5, 5, 200, 287)

        # Add company logo
        pdf.image(company_logo, x=80, y=10, w=50)

        # Add user photo
        if photo:
            try:
                with open("temp_photo.jpg", "wb") as f:
                    f.write(photo.read())
                pdf.image("temp_photo.jpg", x=160, y=20, w=30)  # Add photo
            except Exception as e:
                st.error(f"Error processing photo: {e}")

        # Name and qualification
        pdf.ln(50)
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(200, 10, txt=f"Name: {name}", ln=True, align="L")
        pdf.cell(200, 10, txt=f"Qualification: {qualification}", ln=True, align="L")

        # Section Headers
        pdf.set_text_color(0, 51, 102)
        pdf.set_font("Arial", style="B", size=12)

        # Internships
        pdf.cell(200, 10, txt="Internships:", ln=True, align="L")
        pdf.set_font("Arial", size=11)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 10, internships)

        # Projects
        pdf.set_text_color(0, 51, 102)
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Projects:", ln=True, align="L")
        pdf.set_font("Arial", size=11)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 10, projects)

        # Grants/Funds
        pdf.set_text_color(0, 51, 102)
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Grants/Funds Received:", ln=True, align="L")
        pdf.set_font("Arial", size=11)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 10, grants)

        # Save and download PDF
        pdf.output("resume.pdf")
        st.success("Resume generated successfully!")
        with open("resume.pdf", "rb") as file:
            st.download_button("Download Resume", file, "resume.pdf")
    else:
        st.error("Please fill out all required fields.")
