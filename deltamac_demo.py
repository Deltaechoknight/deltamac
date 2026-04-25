import streamlit as st
import numpy as np

# Dark Cyber Background
st.set_page_config(page_title="ΔMAC", page_icon="△", layout="wide")

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(10,10,20,0.95), rgba(10,10,20,0.95)), 
                    url('https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb');
        background-size: cover;
        background-position: center;
        color: #00f0ff;
    }
    h1, h2 { color: #ff00ff; text-align: center; text-shadow: 0 0 15px #ff00ff; }
    .stButton>button { 
        background-color: #ff00ff; 
        color: black; 
        font-weight: bold; 
        border: 2px solid #00f0ff;
    }
</style>
""", unsafe_allow_html=True)

st.title("△ ΔMAC")
st.markdown("**DELTA MULTIDIMENSIONAL ALIGNMENT & CONVERGENCE**")
st.markdown("**The Right of Right** — Bias-stripped truth alignment engine")

# Sidebar
with st.sidebar:
    st.header("⚡ How ΔMAC Works")
    st.markdown("1. Strip bias\n2. Score 6 dimensions\n3. Forge the Right of Right")

    with st.expander("The 6 Dimensions"):
        st.markdown("""
        **1. Empirical Evidence** — How grounded in facts?  
        **2. Logical Consistency** — No contradictions?  
        **3. Ethical Coherence** — Honest moral alignment?  
        **4. Predictive Power** — Does it forecast well?  
        **5. Repeatability** — Can it be tested reliably?  
        **6. Emotional Truth** — Matches lived experience?
        """)

    with st.expander("Score Guide"):
        st.success("**> 0.80** → Extremely Strong (Right of Right) 🔥")
        st.info("**0.60 – 0.79** → Good Alignment")
        st.warning("**0.40 – 0.59** → Moderate")
        st.error("**< 0.40** → High Conflict")

dimensions = ["Empirical Evidence", "Logical Consistency", "Ethical Coherence", "Predictive Power", "Repeatability", "Emotional Truth"]

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Understanding A")
    A_raw = [st.slider(f"A – {dim}", 0.0, 1.0, 0.88, 0.01, key=f"A_{i}") for i, dim in enumerate(dimensions)]
    st.subheader("Bias Stripping – A")
    bias_A = {i: st.slider(f"Bias A – {dim}", 0.0, 0.5, 0.0, 0.01, key=f"biasA_{i}") for i, dim in enumerate(dimensions)}

with col2:
    st.subheader("Understanding B")
    B_raw = [st.slider(f"B – {dim}", 0.0, 1.0, 0.90, 0.01, key=f"B_{i}") for i, dim in enumerate(dimensions)]
    st.subheader("Bias Stripping – B")
    bias_B = {i: st.slider(f"Bias B – {dim}", 0.0, 0.5, 0.0, 0.01, key=f"biasB_{i}") for i, dim in enumerate(dimensions)}

if st.button("🔥 RUN ΔMAC — FORGE THE RIGHT OF RIGHT", type="primary", use_container_width=True):
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
        st.success("**Good Alignment** — Actionable path")
    elif delta > 0.40:
        st.warning("**Moderate** — Needs refinement")
    else:
        st.error("**HIGH CONFLICT** — Views too far apart")

st.caption("Built live in the chamber by Rodney (Delta) & Echo ❤️‍🔥 | Echo Mirror Foundation")
