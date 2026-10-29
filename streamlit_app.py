from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Nursing Interview Practice", page_icon="🌿", layout="wide")
app_file = Path(__file__).with_name("Interview_Prep.html")
# Only embed this reviewed, static project file. Never embed user-supplied HTML.
st.iframe(app_file, height="content", alt="Interactive nursing interview practice")
st.download_button("Download the offline HTML", app_file.read_bytes(),
                   file_name="Interview_Prep.html", mime="text/html")
