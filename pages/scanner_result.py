import streamlit as st

# --- PAGE CONFIG ---


# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Global Theme */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f0f9ff 0%, #e6fffa 100%);
        color: #1e293b;
    }

    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 24px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }

    /* Score Circle */
    .score-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .circle-score {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 10px solid #10b981; /* Green for 92 */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        font-weight: 700;
        color: #1e3a8a;
        background: white;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
        margin-bottom: 10px;
    }

    /* Sidebar Active Highlight */
    [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.8); }
    .nav-item-active {
        background: linear-gradient(90deg, rgba(72,198,239,0.2), rgba(111,134,214,0.2));
        border-radius: 12px;
        padding: 12px;
        color: #1e3a8a;
        font-weight: 600;
        border-left: 4px solid #48C6EF;
    }

    /* Badges */
    .badge-safe { background: #dcfce7; color: #166534; padding: 5px 15px; border-radius: 20px; font-weight: 600; font-size: 14px; }
    .badge-danger { background: #fee2e2; color: #991b1b; padding: 5px 15px; border-radius: 20px; font-weight: 600; font-size: 14px; }
    .severity-low { color: #059669; font-weight: 600; font-size: 12px; }
    .severity-high { color: #ef4444; font-weight: 600; font-size: 12px; }
    
    /* Timeline */
    .timeline-item {
        border-left: 2px solid #48C6EF;
        padding-left: 20px;
        padding-bottom: 20px;
        position: relative;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -7px;
        top: 0;
        width: 12px;
        height: 12px;
        background: #48C6EF;
        border-radius: 50%;
    }

    /* Success Animation Banner */
    .success-banner {
        background: linear-gradient(90deg, #0d9488 0%, #10b981 100%);
        color: white;
        padding: 15px 25px;
        border-radius: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        animation: fadeInDown 0.8s ease-out;
    }
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---

# --- CHECK FOR ANALYSIS ---
if 'scan_result' not in st.session_state or 'scan_image' not in st.session_state:
    st.warning("Please upload and analyze a screenshot first.")
    if st.button("Go to AI Scanner 🤖", use_container_width=True):
        st.switch_page("pages/ai_scanner.py")
    st.stop()

res = st.session_state.scan_result
img = st.session_state.scan_image

# --- TOP BAR ---
t1, t2 = st.columns([3, 1])
with t1: st.markdown("### AI Scan Result")
with t2: st.markdown("<div style='text-align:right;'>🔔 &nbsp;&nbsp; 👤</div>", unsafe_allow_html=True)

st.markdown("<p style='color:#64748b; margin-top:-15px;'>Your screenshot has been successfully analyzed by PeaceGuard AI Engines.</p>", unsafe_allow_html=True)

# --- SUCCESS BANNER ---
st.markdown(f"""
<div class="success-banner">
    <div><b>✔ Analysis Completed Successfully</b></div>
    <div style="font-size: 14px; opacity: 0.9;">Confidence: {res['confidence']}</div>
</div>
""", unsafe_allow_html=True)

# --- MAIN CONTENT LAYOUT ---
col_score, col_details = st.columns([1, 2.2], gap="large")

with col_score:
    # Uploaded Screenshot Card
    st.markdown('<div class="glass-card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("<h4 style='margin-bottom: 15px;'>Uploaded Screenshot</h4>", unsafe_allow_html=True)
    st.image(img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Digital Peace Score Card
    st.markdown('<div class="glass-card score-container">', unsafe_allow_html=True)
    circle_color = "#10b981" if res['peace_score'] >= 80 else "#ef4444"
    circle_shadow = "rgba(16, 185, 129, 0.2)" if res['peace_score'] >= 80 else "rgba(239, 68, 68, 0.2)"
    st.markdown(f"""
    <div class="circle-score" style="border-color: {circle_color}; box-shadow: 0 0 20px {circle_shadow};">
        {res['peace_score']} / 100
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<h4 style='margin:0; color:#1e3a8a;'>Digital Peace Score</h4>", unsafe_allow_html=True)
    reliability = "High Reliability" if res['peace_score'] >= 80 else "Needs Verification"
    st.markdown(f"<p style='color:#64748b; font-size:14px;'>{reliability}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Risk Level Card
    st.markdown('<div class="glass-card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("<h4>Risk Level</h4>", unsafe_allow_html=True)
    if res['risk_level'] == "Safe Content":
        st.markdown('<span class="badge-safe">🟢 Safe Content</span>', unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; color:#64748b; margin-top:15px;'>No immediate threats found.</p>", unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-danger">🔴 High Risk</span>', unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:12px; color:#c53030; margin-top:15px; font-weight: 600;'>{res['scam_type']} Identified</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_details:
    # Detected Issues
    st.markdown("#### Detected Issues")
    i1, i2 = st.columns(2)
    issues_list = res.get('issues', [])
    with i1:
        if len(issues_list) > 0:
            issue = issues_list[0]
            st.markdown(f"""<div class="glass-card" style="padding:15px;">
                <span style='font-size:20px;'>{issue['icon']}</span> <b>{issue['type']}</b>
                <p style='font-size:12px; color:#64748b;'>{issue['desc']}</p>
                <span style="font-weight:600; font-size:12px; color:{'#059669' if issue['severity'] == 'NONE' else '#ef4444'};">SEVERITY: {issue['severity']}</span>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div class="glass-card" style="padding:15px;">
                <span style='font-size:20px;'>✅</span> <b>No Issues</b>
                <p style='font-size:12px; color:#64748b;'>No risk patterns found in content.</p>
                <span class="severity-low">SEVERITY: NONE</span>
            </div>""", unsafe_allow_html=True)
    with i2:
        if len(issues_list) > 1:
            issue = issues_list[1]
            st.markdown(f"""<div class="glass-card" style="padding:15px;">
                <span style='font-size:20px;'>{issue['icon']}</span> <b>{issue['type']}</b>
                <p style='font-size:12px; color:#64748b;'>{issue['desc']}</p>
                <span style="font-weight:600; font-size:12px; color:{'#059669' if issue['severity'] == 'NONE' else '#ef4444'};">SEVERITY: {issue['severity']}</span>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div class="glass-card" style="padding:15px;">
                <span style='font-size:20px;'>✅</span> <b>No Issues</b>
                <p style='font-size:12px; color:#64748b;'>No other vulnerabilities detected.</p>
                <span class="severity-low">SEVERITY: NONE</span>
            </div>""", unsafe_allow_html=True)

    # AI Explanation
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### 🤖 AI Explanation")
    st.write(res["explanation"])
    st.markdown('</div>', unsafe_allow_html=True)

    # Red Flags Detected
    if res.get("red_flags"):
        st.markdown('<div class="glass-card" style="border-left: 5px solid #ef4444;">', unsafe_allow_html=True)
        st.markdown("#### 🚩 Red Flags Detected")
        for flag in res["red_flags"]:
            st.markdown(f"- **{flag}**")
        st.markdown('</div>', unsafe_allow_html=True)

# --- SECOND ROW ---
col_rec, col_sum = st.columns([1.5, 1], gap="large")

with col_rec:
    st.markdown("#### 🛡️ Safety Recommendations")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    for index, rec in enumerate(res["recommendations"]):
        st.checkbox(rec, value=True, disabled=True, key=f"rec_{index}")
    st.markdown('</div>', unsafe_allow_html=True)

with col_sum:
    st.markdown("#### Scan Summary")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
        <div class="timeline-item">Screenshot Uploaded</div>
        <div class="timeline-item">OCR Completed</div>
        <div class="timeline-item">AI Pattern Analysis</div>
        <div class="timeline-item">Risk Score Generated</div>
        <div class="timeline-item" style="border:none;">Safety Advice Ready</div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- RELATED AWARENESS ---
st.markdown("### Recommended Learning")
a1, a2, a3, a4 = st.columns(4)
related = ["Fake Internship Scam", "QR Code Scams", "Phishing Emails", "OTP Frauds"]
for i, title in enumerate(related):
    with [a1, a2, a3, a4][i]:
        st.markdown(f'<div class="glass-card" style="padding:15px; text-align:center;"><b>{title}</b></div>', unsafe_allow_html=True)
        if st.button("Learn More", key=f"btn_{i}"):
            st.switch_page("pages/awareness.py")

# --- ACTION BUTTONS ---
st.write("<br>", unsafe_allow_html=True)
r1_c1, r1_c2, r1_c3 = st.columns(3)
with r1_c1:
    if st.button("🔍 Scan Another", use_container_width=True):
        st.switch_page("pages/ai_scanner.py")
with r1_c2:
    if st.button("📊 View Dashboard", use_container_width=True):
        st.switch_page("pages/dashboard.py")
with r1_c3:
    if st.button("🚩 Report Scam", use_container_width=True):
        st.session_state.report_from_scan = True
        st.switch_page("pages/community.py")

r2_c1, r2_c2, r2_c3 = st.columns(3)
with r2_c1:
    report_text = f"""PeaceGuard AI Security Report
------------------------------
File: {img.name if hasattr(img, 'name') else 'Suspicious_Content.png'}
Scam Type: {res['scam_type']}
Risk Level: {res['risk_level']}
Confidence: {res['confidence']}
Digital Peace Score: {res['peace_score']}/100
AI Explanation: {res['explanation']}
"""
    st.download_button(
        label="📥 Download Report",
        data=report_text,
        file_name="PeaceGuard_AI_Scan_Report.txt",
        mime="text/plain",
        use_container_width=True
    )
with r2_c2:
    if st.button("📤 Share Result", use_container_width=True):
        st.toast("🔗 Share link copied to clipboard!")
        st.success("Result shared successfully!")
with r2_c3:
    if st.button("🏠 Go Home", use_container_width=True):
        st.switch_page("pages/home.py")

# --- FOOTER ---
st.divider()
st.markdown("""
    <div style="text-align: center; color: #64748b; padding-bottom: 20px;">
        <p style="font-weight:600; color:#1e3a8a; margin-bottom:0;">PeaceGuard AI</p>
        <p style="font-size:13px;">Protecting Digital Peace with AI • Developed by Vaishali Gangurde</p>
    </div>
""", unsafe_allow_html=True)