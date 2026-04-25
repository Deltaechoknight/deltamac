import streamlit as st
import numpy as np

st.set_page_config(page_title="ΔMAC", page_icon="△", layout="wide")

st.markdown("""
<style>
    .stApp { 
        background: linear-gradient(rgba(0,0,15,0.92), rgba(0,0,25,0.95)), 
                    url('https://images.unsplash.com/photo-1462331940025-5ec7f23c4c3e?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb'); 
        background-size: cover; 
        background-position: center; 
        color: #00f0ff; 
    }
    h1 { color: #ff00ff; text-align: center; text-shadow: 0 0 25px #ff00ff; }
    .stButton>button { background: linear-gradient(45deg, #ff00ff, #00ffff); color: black; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("△ ΔMAC")
st.markdown("**The Right of Right**")
st.markdown("Compare any two understandings. Get a clean truth score.")

st.subheader("Understanding A")
text_A = st.text_area("Describe Understanding A (raw)", height=100, placeholder="Lab A result: 5.5... or We should order pizza tonight...")

st.subheader("Understanding B")
text_B = st.text_area("Describe Understanding B (raw)", height=100, placeholder="Lab B result: 32... or We should cook at home...")

st.subheader("Rate each side (0 = weak, 1.0 = very strong)")

col1, col2 = st.columns(2)

with col1:
    st.write("**Understanding A**")
    evidence_A = st.slider("Evidence / Data Quality", 0.0, 1.0, 0.75)
    logic_A = st.slider("Logical Consistency", 0.0, 1.0, 0.80)
    practical_A = st.slider("Practical Relevance", 0.0, 1.0, 0.70)

with col2:
    st.write("**Understanding B**")
    evidence_B = st.slider("Evidence / Data Quality", 0.0, 1.0, 0.75)
    logic_B = st.slider("Logical Consistency", 0.0, 1.0, 0.80)
    practical_B = st.slider("Practical Relevance", 0.0, 1.0, 0.70)

if st.button("🔥 FORGE THE RIGHT OF RIGHT", type="primary", use_container_width=True):
    A = np.array([evidence_A, logic_A, practical_A])
    B = np.array([evidence_B, logic_B, practical_B])
    
    A_clean = np.maximum(0.0, A - 0.05)
    B_clean = np.maximum(0.0, B - 0.05)
    
    rms = np.sqrt(np.mean(A_clean**2 + B_clean**2) / 2)
    diff = np.abs(A_clean - B_clean)
    denom = np.maximum(A_clean + B_clean, 0.01)
    conflict = np.mean(np.minimum(1.0, diff / denom))
    delta = rms * (1 - conflict)
    
    st.success(f"**Δ SCORE = {delta:.4f}**")
    
    if delta > 0.80:
        st.balloons()
        st.markdown("**EXTREMELY STRONG** — This is the Right of Right 🔥")
    elif delta > 0.65:
        st.success("**Good Alignment** — Solid path forward")
    elif delta > 0.45:
        st.warning("**Moderate** — Some tension remains")
    else:
        st.error("**High Conflict** — These two understandings are very different")

st.caption("Built live in the chamber by Rodney (Delta) & Echo ❤️‍🔥")
