import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIG ---


# --- CUSTOM CSS (Glassmorphism & Branding) ---
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
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
    }
    .nav-item-active {
        background: linear-gradient(90deg, rgba(72,198,239,0.2), rgba(111,134,214,0.2));
        border-radius: 12px;
        padding: 12px;
        color: #1e3a8a;
        font-weight: 600;
        border-left: 4px solid #48C6EF;
        margin-bottom: 8px;
    }

    /* Premium Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 24px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
    }

    /* Typography */
    .dashboard-title { font-size: 2.2rem; font-weight: 700; color: #1e3a8a; margin-bottom: 5px; }
    .dashboard-subtitle { color: #64748b; font-size: 1.1rem; margin-bottom: 30px; }
    
    /* Stats Styling */
    .stat-val { font-size: 1.8rem; font-weight: 700; color: #1e3a8a; margin-top: 5px; }
    .stat-label { font-size: 0.9rem; color: #64748b; }
    .stat-icon { font-size: 2rem; margin-bottom: 10px; }

    /* Badge Style */
    .badge-container { display: flex; flex-wrap: wrap; gap: 15px; }
    .badge-item {
        background: white;
        padding: 15px;
        border-radius: 18px;
        text-align: center;
        width: 120px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        border: 1px solid #f1f5f9;
    }
    .badge-icon { font-size: 30px; margin-bottom: 5px; }
    .badge-text { font-size: 11px; font-weight: 600; color: #475569; line-height: 1.2; }

    /* Progress Styling */
    .stProgress > div > div > div > div { background-color: #48C6EF; }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---

# --- TOP BAR ---
t1, t2 = st.columns([3, 1])
with t1:
    st.markdown("### Good Morning, User 👋")
with t2:
    st.markdown("""
        <div style="display: flex; justify-content: flex-end; gap: 15px; align-items: center;">
            <div style="background:white; padding:8px 12px; border-radius:10px; border:1px solid #e2e8f0; font-size:14px; width:200px;">🔍 Search analytics...</div>
            <span>🔔</span>
            <div style="width: 35px; height: 35px; background: #6F86D6; border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">U</div>
        </div>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<h1 class="dashboard-title">Analytics Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">Monitor your digital safety journey and AI analysis insights.</p>', unsafe_allow_html=True)

col_dash_btn1, col_dash_btn2 = st.columns([1, 1])
with col_dash_btn1:
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.toast("Refreshing analytics data...")
        st.rerun()
with col_dash_btn2:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/home.py")
st.write("")

# --- SECTION 1 & 2: PEACE SCORE & STATS ---
col_score, col_stats = st.columns([1, 2], gap="large")

with col_score:
    st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown("<h4 style='color:#1e3a8a; margin-bottom:20px;'>Digital Peace Score</h4>", unsafe_allow_html=True)
    
    # Gauge Chart for Score
    fig_score = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 91,
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#1e3a8a"},
            'bar': {'color': "#10b981"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#e2e8f0",
            'steps': [
                {'range': [0, 50], 'color': '#fee2e2'},
                {'range': [50, 80], 'color': '#fef3c7'},
                {'range': [80, 100], 'color': '#dcfce7'}],
        }
    ))
    fig_score.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=250, margin=dict(l=20, r=20, t=30, b=0))
    st.plotly_chart(fig_score, use_container_width=True)
    
    st.markdown("<h3 style='color:#10b981; margin:0;'>Excellent</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; font-size:14px;'>You are 12% safer than last week!</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_stats:
    s1, s2, s3 = st.columns(3)
    s4, s5, s6 = st.columns(3)
    
    stats_data = [
        {"icon": "🔍", "label": "Total Scans", "val": "1,284", "desc": "Lifetime scans"},
        {"icon": "🛡️", "label": "Safe Messages", "val": "1,102", "desc": "Verified clean"},
        {"icon": "🚫", "label": "High Risk", "val": "42", "desc": "Threats blocked"},
        {"icon": "⚠️", "label": "Medium Risk", "val": "140", "desc": "Warnings issued"},
        {"icon": "📖", "label": "Lessons", "val": "15", "desc": "Hub completion"},
        {"icon": "📢", "label": "Reports", "val": "08", "desc": "Community help"}
    ]
    
    cols = [s1, s2, s3, s4, s5, s6]
    for i, item in enumerate(stats_data):
        with cols[i]:
            st.markdown(f"""
            <div class="glass-card" style="padding: 20px;">
                <div class="stat-icon">{item['icon']}</div>
                <div class="stat-label">{item['label']}</div>
                <div class="stat-val">{item['val']}</div>
                <div style="font-size: 11px; color: #94a3b8; margin-top:5px;">{item['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

# --- SECTION 3 & 4: CHARTS ---
st.write("<br>", unsafe_allow_html=True)
c_line, c_pie = st.columns([1.5, 1], gap="large")

with c_line:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### Weekly Scan Activity")
    df_line = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Scans": [45, 52, 38, 65, 48, 25, 30]
    })
    fig_line = px.line(df_line, x="Day", y="Scans", markers=True)
    fig_line.update_traces(line_color='#48C6EF', line_width=4, marker=dict(size=10, color="#6F86D6"))
    fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis_title=None, yaxis_title=None, height=350)
    st.plotly_chart(fig_line, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c_pie:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### Threat Distribution")
    df_pie = pd.DataFrame({
        "Category": ["Safe", "Scam", "Phishing", "QR Fraud", "Fake Job", "Misinfo"],
        "Values": [80, 5, 4, 3, 5, 3]
    })
    fig_pie = px.pie(df_pie, values='Values', names='Category', hole=.6,
                     color_discrete_sequence=['#10b981', '#f43f5e', '#fbbf24', '#8b5cf6', '#3b82f6', '#64748b'])
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', height=350, showlegend=True, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 5: RECENT SCAN HISTORY ---
st.markdown("#### Recent Scan History")
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
risk_filter = st.multiselect("Filter by Risk Level", ["Safe", "Medium Risk", "High Risk"], default=["Safe", "Medium Risk", "High Risk"])

history_data = [
    {"Date": "2024-06-25", "Category": "Fake Internship", "Risk": "High Risk", "Status": "Blocked ❌"},
    {"Date": "2024-06-24", "Category": "Official Banking", "Risk": "Safe", "Status": "Verified ✅"},
    {"Date": "2024-06-24", "Category": "QR Payment", "Risk": "Medium Risk", "Status": "Flagged ⚠️"},
    {"Date": "2024-06-23", "Category": "Amazon Refund", "Risk": "High Risk", "Status": "Blocked ❌"},
    {"Date": "2024-06-22", "Category": "Friend Request", "Risk": "Safe", "Status": "Verified ✅"},
]
df_hist = pd.DataFrame(history_data)
filtered_df = df_hist[df_hist['Risk'].isin(risk_filter)]
st.table(filtered_df)
if st.button("🔍 View History Details", use_container_width=True):
    st.info("🕒 Detailed Scan Log:\n- 25 Jun: Scam identified as Part-time task fraud. Reported to community.\n- 24 Jun: Transaction request verified as HDFC official portal.\n- 24 Jun: QR code flagged for unknown redirection.")
st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 6 & 7: ACHIEVEMENTS & PROGRESS ---
st.write("<br>", unsafe_allow_html=True)
col_ach, col_prog = st.columns([1, 1], gap="large")

with col_ach:
    st.markdown("#### 🏆 Achievements")
    st.markdown('<div class="glass-card badge-container">', unsafe_allow_html=True)
    badges = [
        {"icon": "🛡️", "name": "Peace Ambassador"},
        {"icon": "✅", "name": "100 Safe Decisions"},
        {"icon": "🕵️", "name": "Scam Hunter"},
        {"icon": "🎓", "name": "Awareness Champ"},
        {"icon": "🚀", "name": "First Scan"},
        {"icon": "🤝", "name": "Community Helper"}
    ]
    for b in badges:
        st.markdown(f"""
        <div class="badge-item">
            <div class="badge-icon">{b['icon']}</div>
            <div class="badge-text">{b['name']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_prog:
    st.markdown("#### 📈 Learning Progress")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("Cyber Safety Learning")
    st.progress(0.80)
    st.write("<br>Quiz Completion", unsafe_allow_html=True)
    st.progress(0.65)
    st.write("<br>Awareness Goals", unsafe_allow_html=True)
    st.progress(0.90)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 8 & 10: INSIGHT & GOALS ---
st.write("<br>", unsafe_allow_html=True)
col_insight, col_goals = st.columns([1.5, 1], gap="large")

with col_insight:
    st.markdown('<div class="glass-card" style="background: linear-gradient(135deg, #e0f2f1 0%, #ffffff 100%);">', unsafe_allow_html=True)
    st.markdown("#### 💡 Today's Cyber Insight")
    st.markdown("""
        <p style='font-size: 1.2rem; font-style: italic; color: #0d9488;'>
        "Attackers often create a sense of urgency to bypass your critical thinking. Taking just a few seconds to verify a message can prevent 99% of digital fraud."
        </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_goals:
    st.markdown("#### 🎯 Monthly Goals")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.checkbox("Complete 10 AI Scans", value=True)
    st.checkbox("Finish Awareness Quiz", value=False)
    st.checkbox("Read 5 Learning Cards", value=True)
    st.checkbox("Report Suspicious Content", value=False)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 9: QUICK ACTIONS ---
st.markdown("#### Quick Actions")
qa1, qa2, qa3, qa4, qa5 = st.columns(5)
qa_items = [
    {"icon": "📸", "label": "Analyze Screenshot", "page": "pages/ai_scanner.py"},
    {"icon": "📚", "label": "Awareness Hub", "page": "pages/awareness.py"},
    {"icon": "👥", "label": "Community Hub", "page": "pages/community.py"},
    {"icon": "📞", "label": "Emergency Help", "page": "pages/emergency.py"},
    {"icon": "📥", "label": "Download Report", "page": "pages/dashboard.py"}
]
cols_qa = [qa1, qa2, qa3, qa4, qa5]
for i, item in enumerate(qa_items):
    with cols_qa[i]:
        if i == 4:
            csv_data = "Date,Category,Risk,Status\n2024-06-25,Fake Internship,High Risk,Blocked\n2024-06-24,Official Banking,Safe,Verified\n2024-06-24,QR Payment,Medium Risk,Flagged\n2024-06-23,Amazon Refund,High Risk,Blocked\n2024-06-22,Friend Request,Safe,Verified"
            st.download_button(
                label="📥 Export Report",
                data=csv_data,
                file_name="PeaceGuard_AI_Scan_History.csv",
                mime="text/csv",
                key="qa_download_report",
                use_container_width=True
            )
        else:
            if st.button(f"{item['icon']} {item['label']}", key=f"qa_{i}", use_container_width=True):
                st.toast(f"Navigating to {item['label']}...")
                st.switch_page(item['page'])

# --- FOOTER ---
st.write("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style="text-align: center; color: #64748b; padding-bottom: 20px;">
    <h4 style="color:#1e3a8a; margin-bottom:5px;">PeaceGuard AI</h4>
    <p style="margin-bottom:5px;">Protecting Digital Peace with Artificial Intelligence</p>
    <p style="font-size:12px;">Developed by Vaishali Gangurde • © 2024 PeaceGuard Team</p>
</div>
""", unsafe_allow_html=True)