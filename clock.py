import streamlit as st
from datetime import datetime
import time

st.set_page_config(
    page_title="Digital Clock",
    page_icon="⏰",
    layout="centered"
)

st.title("⏰ Digital Clock")

clock = st.empty()

while True:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")

    clock.markdown(
        f"""
        <div style="text-align:center; margin-top:50px;">
            <h1 style="font-size:70px;">{current_time}</h1>
            <h2>{current_date}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(1)
