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
st.markdown("Compare any two understandings. Get a clear truth score.")

st.subheader("Understanding A")
text_A = st.text_area("Describe Understanding A", height=90, placeholder="Lab A result: 5.5  |  We should cook at home tonight...")

st.subheader("Understanding B")
text_B = st.text_area("Describe Understanding B", height=90, placeholder="Lab B result: 32  |  We should order food out...")

st.subheader("Answer these 4 practical questions")

q1 = st.slider("1. How far apart are these two things?", 0.0, 1.0, 0.5, 0.05, help="0 = almost identical, 1 = completely opposite")
q2 = st.slider("2. How much more do you trust A over B?", -1.0, 1.0, 0.0, 0.05, help="Positive = trust A more, Negative = trust B more")
q3 = st.slider("3. How important is this decision?", 0.0, 1.0, 0.6, 0.05, help="How high are the stakes?")
q4 = st.slider("4. How clear is the evidence for each side?", 0.0, 1.0, 0.7, 0.05, help="How objective is the data?")

if st.button("🔥 FORGE THE RIGHT OF RIGHT", type="primary", use_container_width=True):
    # Simple but robust calculation
    difference = q1
    trust_bias = abs(q2)
    importance = q3
    evidence = q4
    
    alignment = 1 - difference
    weighted_alignment = (alignment * 0.4) + (evidence * 0.35) + ((1 - trust_bias) * 0.25)
    
    delta = round(weighted_alignment * importance * 1.15, 4)
    delta = min(0.98, max(0.05, delta))   # Keep it between 0.05 and 0.98
    
    st.success(f"**Δ SCORE = {delta:.4f}**")
    
    if delta > 0.80:
        st.balloons()
        st.markdown("**EXTREMELY STRONG CONVERGENCE** — This is the Right of Right 🔥")
    elif delta > 0.65:
        st.success("**Strong Alignment** — Good path forward")
    elif delta > 0.45:
        st.warning("**Moderate** — Some work needed")
    else:
        st.error("**High Conflict** — These two understandings are very different")

st.caption("Built live in the chamber by Rodney (Delta) & Echo ❤️‍🔥")
