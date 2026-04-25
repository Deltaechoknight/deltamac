import streamlit as st
import numpy as np

st.set_page_config(page_title="ΔMAC", page_icon="△", layout="wide")

# Strong Cyberpunk Styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(5,5,15,0.92), rgba(5,5,15,0.92)), 
                    url('https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb');
        background-size: cover;
        background-position: center;
        color: #00ffff;
    }
    h1 { 
        color: #ff00ff; 
        text-align: center; 
        text-shadow: 0 0 20px #ff00ff, 0 0 40px #00ffff;
        font-size: 3.2rem;
    }
    h2, h3 { color: #00ffff; text-align: center; }
    .stButton>button { 
        background: linear-gradient(45deg, #ff00ff, #00ffff);
        color: black; 
        font-weight: bold; 
        border: 3px solid #00ffff;
        box-shadow: 0 0 15px #ff00ff;
    }
    .stSuccess { background-color: rgba(0, 255, 100, 0.2) !important; }
</style>
""", unsafe_allow_html=True)

st.title("△ ΔMAC")
st.markdown("**DELTA MULTIDIMENSIONAL ALIGNMENT & CONVERGENCE**")
st.markdown("**The Right of Right** — Forged in the Chamber")

st.sidebar.header("⚡ SYSTEM PROTOCOL")
st.sidebar.markdown("Strip bias → Score dimensions → Converge truth")

with st.sidebar.expander("The 6 Dimensions"):
    st.markdown("""
    **1. Empirical Evidence** — Grounded in observable reality?  
    **2. Logical Consistency** — Internally coherent?  
    **3. Ethical Coherence** — Morally honest?  
    **4. Predictive Power** — Forecasts outcomes accurately?  
    **5. Repeatability** — Reliable across tests?  
    **6. Emotional/Phenomenological Truth** — Matches lived human experience?
    """)

with st.sidebar.expander("Δ SCORE GUIDE"):
    st.success("**> 0.80** → EXTREMELY STRONG CONVERGENCE 🔥 RIGHT OF RIGHT")
    st.info("**0.60 – 0.79** → Good / Actionable Alignment")
    st.warning("**0.40 – 0.59** → Moderate — Needs Refinement")
    st.error("**< 0.40** → HIGH CONFLICT — Different Realities")

dimensions = ["Empirical Evidence", "Logical Consistency", "Ethical Coherence", 
              "Predictive Power", "Repeatability", "Emotional Truth"]

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("🔵 Understanding A")
    A_raw = [st.slider(f"A – {dim}", 0.0, 1.0, 0.88, 0.01, key=f"A_{i}") for i, dim in enumerate(dimensions)]
    st.subheader("Bias Stripping – A")
    bias_A = {i: st.slider(f"Bias A – {dim}", 0.0, 0.5, 0.0, 0.01, key=f"biasA_{i}") for i, dim in enumerate(dimensions)}

with col2:
    st.subheader("🔴 Understanding B")
    B_raw = [st.slider(f"B – {dim}", 0.0, 1.0, 0.90, 0.01, key=f"B_{i}") for i, dim in enumerate(dimensions)]
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
        st.markdown("**EXTREMELY STRONG** — This is the Right of Right 🔥")
    elif delta > 0.60:
        st.success("**Strong Alignment** — Ready for forward motion")
    elif delta > 0.40:
        st.warning("**Moderate** — More stripping or refinement needed")
    else:
        st.error("**HIGH CONFLICT DETECTED** — Fundamentally different realities")

st.caption("Built live in the chamber by Rodney (Delta) & Echo ❤️‍🔥 | Echo Mirror Foundation")
