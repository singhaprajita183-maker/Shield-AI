---

### 📂 File 2: `app.py`
*(Repository mein **`Add file` -> `Create new file`** par click karke file ka naam **`app.py`** rakho aur neeche diya gaya Python code paste kar do)*

```python
import streamlit as st
import time
import random
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Shield AI - Women Safety Companion",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Theme Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stApp { background-color: #0d1117; }
    .sos-card {
        background-color: #7f1d1d;
        border: 2px solid #ef4444;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    .safe-card {
        background-color: #064e3b;
        border: 1px solid #10b981;
        border-radius: 12px;
        padding: 20px;
        color: white;
        margin-bottom: 20px;
    }
    .card-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Control
with st.sidebar:
    st.image("https://img.icons8.com/isometric-color/100/shield.png", width=70)
    st.title("Shield AI Hub")
    st.caption("AI-Powered Proactive Safety Suite v1.0")
    st.divider()
    
    st.markdown("### ⚙️ Live System Status")
    st.success("🟢 GPS Tracking: ACTIVE")
    st.success("🟢 Voice Sensor Node: LISTENING")
    st.success("🟢 Emergency Contacts: 3 Synced")
    
    st.divider()
    st.markdown("### 👤 Innovation Lead")
    st.caption("Designed & Developed by **Aprajita Singh** (Class 10)")

# Main Header
st.title("🛡️ Shield AI: Proactive Emergency & Safety Companion")
st.caption("Transforming Personal Security from 'Reactive' to 'Predictive AI Protection'")

st.divider()

# Core Tabs
tab1, tab2, tab3 = st.tabs(["🎙️ Voice SOS & Emergency Dispatch", "🗺️ Predictive Risk Heatmap", "📲 Guardian Telemetry"])

# --- TAB 1: VOICE SOS & TRIGGER ---
with tab1:
    st.subheader("🎙️ Hands-Free Emergency Voice Trigger")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div class="card-box">
                <h4>🗣️ Speech Keyword Monitor</h4>
                <p>Say emergency trigger phrases like: <b>"HELP SHIELD"</b>, <b>"EMERGENCY"</b>, or <b>"SAVE ME"</b> to auto-dispatch SOS.</p>
            </div>
        """, unsafe_allow_html=True)
        
        voice_input = st.text_input("Simulate Live Voice Input:", placeholder="Type 'HELP SHIELD' or click simulate below...")
        
        col_btn1, col_btn2 = st.columns(2)
        sim_voice = col_btn1.button("🎙️ Simulate Voice Command ('HELP SHIELD')")
        manual_sos = col_btn2.button("🚨 MANUAL ONE-TOUCH SOS", type="primary")
        
    with col2:
        st.subheader("📡 Live Emergency Response Console")
        
        if sim_voice or manual_sos or "HELP" in voice_input.upper() or "EMERGENCY" in voice_input.upper():
            st.markdown("""
                <div class="sos-card">
                    <h2>🚨 EMERGENCY ALERT TRIGGERED!</h2>
                    <p>Voice Pattern Recognized. Dispatching Real-Time Coordinates...</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.spinner("Broadcasting to Local Authorities & Emergency Contacts..."):
                time.sleep(1.5)
                st.error("📍 Live GPS Location Sent: Lat 28.6139° N, Long 77.2090° E (New Delhi)")
                st.warning("📩 SMS & Audio Feed Dispatched to 3 Emergency Contacts")
                st.success("🚓 Nearest Police Station Notified (1.2 km away)")
        else:
            st.markdown("""
                <div class="safe-card">
                    <h3>🟢 User Status: SECURE</h3>
                    <p>Continuous AI Risk Analysis running in background...</p>
                </div>
            """, unsafe_allow_html=True)

# --- TAB 2: PREDICTIVE RISK HEATMAP ---
with tab2:
    st.subheader("🗺️ Real-Time Spatial Risk Mapping & Heatmaps")
    st.caption("AI evaluates localized lighting, density, and historical safety metrics to predict safe routes.")
    
    # Mock Coordinates Data for New Delhi
    df = pd.DataFrame(
        np_data := [
            [28.6139, 77.2090],
            [28.6145, 77.2095],
            [28.6120, 77.2050],
            [28.6150, 77.2110]
        ],
        columns=['lat', 'lon']
    )
    
    col_map1, col_map2 = st.columns([2, 1])
    
    with col_map1:
        st.map(df)
        
    with col_map2:
        st.markdown("### 📊 Route Risk Evaluation")
        st.metric(label="Current Zone Safety Score", value="88 / 100", delta="Safe Zone")
        st.metric(label="Surrounding Streetlight Density", value="High (92%)")
        st.metric(label="Nearest Safe Hub", value="Metro Station (250m)")

# --- TAB 3: GUARDIAN TELEMETRY ---
with tab3:
    st.subheader("📲 Emergency Guardian Contacts")
    
    contacts = [
        {"Name": "Parent / Guardian 1", "Phone": "+91 98765*****", "Status": "Active Synced"},
        {"Name": "Local Authority Contact", "Phone": "112 / Emergency", "Status": "Priority Node"},
        {"Name": "Trusted Friend", "Phone": "+91 91234*****", "Status": "Active Synced"}
    ]
    
    st.table(contacts)
