import cv2
import numpy as np
from PIL import Image
import streamlit as st


st.title("Image Blur App")



uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.success("Succussfully uploaded")



# pre process
    image = Image.open(uploaded_file)
    st.image(image, "input")
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# process
    blur_amount = st.slider("میزان مات شدن", min_value=1, max_value=199, value=51, step=2)
    result_image = cv2.blur(image, (blur_amount, blur_amount))


# post process
    result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    result_image = Image.fromarray(result_image)
    st.image(result_image, "out put")
else:
    st.info("nothing uploaded")

