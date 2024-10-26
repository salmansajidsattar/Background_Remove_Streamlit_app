import streamlit as st
from rembg import remove
from PIL import Image
import io

# Set up the Streamlit app
st.title("Background Removal App")
st.write("Upload an image to remove its background using rembg.")

# File uploader to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image
    input_image = Image.open(uploaded_file)
    
    # Process the image with rembg to remove the background
    input_bytes = io.BytesIO()
    input_image.save(input_bytes, format="PNG")
    output_bytes = remove(input_bytes.getvalue())
    output_image = Image.open(io.BytesIO(output_bytes))
    
    # Display the processed image with background removed
    st.subheader("Image with Background Removed")
    st.image(output_image)
else:
    st.info("Please upload an image file.")
