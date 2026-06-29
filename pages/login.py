import streamlit as st
import time
from custom_components.logo import get_logo_html

# Custom CSS for Premium Design, Glassmorphism, Background Animation, & Particles
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
/* Apply Outfit font universally */
html, body, [class*="css"], a, p, span, h1, h2, h3, h4, h5, h6, label, input {
    font-family: 'Outfit', sans-serif !important;
}
/* Background animated gradient */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.stApp {
    background: linear-gradient(-45deg, #e0f2fe, #eef9f0, #dbeafe, #f0fdf4) !important;
    background-size: 400% 400% !important;
    animation: gradientBG 15s ease infinite !important;
}
/* Hide streamlit header and footer */
[data-testid="stHeader"] {
    display: none !important;
}
footer {
    display: none !important;
}
/* Hide sidebar and collapsed sidebar controls for authentic Login screen feel */
[data-testid="collapsedControl"] {
    display: none !important;
}
[data-testid="stSidebar"] {
    display: none !important;
}
/* Adjust general spacing */
.block-container {
    padding-top: 3rem !important;
    padding-bottom: 2rem !important;
}
/* Floating particles container */
.particle-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: -1;
    pointer-events: none;
}
/* Elegant glowing floating particles */
.particle {
    position: absolute;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(14, 165, 233, 0.15), rgba(16, 185, 129, 0.15));
    animation: float 25s infinite linear;
    filter: blur(2px);
}
.p1 { width: 80px; height: 80px; left: 10%; top: 20%; animation-delay: 0s; }
.p2 { width: 120px; height: 120px; right: 15%; top: 15%; animation-delay: -5s; animation-duration: 30s; }
.p3 { width: 60px; height: 60px; left: 25%; bottom: 15%; animation-delay: -10s; }
.p4 { width: 100px; height: 100px; right: 20%; bottom: 20%; animation-delay: -15s; animation-duration: 28s; }
.p5 { width: 50px; height: 50px; left: 50%; top: 40%; animation-delay: -2s; }
@keyframes float {
    0% { transform: translateY(0) rotate(0deg) scale(1); opacity: 0.3; }
    50% { transform: translateY(-100px) rotate(180deg) scale(1.1); opacity: 0.8; }
    100% { transform: translateY(-200px) rotate(360deg) scale(1); opacity: 0; }
}
/* Glassmorphic Login Card */
.login-card {
    background: rgba(255, 255, 255, 0.45) !important;
    backdrop-filter: blur(25px) !important;
    -webkit-backdrop-filter: blur(25px) !important;
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    border-radius: 24px !important;
    padding: 35px 40px !important;
    box-shadow: 0 10px 40px 0 rgba(31, 38, 135, 0.05),
                0 4px 20px 0 rgba(34, 197, 94, 0.02) !important;
    max-width: 480px;
    margin: 0 auto;
    animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
/* Logo and Header Styling */
.logo-container {
    text-align: center;
    margin-bottom: 20px;
}
.logo-svg {
    filter: drop-shadow(0 4px 12px rgba(14, 165, 233, 0.25));
    transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.logo-container:hover .logo-svg {
    transform: rotate(360deg) scale(1.1);
}
.logo-title {
    font-size: 1.85rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #1e3b8b 0%, #0d9488 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 10px !important;
    margin-bottom: 0px !important;
    letter-spacing: -0.5px;
}
.logo-subtitle {
    font-size: 0.85rem !important;
    color: #4b5563 !important;
    margin-top: 4px !important;
    font-weight: 500;
}
/* Form Helper Row (Forgot Password alignment) */
.form-helper-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: -10px;
    margin-bottom: 15px;
}
/* Customize Streamlit Input Box wrapper */
div[data-baseweb="input"] {
    background-color: rgba(255, 255, 255, 0.7) !important;
    border: 1px solid rgba(14, 165, 233, 0.15) !important;
    border-radius: 12px !important;
    transition: all 0.3s ease !important;
}
div[data-baseweb="input"]:focus-within {
    border-color: #0ea5e9 !important;
    box-shadow: 0 0 0 4px rgba(14, 165, 233, 0.12) !important;
    background-color: #ffffff !important;
}
input {
    color: #1e293b !important;
    font-size: 0.95rem !important;
}
/* Modify checkbox label color and size */
div[data-testid="stCheckbox"] label {
    font-size: 0.85rem !important;
    color: #4b5563 !important;
    font-weight: 500 !important;
}
/* Primary Gradient Button */
.primary-btn button {
    background: linear-gradient(135deg, #0ea5e9 0%, #10b981 100%) !important;
    color: white !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-size: 0.98rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 15px rgba(14, 165, 233, 0.2) !important;
    height: 46px !important;
}
.primary-btn button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(14, 165, 233, 0.3) !important;
    background: linear-gradient(135deg, #0284c7 0%, #059669 100%) !important;
}
.primary-btn button:active {
    transform: translateY(0) !important;
}
/* Text Link Button */
.link-btn button {
    background: none !important;
    border: none !important;
    color: #0ea5e9 !important;
    text-decoration: none !important;
    font-weight: 500 !important;
    padding: 0 !important;
    font-size: 0.85rem !important;
    transition: color 0.2s ease !important;
}
.link-btn button:hover {
    color: #0284c7 !important;
    text-decoration: underline !important;
    background: none !important;
}
/* OAuth buttons styling */
.oauth-btn button {
    background-color: rgba(255, 255, 255, 0.7) !important;
    color: #334155 !important;
    border: 1px solid rgba(226, 232, 240, 0.8) !important;
    border-radius: 12px !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    padding: 10px 16px !important;
    transition: all 0.2s ease !important;
}
.oauth-btn button:hover {
    background-color: #ffffff !important;
    border-color: rgba(14, 165, 233, 0.3) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04) !important;
}
/* Divider lines for social login */
.divider {
    display: flex;
    align-items: center;
    text-align: center;
    color: #94a3b8;
    font-size: 0.8rem;
    margin: 20px 0;
    font-weight: 500;
}
.divider::before, .divider::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid rgba(226, 232, 240, 0.8);
}
.divider:not(:empty)::before {
    margin-right: .5em;
}
.divider:not(:empty)::after {
    margin-left: .5em;
}
/* Security Badge Badge */
.security-badge {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    background-color: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.15);
    border-radius: 50px;
    padding: 8px 16px;
    margin-top: 20px;
    font-size: 0.78rem;
    color: #065f46;
    font-weight: 600;
}
/* Privacy Text */
.privacy-footer {
    text-align: center;
    font-size: 0.75rem;
    color: #64748b;
    margin-top: 12px;
    line-height: 1.4;
}
/* Streamlit notifications overrides */
div[data-testid="stNotification"] {
    border-radius: 12px !important;
    background-color: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(10px) !important;
}
</style>
"""
# Inject custom styling
st.markdown(CSS, unsafe_allow_html=True)
# Inject floating particles background
st.markdown('''
<div class="particle-container">
    <div class="particle p1"></div>
    <div class="particle p2"></div>
    <div class="particle p3"></div>
    <div class="particle p4"></div>
    <div class="particle p5"></div>
</div>
''', unsafe_allow_html=True)
# Layout: center column for the login card
col_left, col_mid, col_right = st.columns([1, 2, 1])
with col_mid:
    # Card wrapper start
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    
    # Custom Header
    st.markdown(f'''<div class="logo-container">
{get_logo_html("medium", center=True)}
<h1 class="logo-title">PeaceGuard AI</h1>
<p class="logo-subtitle">Welcome Back. Secure Your Digital Peace.</p>
</div>''', unsafe_allow_html=True)
    
    # ------------------ FORM INPUTS ------------------
    email = st.text_input("Email Address", placeholder="e.g. judge@hackathon.com", key="login_email")
    
    # Show/Hide password toggle layout
    col_pass, col_show = st.columns([3.2, 0.8])
    with col_show:
        # Space alignment spacer + checkbox
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        show_password = st.checkbox("Show", value=False, key="show_pass")
        
    with col_pass:
        password = st.text_input(
            "Password", 
            type="default" if show_password else "password", 
            placeholder="••••••••",
            key="login_password"
        )
    
    # Remind me / Forgot password row
    st.markdown('<div class="form-helper-row">', unsafe_allow_html=True)
    col_rem, col_forgot = st.columns(2)
    with col_rem:
        remember = st.checkbox("Remember Me", value=True)
    with col_forgot:
        st.markdown('<div class="link-btn" style="text-align: right; margin-top: 4px;">', unsafe_allow_html=True)
        forgot_clicked = st.button("Forgot Password?", key="forgot_pwd")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    error_placeholder = st.empty()

    # Secure Login submit button
    st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
    login_clicked = st.button("Secure Login", use_container_width=True, key="login_submit")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Divider for OAuth options
    st.markdown('<div class="divider">Or Sign In with</div>', unsafe_allow_html=True)
    
    # Social OAuth login buttons
    st.markdown('<div class="oauth-btn">', unsafe_allow_html=True)
    col_google, col_ms = st.columns(2)
    with col_google:
        google_clicked = st.button("🌐 Google", use_container_width=True, key="oauth_google")
    with col_ms:
        ms_clicked = st.button("💻 Microsoft", use_container_width=True, key="oauth_ms")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Create Account Link
    st.markdown('<div style="text-align: center; margin-top: 20px;">', unsafe_allow_html=True)
    st.markdown('<span style="font-size: 0.85rem; color: #4b5563;">New to PeaceGuard? </span>', unsafe_allow_html=True)
    st.markdown('<div class="link-btn" style="display: inline-block;">', unsafe_allow_html=True)
    create_clicked = st.button("Create Account", key="create_acc_btn")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Back to Landing Page Link/Button
    st.markdown('<div style="text-align: center; margin-top: 10px;">', unsafe_allow_html=True)
    st.markdown('<div class="link-btn" style="display: inline-block;">', unsafe_allow_html=True)
    back_clicked = st.button("⬅ Back to Landing Page", key="back_to_landing")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Security indicator badge
    st.markdown('''
    <div class="security-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
        </svg>
        <span>End-to-End Encrypted Verification</span>
    </div>
    ''', unsafe_allow_html=True)
    
    # Educational notice
    st.markdown('''
    <div class="privacy-footer">
        PeaceGuard AI is an educational project.<br>
        Your credentials are secure, and not recorded in any database.
    </div>
    ''', unsafe_allow_html=True)
    
    # Card wrapper end
    st.markdown('</div>', unsafe_allow_html=True)
# ------------------ EVENT HANDLERS ------------------
if login_clicked:
    if not email:
        error_placeholder.error("⚠️ Please enter your Email Address.")
    elif "@" not in email:
        error_placeholder.error("⚠️ Please enter a valid email address.")
    elif not password:
        error_placeholder.error("⚠️ Please enter your Password.")
    else:
        st.session_state.logged_in = True
        st.session_state.user_email = email
        st.session_state.login_success_toast = True
        st.switch_page("pages/home.py")
elif google_clicked:
    st.session_state.logged_in = True
    st.session_state.user_email = "hackathon.judge@google.com"
    st.session_state.login_success_toast = True
    st.switch_page("pages/home.py")
elif ms_clicked:
    st.session_state.logged_in = True
    st.session_state.user_email = "hackathon.judge@microsoft.com"
    st.session_state.login_success_toast = True
    st.switch_page("pages/home.py")
elif forgot_clicked:
    st.info("💡 Feature coming soon!")
elif create_clicked:
    st.info("💡 Registration coming soon! You can login with any email/password details for this hackathon demo.")
elif back_clicked:
    st.switch_page("pages/landing.py")
