import streamlit as st
import random
import time

# --- PAGE CONFIG ---


# --- DIALOG POPUPS FOR SCAMS ---
@st.dialog("Scam Category Details")
def show_scam_detail(scam):
    st.markdown(f"### {scam['icon']} {scam['title']}")
    st.write(scam['desc'])
    st.markdown("---")
    st.markdown("#### 🚩 Common Red Flags")
    if scam['title'] == "Fake Internship":
        st.markdown("- Recruiter requests payments for training, registration, or hardware setup.")
        st.markdown("- Communication comes from private Gmail or Telegram accounts rather than company addresses.")
    elif scam['title'] == "UPI Fraud":
        st.markdown("- Request asks you to scan a QR code to 'receive' cash rewards.")
        st.markdown("- Request asks you to enter your secret security PIN to credit funds.")
    elif scam['title'] == "Phishing Email":
        st.markdown("- Sender email domain is slightly misspelled (e.g. support@arnazon.com).")
        st.markdown("- Prominent warnings of account lockout demanding quick password verification.")
    elif scam['title'] == "OTP Scam":
        st.markdown("- Callers claim they are bank representatives and induce panic to extract OTP codes.")
        st.markdown("- Threaten account freeze if you do not instantly provide verification SMS PINs.")
    elif scam['title'] == "Investment Scam":
        st.markdown("- Guarantees massive risk-free gains (e.g. double money in 3 days).")
        st.markdown("- Dynamic pressure to invest more to unlock accrued profits.")
    elif scam['title'] == "Fake Lottery":
        st.markdown("- Alerts claiming you won prizes or lotteries for contests you never entered.")
        st.markdown("- Requiring a processing fee or TDS bank deposit to release the prize.")
    elif scam['title'] == "Social Media Scam":
        st.markdown("- Friends sending emergency chat requests for immediate UPI cash transfers.")
        st.markdown("- Excuses explaining why they cannot call or pick up a video dial.")
    elif scam['title'] == "QR Code Scam":
        st.markdown("- Flyers in public places offering gifts by scanning a QR code.")
        st.markdown("- Code triggers an automatic UPI debit authorization flow.")
    else:
        st.markdown("- High urgency tactics, requests for passwords, pins, or payments.")
        
    st.markdown("#### 🛡️ Action Plan")
    st.markdown("1. **Stop & Verify**: Never act in panic. Contact the official customer helpline directly.")
    st.markdown("2. **Block & Report**: Report the number or email to portal (e.g. 1930) and block them.")

@st.dialog("Full Study Guide")
def show_guide(topic):
    st.markdown(f"### 📖 Full Guide: {topic}")
    if topic == "Phishing":
        st.markdown("""
**Overview:** Phishing is the practice of sending fraudulent communications that appear to come from a reputable source.

**How it works:**
1. **Baiting:** You receive an email or SMS threatening that your bank account is locked.
2. **Link redirection:** You click a shortened link (`bit.ly`) leading to a copycat login portal.
3. **Harvesting:** Once you input your passcode, the attacker captures it and steals account control.

**Defense Strategy:**
* Never click login link alerts. Use manual URL navigation.
* Verify the SSL certificate and check domain registration dates.
""")
    elif topic == "QR Scams":
        st.markdown("""
**Overview:** Scammers leverage QR codes to execute unauthorized withdrawals.

**How it works:**
1. **Misdirection:** You sell an item online. The buyer sends a QR code claiming it is to transfer you the payment.
2. **Execution:** Scanning it opens a payment app prompting for your security PIN.
3. **Loss:** Entering the PIN authorizes a *debit* transaction.

**Defense Strategy:**
* Never scan a QR code to *receive* money.
* Carefully read the transaction amount window in your UPI app before entering your PIN.
""")
    else: # Fake News
        st.markdown("""
**Overview:** Fabricated information presented as news to mislead or manipulate readers.

**How it works:**
1. **Sensationalism:** Eye-catching headlines designed to trigger strong emotional responses (anger, fear).
2. **Lack of source:** Missing references, outdated dates, or quotes from unverified experts.

**Defense Strategy:**
* Search the headline on verified news networks.
* Use fact-checking websites like AltNews or PIB Fact Check.
""")

