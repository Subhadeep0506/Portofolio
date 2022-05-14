import json
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Subhadeep Mandal", page_icon=":tada:", layout="wide")

# Hiding the footer with markdown
hide_streamlit_style = """
            <style>
            #MainMenu {
                visibility: hidden;
            }
            footer {
                visibility: hidden;
                background: #67676733;
                color: #000000;
                height: 6rem;
            }
            .css-fk4es0 e8zbici1 {
                height: 1rem;
            }
            
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Function to load lottie animation using url
def load_lottie_url(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()


# USe local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Assets url
lottie_anim = load_lottie_url(
    "https://assets1.lottiefiles.com/private_files/lf30_WdTEui.json"
)
image_file = Image.open("images/user.jpeg")

# Header Section
with st.container():
    image, details = st.columns((1, 3))
    with image:
        st.image(image=image_file)

    with details:
        st.markdown("# Hello! I am Subhadeep :wave:")

        st.markdown("## Student. Flutter Developer. Machine Learing Enthusiast.")
        st.markdown(
            "##### A Machine Learning enthusiast and Mobile app Developer, with a background in Computer Science Engineering. I am currently pursuing my Bachelors in Technology from Haldia Institute of Technology, Haldia, India. My work interests include Mobile App Development, Mobile Game Development and Machine Learing."
        )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - I am an Undergraduate Computer Science student at Haldia Institute of Technology
            - I Love building apps with Flutter
            - I am currently learning to make Full Stack MERN applications
            - Also, I am exploring Machine Learning as well
            """
        )
        st.write(
            "Connect with me through [LinkedIn](https://www.linkedin.com/in/subhadeepmandal2000/)."
        )

    with right_column:
        with open("images/lottie_anim.json", "r") as f:
            data = json.load(f)
        st_lottie(data, height=400, key="coding")

with st.container():
    st.write("---")
    st.header("My Experiences")
    st.write("##")
    project_column, work_column = st.columns(2)

    with project_column:
        st.header("Projects")
        st.write("---")
        st.subheader("Peek-A-Geek")
        st.write(
            """
            - A Full Stack MERN application, for developers to connect with each other
            - Users can view others' profile and projects on Github
            - Share ideas and projects and, communicate through posts
            - Includes new user registration, e-mail confirmation and profile updation and deletion
            """
        )
        st.write(
            "Visit repository on [Github](https://github.com/Subhadeep0506/Peek-A-Geek)"
        )

        st.subheader("E-Commerce RESTful API")
        st.write(
            """
            - Built a Flask RESTful API for E-Commerce site. 
            - Features registration and logging in for users alongwith deleting users, adding and deleting stores and items.
            - Also includes user confirmation through e-mail, payment using Stripe and database migration.
            """
        )
        st.write(
            "Visit repository on [Github](https://github.com/Subhadeep0506/ECommerce-Store-REST-API)"
        )

        st.subheader("Test Application")
        st.write(
            """
            - Built a test taking application using Flutter
            - Questions are viewed as slidable pages. Only MCQs
            - Views time remaining and results (after submission)
            """
        )
        st.write(
            "Visit repository on [Github](https://github.com/Subhadeep0506/test-application)"
        )

    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader(
            "Visit my [Github](https://github.com/Subhadeep0506) profile to find more projects"
        )
    with right_column:
        st.subheader(
            "Download my [Resume](https://github.com/Subhadeep0506/Subhadeep0506/raw/main/Subhadeep's%20Resume.pdf)"
        )

    with work_column:
        st.header("Internships")
        st.write("___")
        st.subheader("IIT Bombay")
        st.write(
            """
            - Flutter Developer Intern
            - 03-01-2022 to 04-07-2022
            - Worked on a Fashion app that suggests outfit combination for different occation
            - I started as a beginner flutter developer with basic knowledge. With this internship, my flutter experience has improved a lot
            """
        )

        st.subheader("The Sparks Foundation")
        st.write(
            """
            - Mobile Developer Intern
            - 01-07-2021 to 01-08-2021
            - Built a basic banking app and a Social media integration app using Java and Android SDK
            """
        )

with st.container():
    st.write("---")
    st.header("My Education")
    st.write("##")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("College")
        st.write("---")
        st.subheader("Haldia Institute of Technology")
        st.write(
            """
            - Btech in Computer Science and Engineering
            - Batch of 2023
            - CGPA (as of 5th semester): 9.25
            """
        )

    with right_column:
        st.header("Schools")
        st.write("---")
        st.subheader("De Paul School, Visakhapatnam")
        st.write(
            """
            - Secondary Education
            - Batch of 2017
            - Percentage: 91.8%
            """
        )

        st.subheader("Sri Chaitanya Educational Institution, Visakhapatnam")
        st.write(
            """
            - Higher Secondary Education
            - Batch of 2019
            - Percentage: 85.6%
            """
        )

with st.container():
    st.write("---")
    st.header("Contact Me")

    contact_form = """
        <form action="https://formsubmit.co/myself.subhadeepmandal@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="your e-mail" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
    """

    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.empty()
