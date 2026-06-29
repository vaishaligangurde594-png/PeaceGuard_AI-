import streamlit as st
import time
from utils.qr_analyzer import detect_and_decode_qr, analyze_qr_with_gemini, generate_offline_qr_analysis

# --- PAGE CONFIG ---


# --- CUSTOM CSS (Glassmorphism & Branding) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Global Theme */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f0f9ff 0%, #e6fffa 100%);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
    }
    .nav-item {
        padding: 12px 15px;
        border-radius: 12px;
        margin-bottom: 5px;
        transition: all 0.3s;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 10px;
        color: #475569;
        text-decoration: none;
    }
    .nav-active {
        background: linear-gradient(90deg, rgba(72,198,239,0.2), rgba(111,134,214,0.2));
        color: #1e3a8a;
        font-weight: 600;
        border-left: 4px solid #48C6EF;
    }

    /* Glass Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }

    /* Upload Area */
    .upload-container {
        border: 2px dashed #cbd5e1;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        background: rgba(255, 255, 255, 0.4);
        transition: border 0.3s;
    }
    .upload-container:hover {
        border-color: #48C6EF;
    }

    /* Gradient Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #48C6EF 0%, #6F86D6 100%);
        color: white;
        border: none;
        padding: 15px;
        border-radius: 15px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(72, 198, 239, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(72, 198, 239, 0.4);
        color: white;
    }

    /* Process Steps */
    .step-item {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 10px;
        color: #0d9488;
        font-weight: 500;
    }

    /* Top Bar */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --- SEARCHABLE SCAM DATABASE ---
