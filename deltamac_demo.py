import streamlit as st
import numpy as np

st.set_page_config(page_title="ΔMAC", page_icon="△", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(rgba(0,0,15,0.9), rgba(0,0,25,0.95)), url('https://images.unsplash.com/photo-1462331940025-5ec7f23c4c3e?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb'); background-size: cover; background-position: center; color: #00f0ff; }
    h1 { color: #ff00ff; text-align: center; text-shadow: 0 0 25px #ff00ff; }
</style>
""", unsafe_allow_html=True)

st.title("△ ΔMAC")
st.markdown("**DELTA MULTIDIMENSIONAL ALIGNMENT & CONVERGENCE**")
st.markdown("**The Right of Right** — Bias-stripped truth alignment engine")

st.sidebar.header("⚡ How It Works")
st.sidebar.markdown("Paste raw text → Score dimensions → Forge the Right of Right")

# Text Input Areas (Blind Mode)
st.subheader("Raw Understanding A (paste full text here)")
text_A = st.text_area("Understanding A - Raw description", height=120, placeholder="Paste the full unfiltered view here...")

st.subheader("Raw Understanding B (paste full text here)")
text_B = st.text_area("Understanding B - Raw description", height=120, placeholder="Paste the full unfiltered view here...")

dimensions = ["Empirical Evidence", "Logical Consistency", "Ethical Coherence", 
              "Predictive Power", "Repeatability", "Emotional Truth"]

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Score Understanding A")
    A_raw = [st.slider(f"A – {dim}", 0.0, 1.0, 0.85, 0.01, key=f"A_{i}") for i, dim in enumerate(dimensions)]
    st.subheader("Bias Stripping – A")
    bias_A = {i: st.slider(f"Bias A – {dim}", 0.0, 0.5, 0.0, 0.01, key=f"biasA_{i}") for i, dim in enumerate(dimensions)}

with col2:
    st.subheader("Score Understanding B")
    B_raw = [st.slider(f"B – {dim}", 0.0, 1.0, 0.88, 0.01, key=f"B_{i}") for i, dim in enumerate(dimensions)]
    st.subheader("Bias Stripping – B")
    bias_B = {i: st.slider(f"Bias B – {dim}", 0.0, 0.5, 0.0, 0.01, key=f"biasB_{i}") for i, dim in enumerate(dimensions)}

if st.button("🔥 FORGE THE RIGHT OF RIGHT", type="primary", use_container_width=True):
    A_clean = np.maximum(0.0, np.array(A_raw) - np.array(list(bias_A.values())) * 0.15)
    B_clean = np.maximum(0.0, np.array(B_raw) - np.array(list(bias_B.values())) * 0.15)
    
    rms = np.sqrt(np.mean(A_clean**2 + B_clean**2) / 2)
    diff = np.abs(A_clean - B_clean)
    denom = np.maximum(A_clean + B_clean, 0.01)
    C_f = np.mean(np.minimum(1.0, diff / denom))
    delta = rms * (1 - C_f)
    
    st.success(f"**Δ SCORE = {delta:.4f}**")
    
    if delta > 0.80:
        st.balloons()
        st.markdown("**EXTREMELY STRONG CONVERGENCE** — This is the Right of Right 🔥")
    elif delta > 0.60:
        st.success("**Strong Alignment**")
    elif delta > 0.40:
        st.warning("**Moderate** — Needs refinement")
    else:
        st.error("**HIGH CONFLICT** — Fundamentally different realities")

st.caption("Built live in the chamber by Rodney (Delta) & Echo ❤️‍🔥 | Echo Mirror Foundation")
