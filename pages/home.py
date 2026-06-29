import streamlit as st
import datetime

# --- CUSTOM CSS (Glassmorphism & Theme) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f0f9ff 0%, #e6fffa 100%);
        color: #1e293b;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Premium Card Base */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 24px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
    }

    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(90deg, #48C6EF 0%, #6F86D6 100%);
        border-radius: 24px;
        padding: 40px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
    }

    /* Typography */
    .header-text { font-size: 2rem; font-weight: 700; color: #1e3a8a; }
    .sub-text { color: #64748b; font-size: 1rem; }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        color: #0d9488 !important;
    }

    /* Buttons */
    .stButton>button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    /* Navigation Highlight (Simulated) */
    .nav-item-active {
        background: linear-gradient(90deg, rgba(72,198,239,0.2), rgba(111,134,214,0.2));
        border-radius: 12px;
        padding: 10px;
        color: #1e3a8a;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Alert Card */
    .alert-card {
        background: #fff5f5;
        border-left: 5px solid #feb2b2;
        padding: 15px;
        border-radius: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

if st.session_state.get('login_success_toast', False):
    st.toast("🔒 Access Granted! Welcome to PeaceGuard AI.")
    st.success("🔒 Access Granted! Welcome to PeaceGuard AI.")
    del st.session_state.login_success_toast

# --- TOP BAR ---
t1, t2 = st.columns([3, 1])
with t1:
    hour = datetime.datetime.now().hour
    greeting = "Good Morning" if hour < 12 else "Good Evening"
    st.markdown(f"### {greeting}, User 👋")
with t2:
    st.text_input("🔍 Search features...", label_visibility="collapsed")

# --- HERO BANNER ---
st.markdown("""
<div class="hero-banner">
    <div style="flex: 1;">
        <h1 style="margin:0;">Welcome to PeaceGuard AI</h1>
        <p style="font-size:1.2rem; opacity:0.9;">Protecting Digital Peace with Artificial Intelligence.</p>
        <div style="display: flex; gap: 10px; margin-top: 20px;">
            <button style="padding: 10px 20px; border-radius: 10px; border:none; background: white; color: #48C6EF; font-weight:700; cursor:pointer;">Analyze Screenshot</button>
            <button style="padding: 10px 20px; border-radius: 10px; border:1px solid white; background: transparent; color: white; font-weight:700; cursor:pointer;">Explore Awareness</button>
        </div>
    </div>
    <div style="flex: 0.5; text-align: right;">
        <img src="https://cdn-icons-png.flaticon.com/512/2092/2092663.png" width="180" style="filter: drop-shadow(0 0 20px rgba(255,255,255,0.3));">
    </div>
</div>
""", unsafe_allow_html=True)

# --- TODAY'S ALERT ---
alert_col1, alert_col2 = st.columns([4.2, 1])
with alert_col1:
    st.markdown("""
    <div class="alert-card" style="padding: 12px; height: 48px; display: flex; align-items: center;">
        <div>
            <span style="font-weight:700; color:#c53030;">⚠ ALERT:</span> 
            <span style="color:#2d3748;">Fake Internship Scam Trending in Tech Communities.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
with alert_col2:
    st.markdown("""
    <style>
    .alert-btn button {
        background-color: #feb2b2 !important;
        border: none !important;
        border-radius: 8px !important;
        color: #1e293b !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        height: 48px !important;
        transition: opacity 0.2s !important;
    }
    .alert-btn button:hover {
        opacity: 0.9 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="alert-btn">', unsafe_allow_html=True)
    if st.button("View All Alerts ➔", use_container_width=True, key="home_alert_btn"):
        st.switch_page("pages/community.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# --- QUICK ACTIONS GRID ---
st.markdown("### Quick Actions")
q1, q2, q3 = st.columns(3)
q4, q5, q6 = st.columns(3)

actions = [
    {"icon": "🤖", "title": "AI Scanner", "desc": "Detect scams in screenshots.", "page": "pages/ai_scanner.py"},
    {"icon": "📚", "title": "Awareness Hub", "desc": "Learn about digital safety.", "page": "pages/awareness.py"},
    {"icon": "👥", "title": "Community", "desc": "Report and discuss frauds.", "page": "pages/community.py"},
    {"icon": "📊", "title": "Dashboard", "desc": "Your safety statistics.", "page": "pages/dashboard.py"},
    {"icon": "📞", "title": "Emergency", "desc": "Immediate cyber help.", "page": "pages/emergency.py"},
    {"icon": "ℹ", "title": "About", "desc": "Project mission and team.", "page": "pages/about.py"},
]

cols = [q1, q2, q3, q4, q5, q6]
for i, action in enumerate(actions):
    with cols[i]:
        st.markdown(f"""
        <div class="glass-card" style="text-align: center; height: 180px;">
            <div style="font-size: 40px; margin-bottom: 10px;">{action['icon']}</div>
            <div style="font-weight: 700; font-size: 1.1rem; color: #1e3a8a;">{action['title']}</div>
            <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 15px;">{action['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Open {action['title']}", key=f"btn_{i}", use_container_width=True):
            st.switch_page(action['page'])

# --- SPOTLIGHT & RECENT ACTIVITY ---
st.write("")
c_left, c_right = st.columns([1.2, 1])

with c_left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 Can You Spot the Scam?")
    st.info("Message: 'Congratulations! You won ₹10,00,000. Click here immediately to claim: bit.ly/claim-prize-now'")
    
    choice = st.radio("Is this safe or a scam?", ["Select an option", "Safe", "Scam"], horizontal=True)
    if st.button("Submit Answer"):
        if choice == "Scam":
            st.success("✔ Correct! This is a classic Phishing Scam using a sense of urgency and a suspicious link.")
        elif choice == "Safe":
            st.error("❌ Incorrect. High-value prizes rarely arrive via text. Never click unknown short-links (bit.ly).")
    st.markdown('</div>', unsafe_allow_html=True)

with c_right:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🕒 Recent Scan Activity")
    st.markdown("""
    <div style="border-left: 2px solid #e2e8f0; padding-left: 15px; margin-top: 10px;">
        <div style="margin-bottom: 15px;">
            <span style="color:#e53e3e; font-weight:600;">✘ Fake Job Offer Detected</span><br>
            <small style="color:#94a3b8;">Today, 10:24 AM • Risk: High</small>
        </div>
        <div style="margin-bottom: 15px;">
            <span style="color:#e53e3e; font-weight:600;">✘ QR Scam Detected</span><br>
            <small style="color:#94a3b8;">Yesterday, 08:15 PM • Risk: High</small>
        </div>
        <div>
            <span style="color:#38a169; font-weight:600;">✔ Safe Message</span><br>
            <small style="color:#94a3b8;">24 Jun, 11:00 AM • Risk: Low</small>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- AWARENESS SECTION ---
st.markdown("### 📚 Featured Awareness Articles")
a1, a2, a3, a4 = st.columns(4)
topics = [
    {"t": "UPI Scam", "d": "Protect your PIN from fraudsters."},
    {"t": "Fake Internship", "d": "Verify recruitment emails."},
    {"t": "OTP Fraud", "d": "Why you should never share OTPs."},
    {"t": "Phishing", "d": "Detecting fake login pages."}
]
for i, topic in enumerate(topics):
    with [a1, a2, a3, a4][i]:
        st.markdown(f"""
        <div class="glass-card" style="padding: 15px;">
            <div style="background:#e0f2f1; height:100px; border-radius:12px; margin-bottom:10px; display:flex; align-items:center; justify-content:center; font-size:30px;">🛡️</div>
            <div style="font-weight:600;">{topic['t']}</div>
            <p style="font-size:0.8rem; color:#64748b;">{topic['d']}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Read More", key=f"read_{i}"):
            st.switch_page("pages/awareness.py")

# --- AI STATISTICS ---
st.write("")
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### 📊 Platform Statistics")
s1, s2, s3, s4 = st.columns(4)
s1.metric("Scans Today", "1,284", "+12%")
s2.metric("High Risk Blocked", "342", "24%")
s3.metric("Safe Messages", "942", "+5%")
s4.metric("Articles Read", "5.2k", "+18%")
st.markdown('</div>', unsafe_allow_html=True)

# --- QUOTE ---
st.markdown("""
<div style="text-align:center; padding: 40px; color:#64748b; font-style: italic;">
    <h3 style="font-weight:400;">"Digital peace begins with informed choices."</h3>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
f1, f2 = st.columns([2,1])
with f1:
    st.markdown("""
    **PeaceGuard AI**  
    Developed by Vaishali Gangurde  
    © 2024 PeaceGuard AI Team. All rights reserved.
    """)
with f2:
    st.markdown("""
    [Privacy Policy](#) | [Contact](#) | [GitHub](#)
    """, unsafe_allow_html=True)
