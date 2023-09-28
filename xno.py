from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon="images/xnor.jpeg", layout="wide")

# ----LOAD ASSETS ---
img_contact_form = Image.open("images/xnor.jpeg")
# ----HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Othniel :wave:")
    st.title("An Electrical Engineer in Nairobi")
    st.write("I am passionate about offering world class Electrial design solutions to people I relate with")
    st.write("Welcome here to get my contacts for Electrical services as well as shop for ambient lighting acessories")




# -- WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On this webstore, please scroll to get price list of all Electrical equipments. 
            You can also connect with us on our social platforms:
            -Instagram
            -Facebook
            -Tiktok
            -Twitter
            from the links below and icons.
            """
        )
        st.write("[Instagram >] (https://www.instagram.com/)")

# --- PROJECTS ---
with st.container():
    st.write("---")
    st.header("Company")
    st.write("##")
    image_column, text_column = st.columns((1,1))
        #insert image
    st.image(img_contact_form)

# ---CONTACT---
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

# ---FORM ---
contact_form = """
<form action="https://formsubmit.co/ssamsanya3@gmail.com" method="POST">
     <input type="hidden" name"_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

