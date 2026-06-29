import streamlit as st
import time
from custom_components.logo import get_logo_html

# --- PAGE CONFIG ---


# --- ADVANCED CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f0f9ff 0%, #e6fffa 100%);
        color: #1e293b;
    }

    /* Floating Animation for Logo */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    .hero-logo {
        animation: float 4s infinite ease-in-out;
        filter: drop-shadow(0 10px 15px rgba(72, 198, 239, 0.3));
    }

    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        transition: all 0.4s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }

    /* Sidebar Highlight */
    .nav-item-active {
        background: linear-gradient(90deg, rgba(72,198,239,0.2), rgba(111,134,214,0.2));
        border-radius: 12px;
        padding: 12px;
        color: #1e3a8a;
        font-weight: 600;
        border-left: 4px solid #48C6EF;
    }

    /* Gradient Text */
    .gradient-text {
        background: linear-gradient(90deg, #1e3a8a, #0d9488);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* Timeline Styles */
    .timeline-item {
        border-left: 3px solid #48C6EF;
        padding-left: 20px;
        padding-bottom: 25px;
        position: relative;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGO URL ---
LOGO_URL = "https://cdn-icons-png.flaticon.com/512/1067/1067357.png"

# --- SIDEBAR NAVIGATION ---

# --- HERO SECTION ---
c1, c2 = st.columns([1, 2])
with c1:
    try:
        st.html(get_logo_html("large"))
    except AttributeError:
        st.markdown(get_logo_html("large"), unsafe_allow_html=True)
with c2:
    st.markdown('<h1 class="gradient-text" style="font-size: 3.5rem; margin-bottom:0;">About PeaceGuard AI</h1>', unsafe_allow_html=True)
    st.markdown("### Protecting Digital Peace with Intelligence 🛡️")
    st.write("We are an AI-powered platform dedicated to making the internet a safer place for everyone. By combining advanced detection with community-driven awareness, we stop scams before they happen.")

# --- INTERACTIVE TABS ---
st.markdown("<br>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["🚀 Our Story", "🧠 The Technology", "📈 Our Impact"])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### Our Mission 🚀")
    st.write("PeaceGuard AI is a dedicated digital safety application designed to bridge the gap between complex cyber-security and everyday digital users. Our mission is to provide simple, actionable safety tools and promote safe online behavior.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### The AI Core 🪄")
    t_col1, t_col2, t_col3 = st.columns(3)
    t_col1.metric("Vision AI", "OCR Extraction", "98%")
    t_col2.metric("LLM Core", "Pattern Detection", "Secure")
    t_col3.metric("Community", "Verified Reports", "Real-time")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("#### Projected Reach 🌍")
    target = st.select_slider("Select Projected Impact:", options=["Local Hub", "City Wide", "State Level", "National", "Global"])
    st.write(f"Our current development focus: **{target}**")
    st.markdown('</div>', unsafe_allow_html=True)

# --- MILESTONES ---
st.markdown("### Our Milestones 📍")
st.markdown("""
<div class="timeline-item"><b>📍 Concept Sparked</b>: Identifying the need for social safety.</div>
<div class="timeline-item"><b>📍 Prototype Build</b>: Developing the AI Scanner engine.</div>
<div class="timeline-item" style="border:none;"><b>📍 Community Launch</b>: Bringing PeaceGuard to the world.</div>
""", unsafe_allow_html=True)

# --- REWARD INTERACTION ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="glass-card" style="background: #e0f2f1; text-align:center;">', unsafe_allow_html=True)
if st.button("Unlock Your Guardian Badge 🎖️"):
    st.balloons()
    try:
        st.html(get_logo_html("small"))
    except AttributeError:
        st.markdown(get_logo_html("small"), unsafe_allow_html=True)
    st.success("You are now a certified PeaceGuard Protector!")
st.markdown('</div>', unsafe_allow_html=True)

# --- GET IN TOUCH & NAVIGATION ---
st.write("<br>", unsafe_allow_html=True)
ac1, ac2, ac3 = st.columns(3)
with ac1:
    if st.button("📞 Contact Us", use_container_width=True):
        st.info("✉️ Contact Information:\n- Email: support@peaceguard.ai\n- Toll-Free: 1930\n- Office: PeaceGuard Cyber Safety Cell")
with ac2:
    if st.button("🐙 GitHub Profile", use_container_width=True):
        st.toast("Redirecting to GitHub profile...")
        st.success("Project Created By: Vaishali Gangurde")
        st.markdown("[Visit Profile ➔](https://github.com/vaishaligangurde594-png)", unsafe_allow_html=True)
with ac3:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/home.py")

# --- FOOTER ---
st.divider()
st.markdown("<p style='text-align:center; color:#64748b;'>PeaceGuard AI • Developed by Vaishali Gangurde</p>", unsafe_allow_html=True)