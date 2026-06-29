import streamlit as st
import time

# 1. Global Page Config (first Streamlit command in entrypoint)
st.set_page_config(
    page_title="PeaceGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session state initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = False
if "demo_step" not in st.session_state:
    st.session_state.demo_step = 0

# 3. Check query parameters for starting the walkthrough
if "demo" in st.query_params and st.query_params["demo"] == "start":
    st.session_state.demo_mode = True
    st.session_state.demo_step = 1
    st.session_state.logged_in = True  # Auto-login to show protected pages
    st.query_params.clear()

# Hide Streamlit header/footer (standard across pages)
st.markdown("""
<style>
header, footer, #MainMenu {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# 4. Hide sidebar if not logged in
if not st.session_state.logged_in:
    st.markdown("""
    <style>
        [data-testid="collapsedControl"] { display: none !important; }
        [data-testid="stSidebar"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# 5. Define Pages
landing_page = st.Page("pages/landing.py", title="Landing Page", icon="🛡️", default=True, url_path="")
login_page = st.Page("pages/login.py", title="Login", icon="🔒", url_path="Login")
home_page = st.Page("pages/home.py", title="Home", icon="🏠", url_path="Home")
scanner_page = st.Page("pages/ai_scanner.py", title="AI Scanner", icon="🤖", url_path="AI_Scanner")
result_page = st.Page("pages/scanner_result.py", title="Scan Result", icon="🔍", url_path="Scanner_Result")
awareness_page = st.Page("pages/awareness.py", title="Awareness Hub", icon="📚", url_path="Awareness")
community_page = st.Page("pages/community.py", title="Community Hub", icon="👥", url_path="Community")
dashboard_page = st.Page("pages/dashboard.py", title="Metrics Dashboard", icon="📊", url_path="Dashboard")
emergency_page = st.Page("pages/emergency.py", title="Emergency Help", icon="📞", url_path="Emergency")
about_page = st.Page("pages/about.py", title="About PeaceGuard", icon="ℹ️", url_path="About")

# 6. Configure navigation
if st.session_state.logged_in:
    pg = st.navigation({
        "PeaceGuard AI": [home_page, scanner_page, awareness_page, community_page, dashboard_page, emergency_page, about_page],
        "Utilities": [result_page]
    })
else:
    pg = st.navigation([landing_page, login_page])

# 7. Render sidebar elements BEFORE pg.run() (displays at top of sidebar)
if st.session_state.logged_in:
    from custom_components.logo import get_logo_html
    with st.sidebar:
        brand_html = f'''<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px; margin-left: 5px; padding-top: 10px;">
{get_logo_html("small", center=False)}
<h2 style="color:#1e3a8a; margin:0; font-family:'Poppins',sans-serif; font-size:1.5rem; font-weight:800;">PeaceGuard AI</h2>
</div>'''
        st.markdown(brand_html, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- DEMO MODE OVERLAY ---
        if st.session_state.demo_mode:
            step = st.session_state.demo_step
            steps = {
                2: {"title": "Step 2 of 7: AI Scanner", "desc": "Upload screenshots of suspicious texts, messages, or emails here to get risk ratings.", "next_page": "pages/awareness.py", "next_step": 3},
                3: {"title": "Step 3 of 7: Awareness Hub", "desc": "Interactive lessons, Myth vs Fact cards, and cyber safety quizzes to educate users.", "next_page": "pages/community.py", "next_step": 4},
                4: {"title": "Step 4 of 7: Community Hub", "desc": "Discussion board where citizens report active scams, upvote alerts, and earn badges.", "next_page": "pages/dashboard.py", "next_step": 5},
                5: {"title": "Step 5 of 7: Metrics Dashboard", "desc": "Insights on safety stats, scans completed, threat categories, and user achievements.", "next_page": "pages/emergency.py", "next_step": 6},
                6: {"title": "Step 6 of 7: Emergency Help", "desc": "Generates draft complaints for cyber cells (1930) and lists immediate recovery steps.", "next_page": "pages/about.py", "next_step": 7},
                7: {"title": "Step 7 of 7: About PeaceGuard", "desc": "Project mission, hackathon milestones, and interactive team details.", "next_page": "pages/landing.py", "next_step": 8}
            }
            if step in steps:
                curr_step = steps[step]
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #1e3a8a, #0d9488); color: white; padding: 15px; border-radius: 14px; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(30,58,138,0.25);">
                    <h4 style="margin: 0; font-size: 1.05rem; font-weight: 700; color: #e6fffa; font-family: 'Poppins', sans-serif;">🛡️ Walkthrough Active</h4>
                    <p style="margin: 5px 0 0 0; font-size: 0.82rem; font-weight: 600; color: #f0fdfa; font-family: 'Poppins', sans-serif;">{curr_step['title']}</p>
                    <p style="margin: 5px 0 0 0; font-size: 0.78rem; opacity: 0.9; line-height: 1.3; font-family: 'Poppins', sans-serif;">{curr_step['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                auto_advance = st.checkbox("Auto-advance (3s)", value=True, key=f"demo_auto_sb_{step}")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Next ➔", use_container_width=True, key=f"demo_next_sb_{step}"):
                        if curr_step['next_step'] == 8:
                            st.session_state.demo_mode = False
                            st.session_state.demo_step = 0
                            st.switch_page("pages/landing.py")
                        else:
                            st.session_state.demo_step = curr_step['next_step']
                            st.switch_page(curr_step['next_page'])
                with col2:
                    if st.button("Exit ❌", use_container_width=True, key=f"demo_exit_sb_{step}"):
                        st.session_state.demo_mode = False
                        st.session_state.demo_step = 0
                        st.rerun()
                
                st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
                
                if auto_advance:
                    time.sleep(3.0)
                    if curr_step['next_step'] == 8:
                        st.session_state.demo_mode = False
                        st.session_state.demo_step = 0
                        st.switch_page("pages/landing.py")
                    else:
                        st.session_state.demo_step = curr_step['next_step']
                        st.switch_page(curr_step['next_page'])

# 8. Run the selected page
pg.run()

# 9. Render sidebar elements AFTER pg.run() (displays at bottom of sidebar)
if st.session_state.logged_in:
    with st.sidebar:
        st.divider()
        if st.button("⚙️ Settings", use_container_width=True, key="app_settings"):
            st.toast("Settings panel coming soon!")
        if st.button("🚪 Logout", use_container_width=True, key="app_logout"):
            st.session_state.logged_in = False
            st.session_state.demo_mode = False
            st.session_state.demo_step = 0
            st.toast("Logged out successfully!")
            st.switch_page("pages/landing.py")