import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Upload IMG"):
    camera_image = st.file_uploader("Upload Here!")

if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)