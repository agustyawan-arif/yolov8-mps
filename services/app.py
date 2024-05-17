import time
import requests
import streamlit as st

st.set_page_config(layout="wide")
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
""", unsafe_allow_html=True)

st.title("YOLOv8 Medium with CPU")
left_pane, right_pane = st.columns(2)

with left_pane:
    html_string = '<img src="http://127.0.0.1:1121/detect" class="img-fluid" alt="http://127.0.0.1:1123/video-stream">'
    st.markdown(html_string, unsafe_allow_html=True)
with right_pane:
    result_text = st.empty()
    while True:
        try:
            response = requests.get("http://127.0.0.1:1121/get_queue")
            response = response.json()
            result_text.write(response)
        except:
            result_text.write("")