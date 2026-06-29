import streamlit as st
import time

# --- DEMO MODE STEP 1 OVERLAY ---
if st.session_state.get("demo_mode", False) and st.session_state.get("demo_step", 1) == 1:
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3a8a, #0d9488); color: white; padding: 20px; border-radius: 16px; margin: 20px; box-shadow: 0 4px 15px rgba(30,58,138,0.25);">
        <h4 style="margin: 0; color: #e6fffa; font-family: 'Poppins', sans-serif;">🛡️ PeaceGuard AI Guided Walkthrough Started</h4>
        <p style="margin: 5px 0 0 0; color: #f0fdfa; font-family: 'Poppins', sans-serif; font-size: 0.95rem;">
            <b>Step 1 of 7: Landing Page</b>. This is the public landing page where digital citizens discover PeaceGuard AI.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_play, col_next, col_exit = st.columns([1.5, 1, 1])
    with col_play:
        auto_advance = st.checkbox("Auto-advance (3s)", value=True, key="demo_auto_1")
    with col_next:
        if st.button("Next: AI Scanner ➔", use_container_width=True, key="demo_next_1"):
            st.session_state.demo_step = 2
            st.switch_page("pages/ai_scanner.py")
    with col_exit:
        if st.button("Exit Walkthrough ❌", use_container_width=True, key="demo_exit_1"):
            st.session_state.demo_mode = False
            st.session_state.demo_step = 0
            st.rerun()
            
    if auto_advance:
        time.sleep(3.0)
        st.session_state.demo_step = 2
        st.switch_page("pages/ai_scanner.py")

