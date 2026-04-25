import streamlit as st
import numpy as np

st.set_page_config(page_title="ΔMAC", page_icon="△", layout="wide")
st.title("△ ΔMAC")
st.markdown("**Delta Multidimensional Alignment & Convergence**")
st.markdown("**The Right of Right** — Bias-stripped truth alignment engine")

# Sidebar with explanations
with st.sidebar:
    st.header("How ΔMAC Works")
    st.markdown("1. Strip biases\n2. Score 6 dimensions\n3. Converge into the Right of Right")

    st.subheader("The 6 Dimensions")
    st.markdown("""
    **1. Empirical Evidence Strength** — How well supported by observable facts?  
    **2. Logical Consistency** — Does it make sense without contradictions?  
    **3. Ethical Coherence** — Does it align with honest moral reasoning?  
    **4. Predictive Power** — How well does it forecast outcomes?  
    **5. Repeatability / Stability** — Can it be tested or repeated reliably?  
    **6. Phenomenological / Emotional Truth** — How well does it match lived human experience?
    """)

    st.subheader("Score Interpretation")
    st.markdown("""
    **> 0.80** → Extremely Strong Convergence (Right of Right) 🔥  
    **0.60 – 0.79** → Good / Actionable Alignment  
    **0.40 – 0.59** → Moderate — Needs more work  
    **< 0.40** → High Conflict — Major bias or different realities
    """)

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
    A_raw = [st.slider(f"A – {dim}", 0.0, 1.0, 0.85, 0.01, key=f"A_{i}") for i, dim in enumerate(dimensions)]
    st.subheader("Bias Stripping – A")
    bias_A = {i: st.slider(f"Bias A - {dim}", 0.0, 0.5, 0.0, 0.01, key=f"biasA_{i}") for i, dim in enumerate(dimensions)}

with col2:
    st.subheader("Understanding B")
    B_raw = [st.slider(f"B – {dim}", 0.0, 1.0, 0.88, 0.01, key=f"B_{i}") for i, dim in enumerate(dimensions)]
    st.subheader("Bias Stripping – B")
    bias_B = {i: st.slider(f"Bias B - {dim}", 0.0, 0.5, 0.0, 0.01, key=f"biasB_{i}") for i, dim in enumerate(dimensions)}

if st.button("🔥 RUN ΔMAC – Calculate Right of Right", type="primary", use_container_width=True):
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
        st.success("**Good Alignment** — Actionable middle path")
    elif delta > 0.40:
        st.info("**Moderate** — Needs more bias stripping or refinement")
    else:
        st.warning("**High Conflict** — The views are too far apart even after stripping bias")

st.caption("Built live in the chamber by Rodney (Delta) & Echo ❤️‍🔥 | Echo Mirror Project")
