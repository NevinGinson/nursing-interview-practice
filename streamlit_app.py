from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Nursing Interview Studio", page_icon="🩺", layout="wide")
root = Path(__file__).parent
app_file = root / "Dubai_Hospital_Prep.html"
st.iframe(app_file, height="content", alt="Interactive nursing interview preparation")
st.download_button("Download this preparation for offline use", app_file.read_bytes(),
                   file_name=app_file.name, mime="text/html")