# --- INITIALIZE SESSION STATE ---
if 'tip_index' not in st.session_state:
    st.session_state.tip_index = 0
if 'game_index' not in st.session_state:
    st.session_state.game_index = 0
if 'pledged' not in st.session_state:
    st.session_state.pledged = False

# --- CUSTOM CSS (Branding & Glassmorphism) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f0f9ff 0%, #e6fffa 100%);
        color: #1e293b;
    }

    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08);
    }

    /* Headings */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #1e3a8a, #0d9488);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    .section-header {
        color: #1e3a8a;
        font-weight: 700;
        margin-top: 40px;
        margin-bottom: 20px;
        border-left: 5px solid #48C6EF;
        padding-left: 15px;
    }

    /* Buttons */
    .stButton>button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
        border: none;
    }
    .primary-btn button {
        background: linear-gradient(90deg, #48C6EF 0%, #6F86D6 100%);
        color: white;
    }
    
    /* Myth vs Fact Colors */
    .myth-box { background: #fee2e2; color: #991b1b; padding: 15px; border-radius: 15px; font-weight: 600; margin-bottom: 10px; }
    .fact-box { background: #dcfce7; color: #166534; padding: 15px; border-radius: 15px; font-weight: 600; }

    /* Nav Sidebar */
    [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.8); }
    .nav-item-active {
        background: linear-gradient(90deg, rgba(72,198,239,0.2), rgba(111,134,214,0.2));
        border-radius: 12px;
        padding: 12px;
        color: #1e3a8a;
        font-weight: 600;
        border-left: 4px solid #48C6EF;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---


# --- HEADER SECTION ---
st.markdown('<h1 class="hero-title">PeaceGuard Learning Hub 🎓</h1>', unsafe_allow_html=True)
st.markdown("<p style='font-size:1.2rem; color:#64748b;'>Empower yourself with interactive lessons, quizzes, and practical cyber safety tips to stay protected in the digital age.</p>", unsafe_allow_html=True)

# --- SECTION 1: DAILY CYBER SAFETY TIP ---
st.markdown('<h3 class="section-header">💡 Daily Cyber Safety Tip</h3>', unsafe_allow_html=True)
tips = [
    "Never share your OTP, Password, or Banking PIN with anyone, even if they claim to be from your bank.",
    "Always check the website URL for a 'HTTPS' and verify the domain name spelling before entering credentials.",
    "Be wary of 'Too Good to be True' offers. If you didn't enter a lottery, you didn't win one!",
    "Use a unique and complex password for every account. Consider using a trusted Password Manager.",
    "Enable Two-Factor Authentication (2FA) on all social media and banking apps for an extra layer of peace."
]

tip_col1, tip_col2 = st.columns([4, 1])
with tip_col1:
    st.markdown(f"""
    <div class="glass-card" style="display:flex; align-items:center; gap:20px;">
        <div style="font-size:50px;">🛡️</div>
        <div>
            <h4 style="margin:0; color:#0d9488;">Pro Tip of the Day</h4>
            <p style="font-size:1.1rem; margin-top:5px;">{tips[st.session_state.tip_index]}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
with tip_col2:
    if st.button("🔄 Refresh Tip", use_container_width=True):
        st.session_state.tip_index = (st.session_state.tip_index + 1) % len(tips)
        st.rerun()

# --- SECTION 2: SCAM CATEGORIES ---
st.markdown('<h3 class="section-header">🔍 Explore Scam Categories</h3>', unsafe_allow_html=True)
scams = [
    {"icon": "🎓", "title": "Fake Internship", "desc": "Scammers offer high-paying remote roles but ask for security deposits or laptop 'processing' fees."},
    {"icon": "💸", "title": "UPI Fraud", "desc": "Fraudsters send 'Collect Requests' or QR codes claiming you'll receive money, but it actually deducts from you."},
    {"icon": "📧", "title": "Phishing Email", "desc": "Emails disguised as official alerts from Google, Banks, or Amazon to steal your login credentials."},
    {"icon": "📱", "title": "OTP Scam", "desc": "Social engineering tricks where callers induce panic to make you reveal your one-time passwords."},
    {"icon": "📈", "title": "Investment Scam", "desc": "Promises of doubling your money in days via crypto or 'secret' stock trading apps."},
    {"icon": "🎁", "title": "Fake Lottery", "desc": "Congratulatory messages for contests you never entered, asking for 'tax' or 'transfer' fees."},
    {"icon": "🤳", "title": "Social Media Scam", "desc": "Fake profiles of friends asking for urgent money due to a medical emergency or stuck at an airport."},
    {"icon": "🖼️", "title": "QR Code Scam", "desc": "Static QR codes in public places or sent via chat that lead to malicious payment gateways or malware."}
]

cols = st.columns(4)
for i, scam in enumerate(scams):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="glass-card" style="height:250px; text-align:center;">
            <div style="font-size:40px; margin-bottom:10px;">{scam['icon']}</div>
            <h5 style="color:#1e3a8a; margin-bottom:10px;">{scam['title']}</h5>
            <p style="font-size:0.85rem; color:#64748b;">{scam['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Learn More", key=f"learn_{i}", use_container_width=True):
            show_scam_detail(scam)

# --- SECTION 3: MYTH VS FACT ---
st.markdown('<h3 class="section-header">🤔 Myth vs. Fact</h3>', unsafe_allow_html=True)
myths = [
    ("Banks ask for OTP to verify your account.", "Banks NEVER ask for OTP, PIN, or CVV over calls, SMS, or emails."),
    ("Public Wi-Fi is safe for banking if the site has HTTPS.", "Hackers can 'sniff' data on public Wi-Fi. Always use a VPN or mobile data for finance."),
    ("If a caller knows my name and DOB, they are official.", "Scammers buy leaked data. Personal info is no longer a guarantee of identity."),
    ("Antivirus makes my phone 100% unhackable.", "Human error is the biggest leak. No software can stop you from giving away your own OTP."),
    ("Only elderly people fall for cyber scams.", "Students and tech-savvy youth are the primary targets for fake job and crypto scams."),
    ("Locking my profile makes me invisible to scammers.", "Scammers use social engineering and mutual friend lists to reach you regardless.")
]

m_cols = st.columns(3)
for i, (m, f) in enumerate(myths):
    with m_cols[i % 3]:
        st.markdown(f"""
        <div class="glass-card">
            <div class="myth-box">❌ Myth: {m}</div>
            <div class="fact-box">✅ Fact: {f}</div>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION: QR CODE SAFETY TIPS ---
st.markdown('<h3 class="section-header">🖼️ QR Code Safety Tips</h3>', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card" style="background: rgba(255, 255, 255, 0.65);">
    <h4 style="color:#0d9488; margin-top:0;">Protect Yourself from Quishing (QR Phishing)</h4>
    <p style="font-size:0.95rem; color:#475569; line-height:1.6;">
        QR codes are incredibly convenient, but they are also blind links. Since humans cannot read QR codes directly, scammers use them to mask malicious URLs and bypass security filters. Follow these original rules to stay safe:
    </p>
    <ul style="font-size:0.95rem; color:#475569; line-height:1.6; margin-left: 15px;">
        <li><b>Check the physical code:</b> Ensure QR codes on public posters, flyers, or parking meters haven't been pasted over with stickers.</li>
        <li><b>Preview URLs:</b> Use a QR scanner app that displays the target domain name before opening the site in your browser.</li>
        <li><b>Beware of payments:</b> Remember that you <i>never</i> need to scan a QR code to receive a payment. A QR scan is strictly for initiating a debit.</li>
        <li><b>Avoid sensitive login:</b> Never enter passwords or credit card details on websites reached via scanned QR codes. Navigate to official portals manually.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- SECTION 4: CAN YOU SPOT THE SCAM? (GAME) ---
st.markdown('<h3 class="section-header">🎯 Interactive: Can You Spot The Scam?</h3>', unsafe_allow_html=True)
game_scenarios = [
    {"msg": "Hi! I am HR from Amazon. Your resume is selected for a Part-time role (₹5000/day). Click to join WhatsApp: wa.link/hr-amazon", "type": "Scam", "reason": "Big brands don't recruit via random WhatsApp links with high daily pay."},
    {"msg": "Google Alert: A new sign-in was detected on your account from Russia. If this wasn't you, check activity here: google.security-auth.com", "type": "Scam", "reason": "The URL 'security-auth.com' is not 'google.com'. This is a Phishing link."},
    {"msg": "Your electricity bill for the month of June is ₹1,420. Please pay by the 10th to avoid late fees. Pay at: bill.utility.gov.in", "type": "Safe", "reason": "Official government domains (.gov.in) and realistic amounts are generally safe."},
    {"msg": "Congrats! You won a ₹500 Amazon Gift Voucher from your company's HR portal. Claim it via your official Employee Dashboard.", "type": "Safe", "reason": "Redirecting to an internal company portal is a standard secure practice."},
    {"msg": "URGENT: Your Bank Account will be blocked in 2 hours due to KYC pending. Update immediately to avoid penalty: bit.ly/bank-kyc-now", "type": "Scam", "reason": "Banks never use 'bit.ly' short-links for KYC and never create '2-hour' panic."}
]

curr = game_scenarios[st.session_state.game_index]
st.markdown(f"""
<div class="glass-card" style="background:#f8fafc; border: 2px dashed #48C6EF; text-align:center;">
    <p style="font-size:0.9rem; color:#64748b;">Analyze the message below:</p>
    <div style="background:white; padding:20px; border-radius:15px; margin:20px auto; max-width:600px; box-shadow:0 4px 12px rgba(0,0,0,0.05);">
        <i>"{curr['msg']}"</i>
    </div>
</div>
""", unsafe_allow_html=True)

g_c1, g_c2, g_c3 = st.columns([1, 1, 1])
with g_c1:
    if st.button("🟢 Safe", use_container_width=True):
        if curr['type'] == "Safe": st.success(f"Correct! {curr['reason']}")
        else: st.error(f"Incorrect. {curr['reason']}")
with g_c2:
    if st.button("🔴 Scam", use_container_width=True):
        if curr['type'] == "Scam": st.success(f"Correct! {curr['reason']}")
        else: st.error(f"Incorrect. {curr['reason']}")
with g_c3:
    if st.button("Next Case ➡️", use_container_width=True):
        st.session_state.game_index = (st.session_state.game_index + 1) % len(game_scenarios)
        st.rerun()

# --- SECTION 5 & 6: CHECKLIST & QUICK LEARNING ---
c_left, c_right = st.columns([1, 1.2], gap="large")

with c_left:
    st.markdown('<h3 class="section-header">✅ Safety Checklist</h3>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.checkbox("Verify website URL for HTTPS & spelling")
    st.checkbox("Never share OTP with anyone on call")
    st.checkbox("Enable 2-Factor Authentication (2FA)")
    st.checkbox("Verify job offers on official LinkedIn/Portals")
    st.checkbox("Check email sender address carefully")
    st.checkbox("Report suspicious messages to 1930")
    st.markdown('</div>', unsafe_allow_html=True)

with c_right:
    st.markdown('<h3 class="section-header">⚡ Quick Learning</h3>', unsafe_allow_html=True)
    quick_topics = [
        ("Phishing", "Look for urgent tone and misspelled URLs."),
        ("QR Scams", "QR codes are for SENDING money, not RECEIVING."),
        ("Fake News", "Check source via Google News or Fact-checkers.")
    ]
    for top, des in quick_topics:
        with st.expander(f"📖 {top}"):
            st.write(des)
            if st.button(f"Read Full Guide on {top}", key=f"guide_{top}"):
                show_guide(top)

# --- SECTION 7: DIGITAL PEACE QUIZ ---
st.markdown('<h3 class="section-header">📝 Digital Peace Quiz</h3>', unsafe_allow_html=True)

# Initialize Session State for Quiz
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'quiz_page' not in st.session_state:
    st.session_state.quiz_page = 0
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}

with st.container():
    st.markdown('<div class="glass-card" style="padding: 25px;">', unsafe_allow_html=True)
    
    if not st.session_state.quiz_started and 'quiz_finished' not in st.session_state:
        st.write("Ready to test your Digital Peace vigilance? Take our interactive quiz!")
        if st.button("🚀 Start Quiz", use_container_width=True):
            st.session_state.quiz_started = True
            st.session_state.quiz_page = 0
            st.session_state.quiz_answers = {}
            st.rerun()
    elif st.session_state.quiz_started:
        questions = [
            {
                "q": "1. What should you do if you get a call asking for an OTP to 'unblock' your card?",
                "opts": ["Give it to them", "Hang up and call the official bank number", "Ask them for their ID first"],
                "correct": "Hang up and call the official bank number"
            },
            {
                "q": "2. A friend sends a link for 'Free ₹500 Recharge'. You should:",
                "opts": ["Click and share with 10 friends", "Check the official service provider app", "Ignore and delete"],
                "correct": "Check the official service provider app"
            }
        ]
        
        idx = st.session_state.quiz_page
        curr_q = questions[idx]
        
        # Save previous value if selected
        prev_ans = st.session_state.quiz_answers.get(idx, None)
        selected_index = curr_q["opts"].index(prev_ans) if prev_ans in curr_q["opts"] else 0
        
        ans = st.radio(curr_q["q"], curr_q["opts"], index=selected_index)
        st.session_state.quiz_answers[idx] = ans
        
        st.write("")
        c_prev, c_next = st.columns(2)
        with c_prev:
            if st.button("⬅ Previous Question", disabled=(idx == 0), use_container_width=True):
                st.session_state.quiz_page -= 1
                st.rerun()
        with c_next:
            if idx < len(questions) - 1:
                if st.button("Next Question ➔", use_container_width=True):
                    st.session_state.quiz_page += 1
                    st.rerun()
            else:
                if st.button("🏁 Finish Quiz", use_container_width=True):
                    score = 0
                    for k, q in enumerate(questions):
                        if st.session_state.quiz_answers.get(k) == q["correct"]:
                            score += 50
                    
                    st.session_state.quiz_score = score
                    st.session_state.quiz_finished = True
                    st.session_state.quiz_started = False
                    st.rerun()
                    
    # Display results if finished
    if 'quiz_finished' in st.session_state and st.session_state.quiz_finished:
        score = st.session_state.quiz_score
        st.markdown(f"#### Your Vigilance Score: **{score}/100**")
        if score == 100:
            st.balloons()
            st.success("🏆 Excellent! You are a certified Digital Peace Guardian! 🛡️")
        elif score == 50:
            st.warning("⚠️ Good! But you need to stay more vigilant. Be careful with links!")
        else:
            st.error("❌ Needs Improvement. Explore the Hub topics to build your cyber awareness.")
            
        if st.button("🔄 Retake Quiz", use_container_width=True):
            del st.session_state.quiz_finished
            st.session_state.quiz_started = False
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 8: SAFETY PLEDGE ---
st.markdown('<h3 class="section-header">🤝 The PeaceGuard Pledge</h3>', unsafe_allow_html=True)
st.markdown(f"""
<div class="glass-card" style="text-align:center; background: linear-gradient(135deg, #e0f2f1 0%, #ffffff 100%);">
    <h2 style="color:#0d9488;">"I pledge to think before I click, verify before I trust, and help create a safer digital world for everyone."</h2>
</div>
""", unsafe_allow_html=True)
if not st.session_state.pledged:
    if st.button("✋ I Take the Pledge", use_container_width=True):
        st.session_state.pledged = True
        st.balloons()
        st.rerun()
else:
    st.success("✅ Thank you for being a responsible Digital Citizen!")

# --- SECTION 9: ACTIONS ---
st.write("<br>", unsafe_allow_html=True)
a1, a2, a3 = st.columns(3)
with a1:
    if st.button("🤖 Analyze Screenshot", use_container_width=True, key="action_scanner"):
        st.switch_page("pages/ai_scanner.py")
with a2:
    if st.button("🚩 Report a Scam", use_container_width=True, key="action_report"):
        st.switch_page("pages/community.py")
with a3:
    if st.button("📊 Visit Dashboard", use_container_width=True, key="action_dashboard"):
        st.switch_page("pages/dashboard.py")

# --- FOOTER ---
st.divider()
st.markdown("""
<div style="text-align: center; color: #64748b; padding-bottom: 30px;">
    <h4 style="color:#1e3a8a; margin-bottom:5px;">PeaceGuard AI</h4>
    <p>Building a Safer Digital World with AI • Developed by Vaishali Gangurde</p>
    <div style="font-size: 20px; gap: 15px; display: flex; justify-content: center;">
        🌐 📧 🐙 🐦
    </div>
</div>
""", unsafe_allow_html=True)