import streamlit as st
import speech_recognition as sr
import pyttsx3
from reportlab.pdfgen import canvas
import tempfile
import os

# Initialize recognizer
r = sr.Recognizer()

# Function to convert speech to text
def recognize_speech():
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        r.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for noise
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, could not understand the audio."
    except sr.RequestError:
        return "Error: Could not request results from Google Speech Recognition."

# Function to generate PDF
def generate_pdf(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        pdf_path = temp_file.name

    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Voice-to-Text Transcript")
    c.drawString(100, 730, "---------------------------")

    y_position = 710
    for line in text.split("\n"):
        c.drawString(100, y_position, line)
        y_position -= 20

    c.save()
    return pdf_path  # Return the actual file path

# Streamlit UI
st.title("🗣️ Speech-to-Text & PDF Generator")
st.write("Click the button below, speak, and download your transcript as a PDF.")

# Initialize session state for storing text
if "text_output" not in st.session_state:
    st.session_state["text_output"] = ""

# Button to start recording
if st.button("🎤 Start Recording"):
    text_output = recognize_speech()
    st.session_state["text_output"] = text_output

# Display the transcribed text
st.text_area("Transcribed Text:", st.session_state["text_output"], height=150)

# Generate and provide PDF download link
if st.session_state["text_output"]:
    if st.button("📄 Generate PDF"):
        pdf_path = generate_pdf(st.session_state["text_output"])

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download PDF",
                data=f,
                file_name="transcription.pdf",
                mime="application/pdf",
            )

        os.remove(pdf_path)  # Delete after ensuring it's available
