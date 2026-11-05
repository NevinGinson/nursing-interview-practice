from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Nursing Interview Studio", page_icon="🩺", layout="wide")
root = Path(__file__).parent
options = {"Dubai Hospital · Adult ICU and emergency": "Dubai_Hospital_Prep.html"}
if (root / "Interview_Prep.html").exists():
    options["Maudsley Health · Earlier preparation"] = "Interview_Prep.html"
selection = st.selectbox("Choose your interview preparation", list(options))
app_file = root / options[selection]
st.iframe(app_file, height="content", alt="Interactive nursing interview preparation")
st.download_button("Download this preparation for offline use", app_file.read_bytes(),
                   file_name=app_file.name, mime="text/html")