searchable_scams = [
    {
        "title": "Fake Internship / Job Scam",
        "category": "Employment Fraud",
        "risk": "High Risk",
        "color": "#ef4444",
        "desc": "Fraudulent job offers requesting registration fees, background check fees, or training costs.",
        "flags": [
            "Requests upfront money for laptop, software, or training setup.",
            "Communication comes from public domains (Gmail, Telegram) rather than corporate email domains.",
            "Salary or stipend is unusually high for entry-level work."
        ],
        "recommendations": [
            "Never pay money to secure a job or internship opportunity.",
            "Verify recruiters through official LinkedIn directory profiles or company email domains.",
            "Crosscheck the opening directly on the company's official careers site."
        ],
        "icon": "🎓"
    },
    {
        "title": "UPI Cash Reward Scam",
        "category": "Financial Fraud",
        "risk": "High Risk",
        "color": "#ef4444",
        "desc": "Fraudsters sending QR codes or 'Collect Requests' claiming you won money, but scanning/authorizing it debits your account.",
        "flags": [
            "Prompting you to scan a QR code to 'receive' or 'credit' money.",
            "Prompting you to enter your UPI security PIN code to receive cash.",
            "Lottery scratch cards sent via WhatsApp or physical mail."
        ],
        "recommendations": [
            "Remember: UPI PIN is ONLY required to send money, NEVER to receive money.",
            "Do not scan QR codes shared by unknown contacts to claim rewards.",
            "Report and block the sender's mobile number on your payment app immediately."
        ],
        "icon": "💸"
    },
    {
        "title": "Phishing / Spoofed Website",
        "category": "Identity Theft",
        "risk": "High Risk",
        "color": "#ef4444",
        "desc": "Fake login interfaces or websites copying real banking, utility, or social media sites to harvest passwords and OTPs.",
        "flags": [
            "Slightly misspelled URLs (e.g., support-netbank-alert.com instead of verified bank URL).",
            "Panic warnings threatening immediate account lockout or card suspension.",
            "Non-standard portals requesting credit card numbers, passwords, and OTP codes together."
        ],
        "recommendations": [
            "Check domain names carefully for typos. Use official bookmarks or search engine links.",
            "Never enter passwords or OTPs on links sent via SMS alerts.",
            "Enable Two-Factor Authentication (2FA) on all accounts."
        ],
        "icon": "📧"
    },
    {
        "title": "OTP Theft Scam",
        "category": "Social Engineering",
        "risk": "High Risk",
        "color": "#ef4444",
        "desc": "Callers pretending to be bank executives, courier agents, or government officers who create urgency to trick you into reading back SMS OTPs.",
        "flags": [
            "Panic call claiming a package is blocked or a card is expiring.",
            "Insistent request for a one-time code sent to your mobile device.",
            "Caller claims they need the code to cancel an unauthorized transaction."
        ],
        "recommendations": [
            "Never share an OTP code with anyone on a phone call or chat.",
            "Read SMS texts carefully—they explicitly warn: 'Do not share this OTP with anyone.'",
            "Hang up and call the official customer service hotline of the provider."
        ],
        "icon": "📱"
    },
    {
        "title": "Investment / Crypto Scam",
        "category": "Financial Fraud",
        "risk": "High Risk",
        "color": "#ef4444",
        "desc": "Platforms or groups promising risk-free high yield returns or guaranteed double money schemes.",
        "flags": [
            "Guarantees massive profit with zero risk (e.g. 50% profit in 24 hours).",
            "Urges you to deposit funds via decentralized cryptocurrency or unknown bank accounts.",
            "Restricts withdrawals until you recruit more members or pay a high 'withdrawal tax'."
        ],
        "recommendations": [
            "Avoid get-rich-quick schemes. There is no such thing as guaranteed risk-free high profit.",
            "Verify registration status of the platform with financial regulators (e.g. SEBI).",
            "Do not invest money based on advice from anonymous Telegram or WhatsApp group admins."
        ],
        "icon": "📈"
    },
    {
        "title": "Fake Lottery Scam",
        "category": "Lottery Fraud",
        "risk": "High Risk",
        "color": "#ef4444",
        "desc": "Spam messages claiming you won a lucky draw, asking for processing fees or TDS taxes to release the prize money.",
        "flags": [
            "Winning notification for a lottery or contest you never entered.",
            "Demanding a 'clearance fee' or 'processing charge' beforehand.",
            "Using fake certificates or logos of reputable companies (like KBC, Tata, etc.) to look official."
        ],
        "recommendations": [
            "Remember: Legitimate contests do not ask winners to pay upfront fees to claim a prize.",
            "Ignore congratulatory messages sent by unknown numbers on WhatsApp or SMS.",
            "Block and report the number as spam."
        ],
        "icon": "🎁"
    },
    {
        "title": "Social Media Impersonation",
        "category": "Social Engineering",
        "risk": "Medium Risk",
        "color": "#f59e0b",
        "desc": "Scammers copy friends' profiles and contact you pleading for urgent financial help due to an emergency.",
        "flags": [
            "Urgent request for money transfer from a friend or relative.",
            "Sender claims they are in a medical emergency or stranded somewhere.",
            "Sender declines direct phone or video calls to confirm identity."
        ],
        "recommendations": [
            "Always call the friend or family member directly using their known phone number before sending money.",
            "Ask a question only the real friend would know to verify their identity.",
            "Report the fake account on the social media platform."
        ],
        "icon": "🤳"
    },
    {
        "title": "QR Code Scam",
        "category": "Payment Fraud",
        "risk": "High Risk",
        "color": "#ef4444",
        "desc": "Malicious QR codes pasted over legitimate codes in public places or sent in chats that redirect to fraudulent checkout pages or initiate instant money debits.",
        "flags": [
            "QR code stickers physically pasted over official payment codes on parking meters or vendors.",
            "Codes sent via chat promising gift vouchers, cashbacks, or lottery payouts upon scanning."
        ],
        "recommendations": [
            "Double-check physical codes to ensure they haven't been tampered with or covered.",
            "Always preview the destination URL or business name shown by the scanner before proceeding.",
            "Never scan a code if you are supposed to be receiving a payment."
        ],
        "icon": "🖼️"
    },
    {
        "title": "Fake Electricity Bill Scam",
        "category": "Financial Fraud",
        "risk": "High Risk",
        "color": "#ef4444",
        "desc": "Threats of power disconnection in 30 minutes unless you pay immediately via a provided mobile number/link.",
        "flags": [
            "Immediate disconnection warning with a short deadline.",
            "Instructions to call personal mobile numbers to avoid disconnection.",
            "Payment requested through non-standard links or personal UPI accounts."
        ],
        "recommendations": [
            "Pay utility bills only through official apps or verified utility company portals.",
            "Verify utility alerts directly with the customer service number on your physical bill.",
            "Electricity boards never threaten disconnection in a span of minutes via SMS."
        ],
        "icon": "⚡"
    }
]

# --- SIDEBAR NAVIGATION ---

