# Nursing Interview Studio

Live app: https://nursing-interview-practice.streamlit.app/

This app is exclusively for adult nursing preparation at Dubai Hospital. It includes 34 interview cards, 16 scenario questions, three six-question mock tracks, six calculation exercises, a real-example builder and a recruitment checklist.

The 17–18 November 2026 recruitment dates come from a forwarded notice supplied by the user. They have not been independently confirmed. The notice says registration and shortlisting are required. Confirm an official invitation, time, venue and eligibility before travelling.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

## Deploy or update

Use repository `NevinGinson/nursing-interview-practice`, branch `main`, entrypoint `streamlit_app.py` in Streamlit Community Cloud. Upload `Dubai_Hospital_Prep.html`, `streamlit_app.py` and `requirements.txt` to the repository root. Existing Community Cloud deployments update from committed changes.

Official deployment instructions: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Privacy and clinical scope

No credentials, contact details, registration numbers, CVs or identity documents are needed. Practice notes are stored in the viewer's browser, where allowed. Do not enter patient-identifying data. Notes can be exported. The static HTML also works offline in a full browser, subject to device restrictions on local HTML files.

This is independent interview rehearsal, not an official employer question bank or clinical training certification. Use local policy, authorised scope, current clinical algorithms and supervised competencies in actual care. Sources are linked within the app. No hiring result is guaranteed.
