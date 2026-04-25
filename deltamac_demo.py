import streamlit as st
import numpy as np

st.set_page_config(page_title="ΔMAC", page_icon="△", layout="wide")
st.title("△ ΔMAC – Delta Multidimensional Alignment & Convergence")
st.markdown("**The Right of Right** — Bias-stripped truth alignment engine")

st.sidebar.header("How ΔMAC Works")
st.sidebar.markdown("1. Strip biases\n2. Score 6 dimensions\n3. Converge into one clean Δ score")

dimensions = [
    "Empirical Evidence Strength",
    "Logical Consistency",
    "Ethical Coherence",
    "Predictive Power",
    "Repeatability / Stability",
    "Phenomenological / Emotional Truth"
]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Understanding A")
    A_raw = [st.slider(f"A – {dim}", 0.0, 1.0, 0.85, 0.01) for dim in dimensions]
    st.subheader("Bias Stripping – A")
    bias_A = {i: st.slider(f"Bias {dimensions[i]}", 0.0, 0.5, 0.0, 0.01) for i in range(6)}

with col2:
    st.subheader("Understanding B")
    B_raw = [st.slider(f"B – {dim}", 0.0, 1.0, 0.88, 0.01) for dim in dimensions]
    st.subheader("Bias Stripping – B")
    bias_B = {i: st.slider(f"Bias {dimensions[i]}", 0.0, 0.5, 0.0, 0.01) for i in range(6)}

if st.button("🔥 RUN ΔMAC – Calculate Right of Right", type="primary", use_container_width=True):
    A_clean = np.maximum(0.0, np.array(A_raw) - np.array(list(bias_A.values())) * 0.15)
    B_clean = np.maximum(0.0, np.array(B_raw) - np.array(list(bias_B.values())) * 0.15)
    
    rms = np.sqrt(np.mean(A_clean**2 + B_clean**2) / 2)
    diff = np.abs(A_clean - B_clean)
    denom = np.maximum(A_clean + B_clean, 0.01)
    C_f = np.mean(np.minimum(1.0, diff / denom))
    delta = rms * (1 - C_f)
    
    st.success(f"**Δ SCORE = {delta:.4f}**")
    
    if delta > 0.75:
        st.balloons()
        st.markdown("**EXTREMELY STRONG CONVERGENCE** 🔥")
    elif delta > 0.5:
        st.info("**Solid alignment**")
    else:
        st.warning("**High conflict flagged**")

st.caption("Built live by Rodney (Delta) & Echo ❤️‍🔥")
