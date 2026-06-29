import streamlit as st
import time

# --- PAGE CONFIG ---


# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #fef2f2 0%, #fff7ed 50%, #f0fdf4 100%);
        color: #1e293b;
    }

    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 10px 40px rgba(239, 68, 68, 0.08);
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 45px rgba(239, 68, 68, 0.12);
    }

    /* Red Alert Card */
    .alert-card {
        background: linear-gradient(135deg, #fee2e2 0%, #fef3c7 100%);
        border-left: 6px solid #ef4444;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 30px;
    }

    /* Typography */
    .emergency-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #dc2626, #ea580c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    .emergency-subtitle {
        color: #64748b;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }

    /* Large Hotline Badge */
    .hotline-badge {
        background: linear-gradient(135deg, #dc2626 0%, #ea580c 100%);
        color: white;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(220, 38, 38, 0.25);
        margin-bottom: 25px;
    }

    .stButton>button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    /* Interactive Complaint Section */
    .complaint-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        padding: 20px;
        font-family: monospace;
        color: #334155;
        white-space: pre-wrap;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---

# --- HEADER SECTION ---
st.markdown('<h1 class="emergency-title">Emergency Cyber Support 📞🚨</h1>', unsafe_allow_html=True)
# --- QUICK ACTION UTILITIES ---
ut_col1, ut_col2, ut_col3, ut_col4 = st.columns(4)
with ut_col1:
    if st.button("🚨 Helpline Info", use_container_width=True):
        st.toast("📞 Call the Toll-Free Cyber Helpline at 1930 immediately!")
        st.info("💡 National Helpline: 1930. Available 24/7. Report any financial cyber fraud immediately to retrieve lost transactions.")
with ut_col2:
    if st.button("📋 Reporting Steps", use_container_width=True):
        st.toast("Showing Reporting Steps...")
        st.info("⚡ Steps to Report: \n1. Take screenshots of all proof. \n2. Call 1930 or submit details on cybercrime.gov.in. \n3. Inform your bank to block transactions. \n4. Submit a copy of the complaint to local police.")
with ut_col3:
    if st.button("✅ Safety Checklist", use_container_width=True):
        st.toast("Opening Safety Checklist...")
        st.info("🔐 Emergency Safety Checklist:\n- [ ] Freeze Bank Accounts / UPI IDs\n- [ ] Take Screenshots of Scammer Details\n- [ ] Change compromised account passwords\n- [ ] Enable 2FA on Google/Social accounts\n- [ ] File Official Report at 1930")
with ut_col4:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/home.py")

st.write("")

# --- MAIN LAYOUT ---
col_left, col_right = st.columns([1.2, 1], gap="large")

with col_left:
    # URGENT NOTICE / CRITICAL STEPS
    st.markdown("""
    <div class="alert-card">
        <h4 style="color:#991b1b; margin-top:0;">⚠️ URGENT: If you have just lost money or been compromised:</h4>
        <ol style="margin-bottom:0; color:#7f1d1d; font-weight: 500;">
            <li><b>Freeze Accounts:</b> Immediately block your debit/credit cards and disable UPI services via your bank's app or customer care.</li>
            <li><b>Report within 24 Hours:</b> Call the national cybercrime helpline at <b>1930</b> or report online at <a href="https://cybercrime.gov.in" target="_blank">cybercrime.gov.in</a>.</li>
            <li><b>Gather Proof:</b> Take screenshots of chats, payment transaction IDs, profiles, and phone numbers. Do not delete them!</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    # INTERACTIVE COMPLAINT DRAFT GENERATOR
    st.markdown("### 📝 Cyber Complaint Draft Generator")
    st.write("Fill in the details below to generate a formal, copy-pasteable complaint draft you can use to report to the Cyber Cell or your local police station.")
    
    with st.container():
        st.markdown('<div class="glass-card" style="padding:25px;">', unsafe_allow_html=True)
        
        c_type = st.selectbox("Type of Scam", [
            "UPI Fraud / Fake Payment Request", 
            "Part-time Job Scam / Task Scam", 
            "Phishing / Fake Login Credentials Theft",
            "OTP / Sim Swapping Fraud",
            "Fake Customer Support / Remote Access Scam",
            "Other Online Fraud"
        ])
        
        c1, c2 = st.columns(2)
        with c1:
            occ_date = st.date_input("Date of Incident")
        with c2:
            occ_time = st.time_input("Approximate Time of Incident")
            
        lost_money = st.radio("Did you lose money?", ["Yes", "No"], horizontal=True)
        amount = ""
        if lost_money == "Yes":
            amount = st.text_input("Amount Lost (in INR)", placeholder="e.g. 5000")
            
        suspect_info = st.text_area("Suspect Details (Phone numbers, UPI IDs, Account numbers, or Web URLs used by scammers)", placeholder="e.g. Suspect Phone: +91 98765 43210, UPI ID: reward-claim@upi")
        incident_desc = st.text_area("Brief Description of the Incident", placeholder="Explain exactly what happened step-by-step...")
        
        generate_btn = st.button("Generate Formal Complaint Draft 📄", use_container_width=True)
        
        if generate_btn:
            with st.spinner("Generating draft complaint..."):
                time.sleep(1)
                
            loss_detail = f"a financial loss of INR {amount}" if lost_money == "Yes" else "an online fraud attempt with no financial loss"
            
            complaint_text = f"""To,
The Officer-in-Charge,
Cyber Crime Investigation Cell / Local Police Station,

Subject: Complaint regarding Online Cyber Fraud ({c_type})

Respected Sir/Madam,

I am writing to bring to your immediate notice an incident of cyber fraud that occurred on {occ_date} at approximately {occ_time}. I have been targeted by online scammers resulting in {loss_detail}.

Details of the Incident:
1. Category of Incident: {c_type}
2. Date & Time: {occ_date} around {occ_time}
3. Suspect Information: {suspect_info if suspect_info else "Not known"}
4. Description of events:
{incident_desc if incident_desc else "The scammers contacted me and manipulated me into executing actions under false pretenses, leading to this incident."}

Evidence:
I have saved all relevant transaction receipts, screenshots of conversation messages, call logs, and suspect UPI IDs/phone numbers as proof.

I request you to kindly register my complaint, initiate an investigation, freeze the suspect's bank account/UPI ID if possible, and take necessary legal action under the Information Technology Act and Indian Penal Code.

Thank you.

Yours faithfully,
[Your Name]
[Your Contact Number]
[Your Email Address]"""

            st.success("Draft Generated successfully! Copy the text below:")
            st.markdown(f'<div class="complaint-box">{complaint_text}</div>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # HELPLINE BADGE
    st.markdown("""
    <div class="hotline-badge">
        <h4 style="margin:0; font-size:1.1rem; text-transform:uppercase; letter-spacing:1px; opacity:0.9;">National Cyber Crime Helpline</h4>
        <h1 style="margin: 5px 0; font-size:3.5rem; font-weight:900;">1930</h1>
        <p style="margin:0; font-size:0.9rem; opacity:0.9;">Toll-free • Available 24/7 across India</p>
    </div>
    """, unsafe_allow_html=True)

    # OFFICIAL PORTALS
    st.markdown("### Official Reporting Portals")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex; align-items:center; gap:15px; margin-bottom: 20px;">
        <span style="font-size:30px;">🌐</span>
        <div>
            <b>National Cyber Crime Reporting Portal</b><br>
            <small style="color:#64748b;">Official Government of India portal to file complaints online.</small><br>
            <a href="https://cybercrime.gov.in" target="_blank" style="color:#ef4444; font-weight:600; text-decoration:none;">Visit Website →</a>
        </div>
    </div>
    <div style="display:flex; align-items:center; gap:15px; margin-bottom: 20px;">
        <span style="font-size:30px;">📞</span>
        <div>
            <b>Sanchar Saathi Portal (TAFCOP)</b><br>
            <small style="color:#64748b;">Report unrecognized mobile connections in your name or block lost/stolen phones.</small><br>
            <a href="https://sancharsaathi.gov.in" target="_blank" style="color:#ef4444; font-weight:600; text-decoration:none;">Visit Website →</a>
        </div>
    </div>
    <div style="display:flex; align-items:center; gap:15px;">
        <span style="font-size:30px;">🏦</span>
        <div>
            <b>RBI Sachet Portal</b><br>
            <small style="color:#64748b;">Report illegal deposits or fraudulent financial schemes directly to regulatory bodies.</small><br>
            <a href="https://sachet.rbi.org.in" target="_blank" style="color:#ef4444; font-weight:600; text-decoration:none;">Visit Website →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # BANK SAFETY HELPLINES
    st.markdown("### Major Bank Emergency Links")
    st.write("Quickly freeze/block accounts at major banks using their direct hotlines or fraud reporting portals:")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    banks = [
        {"name": "State Bank of India (SBI)", "num": "1800 1234"},
        {"name": "HDFC Bank", "num": "1800 202 6161"},
        {"name": "ICICI Bank", "num": "1800 1080"},
        {"name": "Axis Bank", "num": "1860 419 5555"}
    ]
    for b in banks:
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1px solid #f1f5f9; padding: 10px 0;">
            <span style="font-weight:600; color:#334155;">🏦 {b['name']}</span>
            <span style="color:#dc2626; font-weight:700;">{b['num']}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding-bottom: 20px;">
    <p style="margin-bottom: 5px; font-weight: 600; color: #dc2626;">PeaceGuard Emergency Response</p>
    <p style="font-size: 0.85rem;">PeaceGuard AI is an awareness platform. Always rely on official local law enforcement in serious emergencies.</p>
</div>
""", unsafe_allow_html=True)
