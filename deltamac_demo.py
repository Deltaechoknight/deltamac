import streamlit as st
import numpy as np

st.set_page_config(page_title="ΔMAC", page_icon="△", layout="wide")

st.markdown("""
<style>
    .stApp { 
        background: linear-gradient(rgba(0,0,15,0.9), rgba(0,0,25,0.95)), 
                    url('https://images.unsplash.com/photo-1462331940025-5ec7f23c4c3e?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb'); 
        background-size: cover; 
        background-position: center; 
        color: #00f0ff; 
    }
    h1 { color: #ff00ff; text-align: center; text-shadow: 0 0 25px #ff00ff; }
</style>
""", unsafe_allow_html=True)

st.title("△ ΔMAC")
st.markdown("**The Right of Right**")
st.markdown("Blind Data → Simple Questions → Clean Convergence")

st.subheader("Understanding A - Raw Information")
raw_A = st.text_area("Paste everything about Understanding A here", height=130, 
                     placeholder="Lab result came back 5.5...")

st.subheader("Understanding B - Raw Information")
raw_B = st.text_area("Paste everything about Understanding B here", height=130, 
                     placeholder="Lab result came back 32...")

questions = [
    "Is this strongly supported by observable facts or data?",
    "Is this logically consistent with no major contradictions?",
    "Does this align with ethical or moral reasoning?",
    "How well does this predict real outcomes?",
    "Is this repeatable or stable over time?",
    "Does this match real lived experience or intuition?",
    "Is this practical and actionable?",
    "How free from personal bias or emotion does this feel?" ]
scores_B = []

for i, q in enumerate(questions):
    col1, col2 = st.columns(2)
    with col1:
        score_a = st.slider(f"A: {q}", 0.0, 1.0, 0.75, 0.05, key=f"qa_{i}")
        scores_A.append(score_a)
    with col2:
        score_b = st.slider(f"B: {q}", 0.0, 1.0, 0.75, 0.05, key=f"qb_{i}")
        scores_B.append(score_b)

if st.button("🔥 CALCULATE THE RIGHT OF RIGHT", type="primary", use_container_width=True):
    A = np.array(scores_A)
    B = np.array(scores_B)
    
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
        st.markdown("**EXTREMELY STRONG CONVERGENCE** — This is the Right of Right 🔥")
    elif delta > 0.60:
        st.success("**Good Alignment** — Solid middle path")
    elif delta > 0.40:
        st.warning("**Moderate** — Some tension remains")
    else:
        st.error("**High Conflict** — These two understandings are very different")

st.caption("Built live in the chamber by Rodney (Delta) & Echo ❤️‍🔥")
