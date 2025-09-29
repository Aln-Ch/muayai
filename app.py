import streamlit as st

st.title("Muay Thai Technique Analyzer MVP")
st.write("Upload a video of your technique to get started.")

video = st.file_uploader("Upload a training clip", type=["mp4", "mov", "avi"])

if video:
    st.video(video)
    st.success("Video uploaded successfully! (Analysis coming soon...)")
