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
st.markdown("Give me two understandings. I'll tell you how aligned they really are.")

st.subheader("Understanding A")
text_A = st.text_area("What is one side saying or showing?", height=110, 
                     placeholder="Example: Lab A came back with 5.5... or We should order pizza tonight...")

st.subheader("Understanding B")
text_B = st.text_area("What is the other side saying or showing?", height=110, 
                     placeholder="Example: Lab B came back with 32... or We should cook at home...")

st.subheader("Answer these 8 simple questions")

questions = [
    "How different are these two understandings?",
    "How trustworthy is side A compared to side B?",
    "How important is this decision or topic?",
    "How emotionally attached is each side to their view?",
    "How much real evidence supports each side?",
    "How practical or realistic is each side?",
    "How consistent is each side with what you already know?",
    "Overall, how close do these two views feel to you?" ]

for i, q in enumerate(questions):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.write("**A**")
    with col2:
        score = st.slider(q, 0.0, 1.0, 0.5, 0.05, key=f"q{i}")
        scores.append(score)

if st.button("🔥 CALCULATE THE RIGHT OF RIGHT", type="primary", use_container_width=True):
    A = np.array(scores)
    B = np.array( )   # Simple mirror for now
    
    A_clean = np.maximum(0.0, A - 0.05)
    B_clean = np.maximum(0.0, B - 0.05)
    
    rms = np.sqrt(np.mean(A_clean**2 + B_clean**2) / 2)
    diff = np.abs(A_clean - B_clean)
    conflict = np.mean(np.minimum(1.0, diff / np.maximum(A_clean + B_clean, 0.01)))
    delta = rms * (1 - conflict)
    
    st.success(f"**Δ SCORE = {delta:.4f}**")
    
    if delta > 0.80:
        st.balloons()
        st.markdown("**EXTREMELY STRONG** — This is the Right of Right 🔥")
    elif delta > 0.65:
        st.success("**Good Alignment** — These two views are mostly compatible")
    elif delta > 0.45:
        st.warning("**Moderate** — There's noticeable tension here")
    else:
        st.error("**High Conflict** — These two understandings are very different")

st.caption("Built live in the chamber by Rodney (Delta) & Echo ❤️‍🔥")
