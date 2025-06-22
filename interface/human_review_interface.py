# interface/human_review_interface.py

import streamlit as st
import json
import os
from pathlib import Path

st.set_page_config(layout="wide")
st.title("📘 Human-in-the-Loop Review Interface")

# Load data from saved JSON file
DATA_PATH = "interface/temp_review_data.json"

if not os.path.exists(DATA_PATH):
    st.error("❌ Data file not found. Please run `main.py` first.")
    st.stop()

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

original_text = data.get("original", "")
spun_text = data.get("spun", "")
reviewed_text = data.get("reviewed", "")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("1️⃣ Original Chapter Text")
    st.text_area("Original Text", value=original_text, height=400, disabled=True)

    st.subheader("2️⃣ AI-Spun Chapter")
    st.text_area("Spun Text", value=spun_text, height=400, disabled=True)

with col2:
    st.subheader("3️⃣ AI-Reviewed Chapter")
    final_text = st.text_area("✍️ Final Editable Version", value=reviewed_text, height=830)

# Final Save Option
st.markdown("---")
output_filename = st.text_input("📝 Save Final Output As:", value="final_output.txt")

if st.button("✅ Finalize and Save"):
    Path("final_output").mkdir(exist_ok=True)
    output_path = f"final_output/{output_filename}"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_text)
    st.success(f"✅ Final version saved to: `{output_path}`")