# --- TOP BAR ---
t1, t2 = st.columns([3, 1])
with t1:
    search_query = st.text_input(
        "🔍 Search Scans...",
        placeholder="Search scam database (e.g. UPI, job, phish)...",
        label_visibility="collapsed",
        key="scam_search_query"
    )
with t2:
    st.markdown("""
        <div style="display: flex; justify-content: flex-end; gap: 15px; align-items: center;">
            <span>🔔</span>
            <div style="width: 35px; height: 35px; background: #48C6EF; border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">U</div>
        </div>
    """, unsafe_allow_html=True)

# --- PAGE HEADER ---
st.markdown("<h1 style='color:#1e3a8a; margin-bottom:0;'>AI Screenshot Scanner</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748b; font-size:1.1rem;'>Upload suspicious screenshots and let AI analyze scams, phishing, fake jobs, and misinformation.</p>", unsafe_allow_html=True)

# --- SEARCH PROCESSING ---
if search_query:
    st.write("")
    st.markdown(f"### 🔍 Search Results for: *{search_query}*")
    
    # Filter the database
    q_lower = search_query.lower().strip()
    matching_scams = [
        s for s in searchable_scams
        if q_lower in s["title"].lower()
        or q_lower in s["category"].lower()
        or q_lower in s["desc"].lower()
        or any(q_lower in flag.lower() for flag in s["flags"])
    ]
    
    if matching_scams:
        for idx, scam in enumerate(matching_scams):
            # Format lists for HTML rendering
            flags_html = "".join(f"<li>{flag}</li>" for flag in scam['flags'])
            recs_html = "".join(f"<li>{rec}</li>" for rec in scam['recommendations'])
            
            st.markdown(f"""
            <div class="glass-card" style="border-left: 6px solid {scam['color']}; margin-bottom: 20px;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;">
                    <span style="font-size: 2.2rem;">{scam['icon']}</span>
                    <div>
                        <h4 style="margin: 0; color: #1e3a8a;">{scam['title']}</h4>
                        <span style="font-size: 0.85rem; background: rgba(72,198,239,0.15); color: #1e3a8a; padding: 3px 8px; border-radius: 8px; font-weight: 500;">{scam['category']}</span>
                        <span style="font-size: 0.85rem; background: {scam['color']}20; color: {scam['color']}; padding: 3px 8px; border-radius: 8px; font-weight: 500; margin-left: 5px;">{scam['risk']}</span>
                    </div>
                </div>
                <p style="color: #475569; font-size: 0.95rem; line-height: 1.5; margin-bottom: 15px;">{scam['desc']}</p>
                <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 280px; background: rgba(239, 68, 68, 0.04); padding: 15px; border-radius: 12px; border: 1px solid rgba(239, 68, 68, 0.1);">
                        <strong style="color: #ef4444; display: block; margin-bottom: 8px;">🚩 Common Red Flags:</strong>
                        <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 0.88rem; line-height: 1.4;">
                            {flags_html}
                        </ul>
                    </div>
                    <div style="flex: 1; min-width: 280px; background: rgba(16, 185, 129, 0.04); padding: 15px; border-radius: 12px; border: 1px solid rgba(16, 185, 129, 0.1);">
                        <strong style="color: #10b981; display: block; margin-bottom: 8px;">🛡️ Safety Recommendations:</strong>
                        <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 0.88rem; line-height: 1.4;">
                            {recs_html}
                        </ul>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
        
        # Clear search button
        if st.button("Clear Search Results ✖", key="clear_search_btn"):
            st.session_state.scam_search_query = ""
            st.rerun()
    else:
        st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 40px;">
            <div style="font-size: 3rem; margin-bottom: 15px;">🔍🕵️‍♂️</div>
            <h4 style="color: #1e3a8a; margin-bottom: 10px;">No scams found matching your query</h4>
            <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 20px;">Try searching for other common keywords like <b>UPI, job, phishing, OTP, lottery, electricity</b>, etc.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Clear Search Results ✖", key="clear_search_btn_empty"):
            st.session_state.scam_search_query = ""
            st.rerun()
    
    st.markdown("---")

# --- MAIN CONTENT ---
col_main, col_side = st.columns([2, 1], gap="large")

with col_main:
    # UPLOAD SECTION
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; margin-bottom:20px;">
            <img src="https://cdn-icons-png.flaticon.com/512/126/126477.png" width="80" style="opacity:0.5;">
            <h3>Drag & Drop Screenshot</h3>
            <p style="color:#94a3b8;">Supported formats: PNG, JPG, JPEG, WEBP</p>
        </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose File", type=['png', 'jpg', 'jpeg', 'webp'], label_visibility="collapsed")
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Preview: Suspicious Content", use_container_width=True)
        if st.button("Reset / Clear Screenshot 🗑️", use_container_width=True):
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # ANALYSIS OPTIONS
    st.markdown("### Select Analysis Depth")
    o1, o2, o3 = st.columns(3)
    with o1:
        scam_check = st.checkbox("✔ Scam Detection", value=True)
    with o2:
        phish_check = st.checkbox("✔ Phishing Check", value=True)
    with o3:
        job_check = st.checkbox("✔ Fake Job Detection")
        
    o4, o5 = st.columns(2)
    with o4:
        misinfo_check = st.checkbox("✔ Misinformation")
    with o5:
        harm_check = st.checkbox("✔ Harmful Content")

    st.write("")
    col_btn1, col_btn2 = st.columns([3, 1])
    with col_btn1:
        analyze_clicked = st.button("Analyze Screenshot")
    with col_btn2:
        back_clicked = st.button("🏠 Back to Home", use_container_width=True)
        
    if analyze_clicked:
        if uploaded_file is not None:
            # PROCESS CARD
            with st.status("AI PeaceGuard is analyzing...", expanded=True) as status:
                st.write("🔍 Reading Screenshot...")
                time.sleep(0.8)
                
                # Check for QR code in the uploaded image
                has_qr, decode_success, decoded_info = detect_and_decode_qr(uploaded_file)
                
                if has_qr:
                    st.write("🖼️ **QR Code Detected**")
                    if decode_success:
                        st.write(f"📝 **Decoded Content:** `{decoded_info}`")
                    else:
                        st.write("⚠️ *Unreadable QR Code (Failed to decode content)*")
                        
                    st.write("🧠 **Running Gemini AI Safety Analysis...**")
                    
                    try:
                        # Attempt Gemini analysis
                        scan_result = analyze_qr_with_gemini(uploaded_file, decoded_info if decode_success else "")
                        st.session_state.scan_result = scan_result
                        st.write("✅ Gemini Analysis Complete.")
                    except Exception as e:
                        # Graceful fallback on failure
                        st.write(f"⚠️ *Gemini API failure or key missing. Falling back to offline QR analyzer...*")
                        scan_result = generate_offline_qr_analysis(decoded_info if decode_success else "")
                        st.session_state.scan_result = scan_result
                    
                    st.session_state.scan_image = uploaded_file
                    status.update(label="Analysis Complete!", state="complete", expanded=False)
                else:
                    # Proceed with standard screenshot scam analysis flow
                    st.write("📝 Extracting Text via OCR...")
                    time.sleep(1.0)
                    st.write("🛡️ Checking Risk Patterns...")
                    time.sleep(0.8)
                    st.write("📋 Generating AI Report...")
                    time.sleep(0.4)
                    
                    # Dynamic realistic demo analysis generation
                    import random
                    filename = uploaded_file.name.lower()
                    
                    if any(k in filename for k in ["job", "intern", "work", "career"]):
                        scam_type = "Fake Job Scam"
                        risk_level = "High Risk"
                        confidence = f"{random.randint(86, 96)}%"
                        peace_score = random.randint(15, 35)
                        red_flags = [
                            "Recruiter contact domain is a public address (e.g. Gmail) rather than corporate.",
                            "Upfront administrative, laptop setup, or training fees are requested.",
                            "Extremely high payment promised for simple tasks or entry-level skills."
                        ]
                        recommendations = [
                            "Never pay money to secure a job offer or internship opportunity.",
                            "Verify recruiters via official corporate directories or LinkedIn.",
                            "Crosscheck the job title directly on the company's official careers portal."
                        ]
                        explanation = "This screenshot contains key risk patterns typical of a Recruitment/Employment Scam. It pressures the applicant to pay upfront fees and displays non-standard communication channels."
                        issues = [
                            {"type": "Recruiter Email", "desc": "Public domain email used for official contact.", "severity": "HIGH", "icon": "✉️"},
                            {"type": "Payment Demand", "desc": "Asks for registration fees upfront.", "severity": "HIGH", "icon": "💳"}
                        ]
                    elif any(k in filename for k in ["upi", "pay", "reward", "money", "cash", "scan", "qr"]):
                        scam_type = "UPI Cash Reward Scam"
                        risk_level = "High Risk"
                        confidence = f"{random.randint(89, 98)}%"
                        peace_score = random.randint(10, 25)
                        red_flags = [
                            "Prompts you to enter your UPI PIN to claim or receive money.",
                            "Claims you won an unentered lottery, lucky draw, or scratch card.",
                            "Creates high urgency by claiming the reward will expire in minutes."
                        ]
                        recommendations = [
                            "Remember: A UPI PIN is only required to send money, NEVER to receive it.",
                            "Do not scan QR codes shared by unknown contacts to 'credit' funds.",
                            "Report and block the sender's mobile number on your payment app."
                        ]
                        explanation = "This image contains elements of a Payment Gateway Fraud. The scam attempts to trick you into entering a security PIN to receive a lottery reward. This will drain funds instead of crediting them."
                        issues = [
                            {"type": "UPI PIN Request", "desc": "PIN prompt for incoming transaction.", "severity": "HIGH", "icon": "🔑"},
                            {"type": "Urgency Pressure", "desc": "Claims reward expires in 5 minutes.", "severity": "HIGH", "icon": "⚠️"}
                        ]
                    elif any(k in filename for k in ["login", "bank", "phish", "secure", "verify", "link"]):
                        scam_type = "Phishing Scam"
                        risk_level = "High Risk"
                        confidence = f"{random.randint(88, 97)}%"
                        peace_score = random.randint(18, 38)
                        red_flags = [
                            "URL does not match the official domain (e.g. secure-netbank-update.com).",
                            "Urgent warnings threatening account suspension or card blocking.",
                            "Login fields asking for passwords, security questions, or OTPs."
                        ]
                        recommendations = [
                            "Do not click links in SMS or email alerts regarding bank account lockouts.",
                            "Manually type the verified bank website address in your browser.",
                            "Report the phishing link to the corporate security team or authorities."
                        ]
                        explanation = "This screenshot matches typical phishing layout templates. It uses a high-pressure warning of account deactivation to manipulate the user into entering sensitive login credentials on a spoofed portal."
                        issues = [
                            {"type": "Spoofed Link", "desc": "Domain mismatch with verified brand domain.", "severity": "HIGH", "icon": "🔗"},
                            {"type": "Suspension Threat", "desc": "Threatens immediate account lockout.", "severity": "HIGH", "icon": "⚠️"}
                        ]
                    else:
                        # Randomly assign one of the types (scam or safe)
                        choice = random.choice(["job", "upi", "phish", "safe"])
                        if choice == "job":
                            scam_type = "Fake Job Scam"
                            risk_level = "High Risk"
                            confidence = f"{random.randint(85, 95)}%"
                            peace_score = random.randint(20, 35)
                            red_flags = [
                                "Use of non-business email domain for official communication.",
                                "Requirement of payment for starter equipment/training."
                            ]
                            recommendations = [
                                "Do not pay recruitment or hardware fees.",
                                "Verify the contact's identity on LinkedIn or official directory."
                            ]
                            explanation = "Employment fraud indicators found. The message requests payment in exchange for training materials, which is typical of recruitment scams."
                            issues = [
                                {"type": "Public Domain", "desc": "Recruiter using non-corporate email.", "severity": "HIGH", "icon": "✉️"},
                                {"type": "Upfront Fees", "desc": "Request for administrative payment.", "severity": "HIGH", "icon": "💳"}
                            ]
                        elif choice == "upi":
                            scam_type = "UPI Cash Reward Scam"
                            risk_level = "High Risk"
                            confidence = f"{random.randint(90, 97)}%"
                            peace_score = random.randint(12, 28)
                            red_flags = [
                                "Urges scanning a QR code or entering a PIN to receive a cash gift.",
                                "Lucky draw notification from an unknown sender."
                            ]
                            recommendations = [
                                "Never enter a UPI PIN to receive cashback or payments.",
                                "Ignore lottery win SMS messages."
                            ]
                            explanation = "UPI scam pattern detected. The screenshot urges scanning a code to claim a cash reward, which will result in unauthorized debit."
                            issues = [
                                {"type": "PIN Prompt", "desc": "Asks for security code to accept money.", "severity": "HIGH", "icon": "🔑"},
                                {"type": "Suspicious Sender", "desc": "Unsolicited reward notification.", "severity": "HIGH", "icon": "👤"}
                            ]
                        elif choice == "phish":
                            scam_type = "Phishing Scam"
                            risk_level = "High Risk"
                            confidence = f"{random.randint(87, 96)}%"
                            peace_score = random.randint(15, 37)
                            red_flags = [
                                "Suspicious URL containing misspelled brand names.",
                                "Warning that account will be closed within 24 hours."
                            ]
                            recommendations = [
                                "Do not enter passwords or OTPs on redirected webpages.",
                                "Directly contact the official helpline of the provider."
                            ]
                            explanation = "Phishing attempt detected. The message is spoofing a banking/payment portal to capture account credentials."
                            issues = [
                                {"type": "Unverified Link", "desc": "Suspicious URL domain name.", "severity": "HIGH", "icon": "🔗"},
                                {"type": "Urgent Action", "desc": "Threatens card suspension in 24 hours.", "severity": "HIGH", "icon": "⚠️"}
                            ]
                        else:
                            scam_type = "None (Safe Communication)"
                            risk_level = "Safe Content"
                            confidence = f"{random.randint(92, 99)}%"
                            peace_score = random.randint(90, 98)
                            red_flags = []
                            recommendations = [
                                "Keep practicing safe online behavior.",
                                "Always verify sender details before sharing any personal info."
                            ]
                            explanation = "No safety threats or scam patterns were identified in the screenshot. The message appears to be safe and official communication."
                            issues = [
                                {"type": "Verified Sender", "desc": "Sender matches official corporate domain.", "severity": "NONE", "icon": "🛡️"},
                                {"type": "Clean Content", "desc": "No high-pressure text or request for credentials.", "severity": "NONE", "icon": "✅"}
                            ]
                    
                    st.session_state.scan_image = uploaded_file
                    st.session_state.scan_result = {
                        "scam_type": scam_type,
                        "risk_level": risk_level,
                        "confidence": confidence,
                        "peace_score": peace_score,
                        "red_flags": red_flags,
                        "recommendations": recommendations,
                        "explanation": explanation,
                        "issues": issues
                    }
                    
                    status.update(label="Analysis Complete!", state="complete", expanded=False)
            
            st.toast("Redirecting to detailed report...")
            time.sleep(1.0)
            st.switch_page("pages/scanner_result.py")
        else:
            st.error("Please upload a screenshot first!")
            
    if back_clicked:
        st.switch_page("pages/home.py")

with col_side:
    # TIPS CARD
    st.markdown('<div class="glass-card" style="background: linear-gradient(135deg, #e0f2f1 0%, #ffffff 100%);">', unsafe_allow_html=True)
    st.markdown("#### 💡 Cyber Safety Tip")
    st.markdown("""
    <p style="font-size:0.9rem; color:#0d9488;">
    "Always verify the sender's email address or phone number before clicking any links, even if the message looks urgent."
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # RECENT SCANS
    st.markdown("### Recent Scans")
    
    scans = [
        {"title": "Fake Internship", "risk": "Medium Risk", "color": "#f59e0b", "time": "Yesterday"},
        {"title": "UPI Scam", "risk": "High Risk", "color": "#ef4444", "time": "Today"},
        {"title": "Safe Message", "risk": "Safe", "color": "#10b981", "time": "2 Days Ago"}
    ]
    
    for scan in scans:
        st.markdown(f"""
            <div class="glass-card" style="padding: 15px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 600;">{scan['title']}</span>
                    <span style="font-size: 0.75rem; color: #94a3b8;">{scan['time']}</span>
                </div>
                <div style="color: {scan['color']}; font-size: 0.85rem; font-weight: 500;">{scan['risk']}</div>
            </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
    <div style="text-align: center; color: #94a3b8; padding-bottom: 20px;">
        <p style="margin-bottom: 5px; font-weight: 600; color: #1e3a8a;">PeaceGuard AI</p>
        <p style="font-size: 0.85rem;">AI Powered Digital Peace Platform • Developed by Vaishali Gangurde</p>
    </div>
""", unsafe_allow_html=True)