import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import time

st.set_page_config(page_title="Radiology AI", layout="wide", page_icon="📸")

st.markdown("""
    <style>
    .main { background-color: #f1f5f9; color: #0f172a; }
    .stMetric { background-color: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📸 Radiology AI | Pulmonary Screening")
st.write("Deep Learning Diagnostic Support for Chest X-Rays")

uploaded_file = st.file_uploader("Upload Chest X-Ray (JPEG/PNG/DICOM)", type=["jpg", "png", "dcm"])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Original Scan")
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("AI Diagnostic Analysis")
        with st.spinner("Analyzing neural features..."):
            time.sleep(2) # Simulate deep learning inference
            
            # Simulated results
            results = {
                "Pneumonia": 0.88,
                "Infiltration": 0.12,
                "Normal": 0.05
            }
            
            for condition, prob in results.items():
                st.write(f"**{condition}**")
                st.progress(prob)
                st.caption(f"Confidence: {prob*100}%")

            if results["Pneumonia"] > 0.70:
                st.error("🚨 HIGH RISK DETECTED: Clinical review recommended for potential Pneumonia.")
            else:
                st.success("✅ LOW RISK: No significant abnormalities detected in primary screening.")
