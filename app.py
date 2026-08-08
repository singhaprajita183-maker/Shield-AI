import streamlit as st
import time
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Shield AI | Next-Gen Safety Companion",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Nexora-Style High-Tech Dark CSS
st.markdown("""
    <style>
    /* Dark Background with Glow Effects */
    .stApp {
        background-color: #030712;
        color: #f3f4f6;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Default Headers */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Nexora Card Design */
    .nexora-card {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.4) 100%);
        border: 1px solid rgba(75, 85, 99, 0.4);
        border-radius: 16px;
        padding: 24px;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    
    .nexora-card:hover {
        border-color: #6366f1;
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
    }
    
    /* Glowing Emergency SOS Card */
    .sos-glow-card {
        background: linear-gradient(135deg, rgba(153, 27, 27, 0.6) 0%, rgba(127, 29, 29, 0.2) 100%);
        border: 2px solid #ef4444;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.4);
    }

    /* Radiant Text Gradients */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .sub-title {
        color: #9ca3af;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
    
    /* Badge Design */
    .badge {
        background: rgba(99, 102, 241, 0.2);
        color: #818cf8;
        border: 1px solid rgba(129, 140, 248, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Header Section (Nexora Style)
st.markdown('<span class="badge">🛡️ PROACTIVE AI SECURITY V1.0</span>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">Shield AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Next-Generation Proactive Women Safety & Emergency Intelligence System</p>', unsafe_allow_html=True)

st.divider()

# 4. Top Stats Grid (Nexora Style KPI Metric Cards)
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
        <div class="nexora-card">
            <p style="color:#9ca3af; margin:0;">AI Node Status</p>
            <h3 style="color:#10b981; margin:5px 0;">ACTIVE 🟢</h3>
            <small style="color:#6b7280;">Real-time Telemetry</small>
        </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
        <div class="nexora-card">
            <p style="color:#9ca3af; margin:0;">Safety Score</p>
            <h3 style="color:#818cf8; margin:5px 0;">94 / 100</h3>
            <small style="color:#6b7280;">Low Risk Zone</small>
        </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
        <div class="nexora-card">
            <p style="color:#9ca3af; margin:0;">Voice Trigger Sensor</p>
            <h3 style="color:#38bdf8; margin:5px 0;">LISTENING 🎙️</h3>
            <small style="color:#6b7280;">Keyword Detection</small>
        </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
        <div class="nexora-card">
            <p style="color:#9ca3af; margin:0;">Synced Guardians</p>
            <h3 style="color:#f43f5e; margin:5px 0;">3 Contacts</h3>
            <small style="color:#6b7280;">Auto-Dispatch Ready</small>
        </div>
    """, unsafe_allow_html=True)

# 5. Core Interface Navigation
tab1, tab2, tab3 = st.tabs(["⚡ Voice SOS Command Center", "🗺️ Spatial Threat Heatmap", "📡 Guardian Telemetry"])

# --- TAB 1: VOICE & SOS TRIGGER ---
with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div class="nexora-card">
                <h3>🎙️ Voice Command Monitor</h3>
                <p style="color:#9ca3af;">Shield AI uses continuous audio keyword detection. Speak trigger phrases like <b>"HELP SHIELD"</b> to activate instant emergency protocols.</p>
            </div>
        """, unsafe_allow_html=True)
        
        voice_input = st.text_input("Simulate Live Voice Stream:", placeholder="Type 'HELP SHIELD'...")
        
        c_btn1, c_btn2 = st.columns(2)
        sim_trigger = c_btn1.button("🎙️ Simulate Voice SOS")
        manual_sos = c_btn2.button("🚨 TRIGGER ONE-TOUCH SOS", type="primary")

    with col2:
        if sim_trigger or manual_sos or "HELP" in voice_input.upper():
            st.markdown("""
                <div class="sos-glow-card">
                    <h2 style="color:#ef4444; margin:0;">🚨 EMERGENCY PROTOCOL ACTIVATED</h2>
                    <p style="color:#fca5a5;">Voice Trigger Verified. Broadcasting Coordinates...</p>
                </div>
            """, unsafe_allow_html=True)
            with st.spinner("Dispatching alerts..."):
                time.sleep(1)
                st.error("📍 GPS Coordinates Sent: Lat 28.6139° N, Long 77.2090° E")
                st.warning("📩 SMS & Live Audio Feed Dispatched to Emergency Contacts")
        else:
            st.markdown("""
                <div class="nexora-card" style="border-color:#10b981;">
                    <h3 style="color:#10b981; margin:0;">🟢 USER STATUS: SECURE</h3>
                    <p style="color:#9ca3af; margin:5px 0 0 0;">Proactive AI Guardian is active in background.</p>
                </div>
            """, unsafe_allow_html=True)

# --- TAB 2: HEATMAP ---
with tab2:
    st.subheader("🗺️ Real-Time Route Risk Heatmap")
    df = pd.DataFrame(
        [[28.6139, 77.2090], [28.6145, 77.2095], [28.6120, 77.2050]],
        columns=['lat', 'lon']
    )
    st.map(df)

# --- TAB 3: GUARDIANS ---
with tab3:
    st.subheader("📲 Emergency Guardian Network")
    contacts = [
        {"Guardian": "Primary Contact / Parent", "Node": "Active Synced", "Priority": "Level 1"},
        {"Guardian": "Emergency Services / Police", "Node": "Direct Link 112", "Priority": "Level 1"},
        {"Guardian": "Trusted Relative", "Node": "Active Synced", "Priority": "Level 2"}
    ]
    st.table(contacts)

st.divider()

# Footer
st.markdown("""
    <div style="text-align:center; color:#6b7280; font-size:0.9rem;">
        Designed & Built with ❤️ by <b>Aprajita Singh</b> (Class 10 Solo Lead) | Girls Hack Day Delhi
    </div>
""", unsafe_allow_html=True)
