import streamlit as st
import datetime

# --- PAGE CONFIG ---


# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f0f9ff 0%, #e6fffa 100%);
    }

    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 24px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }

    /* Discussion Post */
    .post-container {
        border-bottom: 1px solid #e2e8f0;
        padding: 15px 0;
    }
    .post-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 8px;
    }
    .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: #48C6EF;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
    }

    /* Badges */
    .badge-community {
        background: #e0f2f1;
        color: #00796b;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
    }

    /* Sidebar Highlight */
    [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.8); }
    .nav-item-active {
        background: linear-gradient(90deg, rgba(72,198,239,0.2), rgba(111,134,214,0.2));
        border-radius: 12px;
        padding: 12px;
        color: #1e3a8a;
        font-weight: 600;
        border-left: 4px solid #48C6EF;
    }

    /* Sticker Style */
    .sticker {
        font-size: 40px;
        animation: bounce 2s infinite;
        display: inline-block;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---

# --- HEADER ---
st.markdown("<h1 style='color:#1e3a8a;'>Community Peace Hub 👥✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748b; font-size:1.1rem;'>Report scams, discuss safety trends, and help others stay protected! Together we are stronger. 🛡️🤝</p>", unsafe_allow_html=True)

# --- TOP STATS & STICKERS ---
stat1, stat2, stat3, stat4 = st.columns(4)
with stat1:
    st.markdown('<div class="glass-card" style="text-align:center;"><div class="sticker">🌟</div><h4>12.4k</h4><p>Active Guardians</p></div>', unsafe_allow_html=True)
with stat2:
    st.markdown('<div class="glass-card" style="text-align:center;"><div class="sticker">📢</div><h4>450</h4><p>Scams Reported</p></div>', unsafe_allow_html=True)
with stat3:
    st.markdown('<div class="glass-card" style="text-align:center;"><div class="sticker">🏆</div><h4>89%</h4><p>Safety Rating</p></div>', unsafe_allow_html=True)
with stat4:
    st.markdown('<div class="glass-card" style="text-align:center;"><div class="sticker">💖</div><h4>2.1k</h4><p>Lives Protected</p></div>', unsafe_allow_html=True)

# --- MAIN LAYOUT ---
# Initialize session state posts
if 'community_posts' not in st.session_state:
    st.session_state.community_posts = [
        {"user": "Rohan", "tag": "Verified Guardian", "title": "New 'Part-time job' SMS doing rounds!", "content": "Just got an SMS claiming to be from Amazon offering ₹10,000/day. Don't click the link, it's a phishing site!", "time": "2h ago", "likes": 45, "comments_list": ["Thanks for sharing, I got this too!", "This is definitely fake."]},
        {"user": "Sanya", "tag": "Elite Member", "title": "Safe Payment Tip 💡", "content": "Always remember, you NEVER need to enter your UPI PIN to RECEIVE money. If someone asks for it, it's a scam!", "time": "5h ago", "likes": 120, "comments_list": ["Very important tip!", "Almost fell for this last week."]},
        {"user": "Amit", "tag": "New Member", "title": "Help! Is this QR Code safe?", "content": "Saw a QR code at the bus stop for 'Free Data'. My PeaceGuard AI scanner flagged it. Glad I used the app first! 🛡️", "time": "1d ago", "likes": 32, "comments_list": ["Scan first, open later. Always safe."]}
    ]

# If redirected from Scanner Result with report flag
if st.session_state.get('report_from_scan', False):
    new_scan_post = {
        "user": "You (Guardian)",
        "tag": "Guardian",
        "title": "Alert: Verified Safe Screenshot Scan Report",
        "content": "Just analyzed a screenshot using PeaceGuard AI. The report indicates 92/100 Digital Peace Score (Safe). Proceeding with confidence.",
        "time": "Just now",
        "likes": 0,
        "comments_list": []
    }
    st.session_state.community_posts.insert(0, new_scan_post)
    st.success("🎉 Scan report successfully imported and posted to community feed!")
    del st.session_state.report_from_scan

col_feed, col_side = st.columns([2.2, 1], gap="large")

with col_feed:
    col_t, col_ref = st.columns([2.5, 1.5])
    with col_t:
        st.markdown("### 🔥 Trending Discussions")
    with col_ref:
        if st.button("Refresh Feed 🔄", use_container_width=True, key="refresh_feed_btn"):
            # Update existing post likes randomly to show activity
            import random
            for p in st.session_state.community_posts:
                p['likes'] += random.randint(1, 4)
            
            # List of possible new mock posts to inject
            new_mock_posts = [
                {"user": "Neha", "tag": "Active Member", "title": "Phishing link claiming to be SpeedPost", "content": "Got a text saying my package is held at the post office due to incorrect address: speedpost-lookup.info. Checked and flagged it. Stay safe!", "time": "Just now", "likes": 5, "comments_list": []},
                {"user": "Deepak", "tag": "Verified Guardian", "title": "Fake electricity bill alert!", "content": "A caller claiming to be from electricity board threatened disconnect in 30 mins. It's a scam to get instant UPI pay!", "time": "1m ago", "likes": 12, "comments_list": ["Classic pressure tactic."]},
                {"user": "Meera", "tag": "Elite Member", "title": "Instagram Giveaway Scam", "content": "Accounts spoofing popular influencers are DMing people claiming they won a phone. They ask you to pay shipping fee first. Don't pay!", "time": "3m ago", "likes": 18, "comments_list": ["Never pay shipping for giveaways."]},
            ]
            
            # Find a post that is not yet in the feed
            existing_titles = {p['title'] for p in st.session_state.community_posts}
            available_posts = [p for p in new_mock_posts if p['title'] not in existing_titles]
            
            if available_posts:
                st.session_state.community_posts.insert(0, random.choice(available_posts))
                st.toast("New scam reports loaded! 🔄")
            else:
                st.toast("Feed is up to date! 🔄")
                
            st.rerun()
    
    # REPORT A SCAM INTERACTIVE BOX
    with st.expander("✨ Report a New Scam to the Community", expanded=False):
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        scam_type = st.selectbox("Scam Category", ["Phishing", "Fake Job", "UPI Fraud", "OTP Theft", "Other"])
        scam_desc = st.text_area("Describe what happened...")
        scam_img = st.file_uploader("Attach Screenshot (Optional)", type=['png', 'jpg'])
        if st.button("Post to Feed 🚀"):
            if scam_desc:
                new_reported_post = {
                    "user": "You (Guardian)",
                    "tag": "Guardian",
                    "title": f"New report: {scam_type}",
                    "content": scam_desc,
                    "time": "Just now",
                    "likes": 0,
                    "comments_list": []
                }
                st.session_state.community_posts.insert(0, new_reported_post)
                st.balloons()
                st.success("Your report has been shared! You just helped the community. 🎖️")
                st.rerun()
            else:
                st.error("Please enter a description.")
        st.markdown('</div>', unsafe_allow_html=True)

    # COMMUNITY FEED
    for idx, post in enumerate(st.session_state.community_posts):
        st.markdown(f"""
        <div class="glass-card" style="margin-bottom: 5px;">
            <div class="post-header">
                <div class="user-avatar">{post['user'][0]}</div>
                <div>
                    <span style="font-weight:700; color:#1e3a8a;">{post['user']}</span> 
                    <span class="badge-community">{post['tag']}</span><br>
                    <small style="color:#94a3b8;">{post['time']}</small>
                </div>
            </div>
            <h5 style="margin:10px 0;">{post['title']}</h5>
            <p style="color:#475569; font-size:0.95rem;">{post['content']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactions
        col_like, col_comm = st.columns([1.2, 2.8])
        with col_like:
            if st.button(f"❤️ Like ({post['likes']})", key=f"like_btn_{idx}"):
                post['likes'] += 1
                st.rerun()
        with col_comm:
            comment_clicked = st.button(f"💬 Comment ({len(post.get('comments_list', []))})", key=f"comment_btn_{idx}")
            
        show_comm_input = st.session_state.get(f"show_comm_input_{idx}", False)
        if comment_clicked:
            st.session_state[f"show_comm_input_{idx}"] = not show_comm_input
            st.rerun()
            
        if show_comm_input:
            new_comment = st.text_input("Add a comment...", key=f"new_comm_val_{idx}")
            if st.button("Submit comment", key=f"sub_comm_btn_{idx}"):
                if new_comment:
                    post.setdefault('comments_list', []).append(new_comment)
                    st.session_state[f"show_comm_input_{idx}"] = False
                    st.toast("Comment added!")
                    st.rerun()
                    
        # Render comments list
        if post.get('comments_list'):
            for c in post['comments_list']:
                st.markdown(f"""
                <div style="background: rgba(0,0,0,0.03); border-radius: 8px; padding: 6px 12px; margin: 4px 0 4px 20px; font-size: 0.85rem;">
                    💬 <b>Anonymous:</b> {c}
                </div>
                """, unsafe_allow_html=True)
        st.write("")

with col_side:
    st.markdown("### 📊 Community Poll")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("**What's the most common scam you've encountered this week?**")
    st.radio("Select one:", ["WhatsApp Job Offers", "UPI Payment Requests", "Fake Electricity Bills", "Instagram Giveaways"], label_visibility="collapsed")
    if st.button("Vote & See Results", use_container_width=True):
        st.info("Results: 42% voted for WhatsApp Job Offers!")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🏆 Top Contributors")
    contributors = [
        {"name": "Ananya Sharma", "points": "2,450 XP", "badge": "🥇"},
        {"name": "Vikram Singh", "points": "1,820 XP", "badge": "🥈"},
        {"name": "Priya Patel", "points": "1,540 XP", "badge": "🥉"}
    ]
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    for c in contributors:
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <span>{c['badge']} <b>{c['name']}</b></span>
            <span style="color:#0d9488; font-weight:600;">{c['points']}</span>
        </div>
        """, unsafe_allow_html=True)
    if st.button("View Leaderboard", use_container_width=True):
        st.toast("Leaderboard is up to date!")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card" style="background: linear-gradient(135deg, #6F86D6 0%, #48C6EF 100%); color:white;">', unsafe_allow_html=True)
    st.markdown("#### 🎁 Earn Badges!")
    st.write("Report 5 scams to unlock the **'Vigilant Guardian'** badge and earn a PeaceGuard NFT!")
    if st.button("Learn How", key="earn_badge", use_container_width=True):
        st.info("💡 Simply report scams through the Reporting box. Once you reach 5 reports, your badge automatically unlocks!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
st.markdown("""
<div style="text-align: center; color: #64748b; padding-bottom: 20px;">
    <p style="font-weight:600; color:#1e3a8a; margin-bottom:0;">PeaceGuard AI Community</p>
    <p style="font-size:13px;">Connect • Protect • Peace</p>
</div>
""", unsafe_allow_html=True)