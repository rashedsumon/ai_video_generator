# app.py
import streamlit as st
from data_loader import download_dataset
from utils.video_utils import generate_video_from_prompts

# --- Streamlit Setup ---
st.set_page_config(page_title="AI Video Generator", layout="wide")
st.title("🎬 AI Video Generator")
st.write("Generate high-quality animated videos using generative AI models without MoviePy.")

# --- Dataset Download ---
st.header("Step 1: Load Dataset")
dataset_id = st.text_input("Enter KaggleHub Dataset ID", "yogendras843/online-casino-dataset")
if st.button("Download Dataset"):
    path = download_dataset(dataset_id)
    st.success(f"Dataset downloaded to: {path}")

# --- Video Generation ---
st.header("Step 2: Generate Video")
prompt = st.text_area("Enter Video Description / Prompt", "A futuristic city with neon lights")
style = st.selectbox("Choose Animation Style", ["Cinematic", "Cartoon", "Abstract", "Realistic"])
fps = st.slider("FPS", 12, 60, 24)
duration = st.slider("Video Duration (seconds)", 5, 30, 10)

if st.button("Generate Video"):
    with st.spinner("Generating video... 🎨"):
        output_path = generate_video_from_prompts(prompt, style, fps, duration)
    st.success(f"Video saved at: {output_path}")
    st.video(output_path)
