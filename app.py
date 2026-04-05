import streamlit as st
import os

from models.speech_to_text import SpeechToText
from models.sound_classifier import SoundClassifier
from models.reasoning import ReasoningEngine

# ⚡ Cache models (for speed)
@st.cache_resource
def load_models():
    return SpeechToText(), SoundClassifier(), ReasoningEngine()

# 🎨 Page config
st.set_page_config(page_title="Military Audio System", layout="wide")

# 🛰️ Sidebar
st.sidebar.title("🛰️ Control Panel")
st.sidebar.success("🟢 System Online")
st.sidebar.markdown("---")
st.sidebar.info("Upload audio to analyze")

# 🎯 Header
st.markdown("<h1 style='text-align:center;'>🛡️ Military Audio Intelligence Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# 📂 Upload
uploaded_file = st.file_uploader("🎧 Upload Audio File", type=["wav", "mp3"])

if uploaded_file is not None:
    file_path = os.path.join("data", uploaded_file.name)

    # Save file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.audio(uploaded_file)

    if st.button("🚀 Run Analysis"):
        st.info("Processing audio...")

        # Load models
        stt, sound_model, reasoning = load_models()

        # 🌍 Speech
        original, translated, lang = stt.transcribe(file_path)

        # 🔊 Sound
        sounds = sound_model.predict(file_path)

        # 🧠 Reasoning
        analysis = reasoning.analyze(translated, sounds)

        # 🔥 MULTIMODAL THREAT LOGIC (FIXED)
        speech_lower = translated.lower()

        threat_words = [
            "danger", "attack", "kill", "fire",
            "blast", "shoot", "gun", "hit", "enemy"
        ]

        if (
            "Gunshot" in sounds
            or "Explosion" in sounds
            or any(word in speech_lower for word in threat_words)
        ):
            threat_level = "HIGH"

        elif "Footsteps" in sounds or "Vehicle" in sounds:
            threat_level = "MEDIUM"

        else:
            threat_level = "LOW"

        # 🚨 TOP ALERT
        if threat_level == "HIGH":
            st.error("🚨 HIGH THREAT LEVEL - IMMEDIATE ACTION REQUIRED")
        elif threat_level == "MEDIUM":
            st.warning("⚠️ MEDIUM THREAT - MOVEMENT DETECTED")
        else:
            st.success("✅ LOW THREAT - ENVIRONMENT STABLE")

        st.markdown("---")

        # 📊 Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("🌍 Language", lang.upper())
        col2.metric("🚨 Threat Level", threat_level)
        col3.metric("🔊 Sound Events", len(sounds))

        st.markdown("---")

        # 🗣️ Communication
        st.markdown("### 🗣️ Communication Analysis")
        st.code(original, language="bash")

        st.markdown("### 🔁 Translated Speech")
        st.code(translated, language="bash")

        st.markdown("---")

        # 🔊 Sounds
        st.markdown("### 🔊 Audio Event Detection")
        if sounds:
            for s in sounds:
                st.markdown(f"- `{s}`")
        else:
            st.write("No significant sounds detected")

        st.markdown("---")

        # 🧠 Final Report
        st.markdown("### 🧠 AI Situation Report")

        if threat_level == "HIGH":
            st.error(analysis)
        elif threat_level == "MEDIUM":
            st.warning(analysis)
        else:
            st.success(analysis)