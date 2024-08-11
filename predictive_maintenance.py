import streamlit as st
from PIL import Image

# Set the page title and layout
st.set_page_config(page_title="Synthetic Image Generation", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: orange;'>Synthetic Image Generation</h1>", unsafe_allow_html=True)

# Dropdown menus for selecting asset and defect
asset = st.selectbox("Select an asset", ["Pipeline", "Tank", "Pump", "Valve"])
defect = st.selectbox("Select a defect", ["Rust", "Crack", "Leak", "Dirt"])

# Text input for the prompt
prompt = st.text_input("Prompt", "Heavy rust, corrosion, weathered, damaged, old, abandoned")

# Displaying images
col1, col2 = st.columns(2)

with col1:
    st.write("Original Image")
    image = Image.open("original_image.png")  # Replace with your original image file path
    st.image(image, caption="Original Image", use_column_width=True)

with col2:
    st.write("Synthetic Image")
    synthetic_image = Image.open("synthetic_image.png")  # Replace with your synthetic image file path
    st.image(synthetic_image, caption="Synthetic Image", use_column_width=True)

# Generate button
if st.button("Generate"):
    st.write("Generating synthetic image...")

# Display the output of image generation process
# Here you would typically display the result of the synthetic image generation