st.markdown("""
<style>
.page, .page *{
box-sizing:border-box;
font-family:Inter,Arial,sans-serif;
}

body, .stApp {
margin:0;
color:#102033;
background:
radial-gradient(circle at 8% 8%,rgba(47,128,237,.23),transparent 30%),
radial-gradient(circle at 88% 12%,rgba(32,201,151,.25),transparent 32%),
linear-gradient(135deg,#f7fcff,#effff8) !important;
}

.page{
max-width:1180px;
margin:auto;
padding:28px;
}

.nav{
position:sticky;
top:18px;
z-index:20;
display:flex;
align-items:center;
justify-content:space-between;
padding:15px 20px;
border-radius:28px;
background:rgba(255,255,255,.68);
border:1px solid rgba(255,255,255,.9);
backdrop-filter:blur(22px);
box-shadow:0 24px 70px rgba(47,128,237,.15);
}

.brand{
display:flex;
align-items:center;
gap:14px;
font-size:24px;
font-weight:800;
}

.logo-wrap{
width:56px;
height:56px;
border-radius:20px;
background:linear-gradient(135deg,#2f80ed,#20c997);
display:grid;
place-items:center;
position:relative;
box-shadow:0 18px 45px rgba(47,128,237,.25);
}

.logo-wrap:before{
content:"";
position:absolute;
inset:-8px;
border-radius:28px;
border:2px solid rgba(47,128,237,.22);
border-top-color:#20c997;
border-right-color:#2f80ed;
animation:spin 3s linear infinite;
}

.logo-wrap:after{
content:"";
position:absolute;
inset:-15px;
border-radius:34px;
border:1px dashed rgba(32,201,151,.35);
animation:spinReverse 7s linear infinite;
}

.logo-shield{
width:29px;
height:36px;
background:white;
clip-path:polygon(50% 0,88% 15%,86% 55%,70% 82%,50% 100%,30% 82%,14% 55%,12% 15%);
position:relative;
z-index:2;
}

.links{
display:flex;
align-items:center;
gap:28px;
font-weight:700;
}

.links a{
color:#50687b;
text-decoration:none;
transition:.25s;
}

.links a:hover{
color:#10806d;
}

.sign{
padding:12px 21px;
border-radius:30px;
color:white;
background:linear-gradient(135deg,#2f80ed,#20c997);
box-shadow:0 14px 35px rgba(32,201,151,.25);
}

.links a.sign {
color: white !important;
text-decoration: none !important;
}

.links a.sign:hover {
color: white !important;
opacity: 0.9;
}

.hero{
display:grid;
grid-template-columns:1fr 1fr;
gap:58px;
align-items:center;
min-height:640px;
}

.badge{
display:inline-block;
margin-bottom:20px;
padding:10px 16px;
border-radius:99px;
background:rgba(255,255,255,.78);
color:#087765;
font-weight:800;
font-size:14px;
}

h1{
font-size:68px;
line-height:1.04;
margin:0;
font-weight:800;
letter-spacing:0;
}

.grad{
background:linear-gradient(135deg,#2f80ed,#20c997);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.tagline{
font-size:22px;
font-weight:800;
margin-top:22px;
color:#12344d;
}

.sub{
font-size:19px;
line-height:1.75;
color:#547085;
max-width:620px;
margin-top:14px;
}

.actions{
display:flex;
gap:16px;
margin-top:32px;
}

.btn{
padding:16px 25px;
border-radius:32px;
text-decoration:none;
font-weight:800;
transition:.25s;
display:inline-block;
}

.btn:hover{
transform:translateY(-4px);
}

.primary{
color:white;
background:linear-gradient(135deg,#2f80ed,#20c997);
box-shadow:0 18px 40px rgba(47,128,237,.3);
}

.btn.primary:hover {
color: white !important;
}

.secondary{
color:#12334b;
background:white;
border:1px solid rgba(47,128,237,.18);
}

.visual{
height:505px;
border-radius:40px;
position:relative;
overflow:hidden;
background:rgba(255,255,255,.64);
border:1px solid white;
backdrop-filter:blur(24px);
box-shadow:0 34px 90px rgba(30,88,143,.18);
}

.visual:before{
content:"";
position:absolute;
inset:30px;
border-radius:30px;
background:
linear-gradient(90deg,rgba(47,128,237,.09) 1px,transparent 1px),
linear-gradient(rgba(32,201,151,.09) 1px,transparent 1px);
background-size:32px 32px;
}

.orbit{
position:absolute;
width:330px;
height:330px;
border-radius:50%;
left:50%;
top:95px;
transform:translateX(-50%);
border:2px solid rgba(47,128,237,.25);
animation:pulse 3.5s ease-in-out infinite;
}

.orbit:before{
content:"";
position:absolute;
width:18px;
height:18px;
border-radius:50%;
background:#20c997;
top:30px;
left:52px;
box-shadow:0 0 22px rgba(32,201,151,.75);
animation:orbitMove 5s linear infinite;
}

.big-shield{
position:absolute;
width:195px;
height:240px;
left:50%;
top:92px;
transform:translateX(-50%);
background:linear-gradient(135deg,#2f80ed,#20c997);
clip-path:polygon(50% 0,88% 15%,86% 55%,70% 82%,50% 100%,30% 82%,14% 55%,12% 15%);
animation:float 4s ease-in-out infinite;
box-shadow:0 25px 65px rgba(47,128,237,.28);
}

.big-shield:after{
content:"";
position:absolute;
inset:22px;
background:white;
clip-path:inherit;
}

.float-card{
position:absolute;
width:94px;
height:94px;
border-radius:28px;
background:rgba(255,255,255,.78);
box-shadow:0 18px 45px rgba(47,128,237,.14);
animation:soft 5s infinite;
}

.float-card:after{
content:"";
position:absolute;
inset:28px;
border-radius:14px;
background:linear-gradient(135deg,#2f80ed,#20c997);
}

.f1{left:62px;top:86px}
.f2{right:64px;top:145px;animation-delay:-1s}
.f3{left:105px;bottom:78px;animation-delay:-2s}
.f4{right:105px;bottom:82px;animation-delay:-1.5s}

.trust{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:22px;
margin:35px 0 90px;
}

.card{
background:rgba(255,255,255,.68);
border:1px solid white;
border-radius:28px;
padding:28px;
box-shadow:0 22px 60px rgba(33,93,145,.12);
transition:.25s;
}

.card:hover{
transform:translateY(-8px);
}

.card h3{
margin:0 0 10px;
font-size:22px;
}

.card p{
margin:0;
color:#5a7488;
line-height:1.65;
}

.section-title{
text-align:center;
margin-bottom:36px;
}

.section-title h2{
font-size:44px;
margin:0;
}

.section-title p{
color:#5a7488;
font-size:17px;
}

.features{
display:grid;
grid-template-columns:repeat(3,1fr);
gap:22px;
margin-bottom:85px;
}

.icon{
width:52px;
height:52px;
border-radius:18px;
background:linear-gradient(135deg,#2f80ed,#20c997);
margin-bottom:22px;
position:relative;
}

.icon:after{
content:"";
position:absolute;
inset:13px;
border-radius:10px;
background:white;
opacity:.8;
}

.footer{
display:flex;
justify-content:space-between;
gap:20px;
border-top:1px solid rgba(47,128,237,.2);
padding:32px 0;
color:#60788a;
}

@keyframes spin{
to{transform:rotate(360deg)}
}

@keyframes spinReverse{
to{transform:rotate(-360deg)}
}

@keyframes float{
50%{transform:translateX(-50%) translateY(-16px)}
}

@keyframes pulse{
50%{transform:translateX(-50%) scale(1.05);opacity:.55}
}

@keyframes soft{
50%{transform:translateY(-12px)}
}

@keyframes orbitMove{
from{transform:rotate(0deg) translateX(145px) rotate(0deg)}
to{transform:rotate(360deg) translateX(145px) rotate(-360deg)}
}

@media(max-width:900px){
.hero,.trust,.features{
grid-template-columns:1fr;
}
.links{
display:none;
}
h1{
font-size:46px;
}
.footer{
flex-direction:column;
}
}
</style>

<div class="page">
<nav class="nav">
  <div class="brand">
    <div class="logo-wrap">
      <div class="logo-shield"></div>
    </div>
    PeaceGuard AI
  </div>
  <div class="links">
    <a href="#home">Home</a>
    <a href="#features">Features</a>
    <a href="#about">About</a>
    <a href="#contact">Contact</a>
    <a class="sign" href="/Login" target="_self" style="cursor: pointer;">Sign In</a>
  </div>
</nav>
<section class="hero" id="home">
  <div>
    <div class="badge">AI Safety Platform for Digital Peace</div>
    <h1>
      Building a Safer Digital World with
      <span class="grad">AI</span>
    </h1>
    <div class="tagline">
      Detect danger early. Verify before you trust. Spread peace online.
    </div>
    <p class="sub">
      PeaceGuard AI helps users detect scams, phishing, misinformation,
      fake job offers, and suspicious screenshots before they cause harm.
    </p>
    <div class="actions">
      <a class="btn primary" href="/Login" target="_self" style="cursor: pointer;">Get Started</a>
      <a class="btn secondary" href="/?demo=start" target="_self" style="cursor: pointer;">Watch Demo</a>
    </div>
  </div>
  <div class="visual">
    <div class="orbit"></div>
    <div class="big-shield"></div>
    <div class="float-card f1"></div>
    <div class="float-card f2"></div>
    <div class="float-card f3"></div>
    <div class="float-card f4"></div>
  </div>
</section>
<section class="trust" id="about">
  <div class="card">
    <h3>Trusted by Students</h3>
    <p>Built for young digital citizens who need quick, clear, and calm online safety guidance.</p>
  </div>
  <div class="card">
    <h3>AI Powered</h3>
    <p>Uses intelligent risk signals to explain scams, suspicious claims, and harmful content.</p>
  </div>
  <div class="card">
    <h3>Privacy First</h3>
    <p>Designed around safe handling, minimal exposure, and responsible cyber awareness.</p>
  </div>
</section>
<section id="features">
  <div class="section-title">
    <h2>Premium Protection Features</h2>
    <p>A modern safety layer for peaceful and informed online communities.</p>
  </div>
  <div class="features">
    <div class="card">
      <div class="icon"></div>
      <h3>AI Screenshot Analysis</h3>
      <p>Analyze suspicious screenshots and identify warning signs in messages, offers, and posts.</p>
    </div>
    <div class="card">
      <div class="icon"></div>
      <h3>Scam Detection</h3>
      <p>Flags fake rewards, phishing links, payment pressure, impersonation, and fraud patterns.</p>
    </div>
    <div class="card">
      <div class="icon"></div>
      <h3>Misinformation Detection</h3>
      <p>Highlights misleading claims, missing sources, manipulated narratives, and harmful content.</p>
    </div>
    <div class="card">
      <div class="icon"></div>
      <h3>Awareness</h3>
      <p>Turns every digital risk into a simple cyber safety learning moment.</p>
    </div>
    <div class="card">
      <div class="icon"></div>
      <h3>Community</h3>
      <p>Encourages peaceful reporting, shared awareness, and responsible digital behavior.</p>
    </div>
    <div class="card">
      <div class="icon"></div>
      <h3>Dashboard</h3>
      <p>Shows safety insights, scan trends, and common threat categories in a clean visual way.</p>
    </div>
  </div>
</section>
<footer class="footer" id="contact">
  <div>
    **PeaceGuard AI**<br>
    Protecting digital peace with AI.
  </div>
  <div>
    Home &nbsp; Features &nbsp; About &nbsp; Contact
  </div>
</footer>
</div>
""", unsafe_allow_html=True)
