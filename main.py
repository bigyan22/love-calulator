import streamlit as st
import random
st.set_page_config(page_title="Love Calculator", layout='centered')
col1, col2, col3 = st.columns(3)
st.markdown(
    """
    <h1 style="text-align: center; color: #FF1493;">Love Calculator💖</h1>
    """, 
    unsafe_allow_html=True
)

st.markdown('')
st.markdown('')
pickup_lines = [
    "Do you believe in fate? Because I think we were meant to meet right here, right now.",
    "Are you a magician? Because you just turned my world upside down.",
    "Are you gravity? Because I’m so attracted to you, I can’t stay away.",
    "Do you believe in love at first sight, or should I make eye contact again?",
    "Are you a bank loan? Because you’ve got my interest at 100%.",
    "If beauty were a crime, you’d definitely be serving a life sentence.",
    "Is your aura made of stars? Because you light up every room you walk into.",
    "Are you an adventurer? Because I want to explore life with you by my side.",
    "Do you have a mirror in your pocket? Because I can see myself in your future.",
    "If kisses were snowflakes, I’d give you a blizzard.",
    "Are you the ocean? Because I’m lost in your depths.",
    "Are you my phone charger? Because you’re the one who powers me up.",
    "Are you an eclipse? Because you’ve blocked out everyone else from my sight.",
    "Is your smile Wi-Fi enabled? Because it’s connecting straight to my heart.",
    "Are you sunlight? Because you make my world brighter every time I see you.",
    "Do you have a spellbook? Because you’ve bewitched me completely.",
    "Is your name Melody? Because you’re the song I’ve been searching for.",
    "Are you a cupcake? Because you’re sweet, irresistible, and perfect.",
    "If I were to write a story, it’d start with 'Once upon a time, I met you.'",
    "Are you an artist? Because you just painted a permanent smile on my face."
]

def generate_circle_html(percentage):
    circle_html = f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
        <div style="
            position: relative;
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: conic-gradient(
                red {percentage}%,
                lightgray {percentage}% 100%
            );
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
            color: black;
            font-weight: bold;
        ">
            {percentage}%
        </div>
    </div>
    """
    return circle_html


def love_calc(own_name, partner_name):
    combined_name = own_name+partner_name
    score = sum(ord(ch) for ch in combined_name) % 101
    return score

col1, col2 = st.columns(2)
with col1:
    name = st.text_input('Your Name:')
    ur_gender = st.radio('Gender', options=['Male', 'Female'], index=0)

with col2:
    partner_name = st.text_input("Beloved one's Name:")
    if ur_gender == "Male":
        partner_gender = 'Female'
    else:
        partner_gender = "Male"
    
    st.write(f"Partner Gender: {partner_gender}")
col1, col2, col3 = st.columns(3)
successs = False
with col2:
    if st.button('Calculate Love💘'):
        if not name and not partner_name:
            st.error("Please enter both names!")
        elif not name:
            st.error("Please enter your name!")
        elif not partner_name:
            st.error("Please enter your partner name!")
        else:
            love_score = love_calc(name, partner_name)
            successs = True
if successs:
    if ur_gender == "Male":
        st.info(f"Champion, your love score is: {love_score}%!")
    else:
        st.info(f"Queen, your love score is: {love_score}%!")
    st.markdown(generate_circle_html(love_score), unsafe_allow_html=True)
    st.divider()
    st.markdown(f"### 💬 {random.choice(pickup_lines)}")

