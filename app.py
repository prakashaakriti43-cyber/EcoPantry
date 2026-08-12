import os
import base64
import random
from datetime import date, datetime
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# --- Helper Functions ---
def get_image_base64(path):
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except Exception:
        return None

logo_b64 = get_image_base64("assets/logo.png")

# --- Page Config ---
st.set_page_config(
    page_title="EcoPantry - Home",
    page_icon="🥗",
    layout="wide"
)

# --- Data Processing for Dynamic Metrics ---
pantry_path = "data/pantry.csv"
leftovers_path = "data/leftovers.csv"

pantry_df = pd.read_csv(pantry_path) if os.path.exists(pantry_path) else pd.DataFrame(columns=["Product", "Category", "Expiry Date", "Quantity"])
leftovers_df = pd.read_csv(leftovers_path) if os.path.exists(leftovers_path) else pd.DataFrame(columns=["Item", "Days Stored"])

today = date.today()

total_pantry = len(pantry_df)
total_leftovers = len(leftovers_df)

expiring_soon_count = 0
expired_count = 0
fresh_count = 0
alerts = []
rec_message = "Your inventory looks good! Keep tracking items to minimize household food waste."

if not pantry_df.empty and "Expiry Date" in pantry_df.columns:
    for idx, row in pantry_df.iterrows():
        try:
            exp_date = datetime.strptime(str(row["Expiry Date"]).strip(), "%Y-%m-%d").date()
            diff = (exp_date - today).days

            if diff < 0:
                expired_count += 1
                alerts.append(f"❌ <strong>{row['Product']}</strong> expired {abs(diff)} day(s) ago!")
            elif diff <= 2:
                expiring_soon_count += 1
                msg = f"⏱️ <strong>{row['Product']}</strong> expires today!" if diff == 0 else f"⚠️ <strong>{row['Product']}</strong> expires in {diff} day(s)!"
                alerts.append(msg)
                rec_message = f"💡 <strong>{row['Product']}</strong> is expiring soon! Consider cooking a recipe using it today."
            else:
                fresh_count += 1
        except Exception:
            pass

# Eco Score Calculation
overdue_leftovers = len(leftovers_df[leftovers_df["Days Stored"] > 3]) if not leftovers_df.empty and "Days Stored" in leftovers_df.columns else 0
raw_score = 100 - (expired_count * 5) - (overdue_leftovers * 2) + (fresh_count * 1)
eco_score = max(0, min(100, raw_score))

# --- Next-Gen Glassmorphic UI Styling ---
st.markdown("""
    <style>
    /* Force-remove default Streamlit horizontal lines */
    hr {
        display: none !important;
    }

    /* Global Page Styling */
    .stApp {
        background-color: #0B0F0D;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        max-width: 1100px;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #101412 !important;
        border-right: 1px solid rgba(0, 255, 135, 0.12);
    }

    div[data-testid="stSidebarNav"] ul {
        padding-top: 1rem;
    }

    div[data-testid="stSidebarNav"] li a {
        border-radius: 12px !important;
        margin: 4px 10px !important;
        padding: 10px 16px !important;
        transition: all 0.3s ease !important;
        color: #9EAB9C !important;
        font-weight: 500 !important;
    }

    div[data-testid="stSidebarNav"] li a:hover {
        background: rgba(0, 255, 135, 0.08) !important;
        color: #00FF87 !important;
        transform: translateX(4px);
    }

    div[data-testid="stSidebarNav"] li a[aria-selected="true"] {
        background: linear-gradient(90deg, rgba(0, 255, 135, 0.2) 0%, rgba(0, 255, 135, 0.02) 100%) !important;
        border-left: 3px solid #00FF87 !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* Hero Typography */
    .hero-title {
        text-align: center;
        font-size: 3.6rem !important;
        font-weight: 900;
        background: linear-gradient(135deg, #A8E6CF 0%, #00FF87 50%, #2E7D32 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1.2px;
        margin-bottom: 0.3rem;
        filter: drop-shadow(0 0 25px rgba(0, 255, 135, 0.35));
    }
    
    .hero-subtitle {
        text-align: center;
        font-size: 1.15rem !important;
        font-weight: 400;
        color: #8E9B90 !important;
        margin-bottom: 2rem;
        letter-spacing: 0.2px;
    }

    /* Glowing Logo Ring */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0.5rem 0 2.5rem 0;
    }

    .logo-wrapper {
        padding: 8px;
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(0, 255, 135, 0.3), rgba(0, 255, 135, 0.05));
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6), 0 0 25px rgba(0, 255, 135, 0.25);
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .logo-wrapper:hover {
        transform: scale(1.04);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8), 0 0 35px rgba(0, 255, 135, 0.45);
    }

    .logo-wrapper img {
        max-width: 200px;
        width: 100%;
        border-radius: 20px;
        display: block;
    }

    /* Metric Dashboard Grid */
    .stats-banner {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.2rem;
        margin-bottom: 2rem;
    }

    .stat-card {
        background: rgba(20, 26, 23, 0.75);
        border: 1px solid rgba(0, 255, 135, 0.15);
        border-radius: 18px;
        padding: 1.4rem 1rem;
        text-align: center;
        backdrop-filter: blur(14px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
        transition: all 0.35s ease;
        position: relative;
        overflow: hidden;
    }

    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #00FF87, transparent);
        opacity: 0.6;
    }

    .stat-card:hover {
        border-color: rgba(0, 255, 135, 0.4);
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(0, 255, 135, 0.15);
    }

    .stat-number {
        font-size: 2.2rem;
        font-weight: 800;
        color: #00FF87;
        text-shadow: 0 0 12px rgba(0, 255, 135, 0.3);
    }

    .stat-label {
        font-size: 0.82rem;
        color: #8E9B90;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-top: 0.3rem;
    }

    /* Alert Banner */
    .alert-box {
        background: rgba(255, 75, 75, 0.08);
        border: 1px solid rgba(255, 75, 75, 0.3);
        border-radius: 18px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.8rem;
        backdrop-filter: blur(10px);
    }
    
    .alert-item {
        color: #FF8A8A;
        font-size: 0.95rem;
        margin-bottom: 0.4rem;
    }

    /* AI Recommendation Card */
    .rec-box {
        background: rgba(0, 255, 135, 0.06);
        border: 1px solid rgba(0, 255, 135, 0.2);
        border-left: 5px solid #00FF87;
        border-radius: 0 18px 18px 0;
        padding: 1.25rem 1.5rem;
        margin-bottom: 2.2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    /* Section Headers */
    .section-title {
        color: #E0E0E0;
        font-size: 1.35rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Action Buttons Styling */
    div.stButton > button {
        background: rgba(20, 26, 23, 0.8) !important;
        border: 1px solid rgba(0, 255, 135, 0.25) !important;
        color: #00FF87 !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        height: 3.6rem !important;
        transition: all 0.3s ease !important;
        width: 100%;
        backdrop-filter: blur(8px);
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #00FF87 0%, #1B5E20 100%) !important;
        color: #080C0A !important;
        border-color: #00FF87 !important;
        box-shadow: 0 0 25px rgba(0, 255, 135, 0.45) !important;
        transform: translateY(-2px);
    }

    /* Feature Capabilities Grid */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.2rem;
        margin-top: 1rem;
        margin-bottom: 2.5rem;
    }

    .feature-card {
        background: rgba(20, 26, 23, 0.7);
        border: 1px solid rgba(0, 255, 135, 0.15);
        border-radius: 20px;
        padding: 1.6rem;
        transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        backdrop-filter: blur(12px);
    }

    .feature-card:hover {
        transform: translateY(-4px);
        border-color: rgba(0, 255, 135, 0.4);
        box-shadow: 0 10px 30px rgba(0, 255, 135, 0.12);
        background: rgba(26, 33, 29, 0.85);
    }

    .feature-icon {
        font-size: 2.2rem;
        margin-bottom: 0.8rem;
    }

    .feature-title {
        color: #00FF87;
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .feature-desc {
        color: #B0BEC5;
        font-size: 0.92rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("<h1 class='hero-title'>🌿 EcoPantry</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>AI-Powered Smart Food Waste Management & Pantry Tracker</p>", unsafe_allow_html=True)

# --- Logo Display ---
if logo_b64:
    st.markdown(
        f"""
        <div class="logo-container">
            <div class="logo-wrapper">
                <img src="data:image/png;base64,{logo_b64}" alt="EcoPantry Logo">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Dynamic Metrics Banner ---
st.markdown(f"""
<div class="stats-banner">
    <div class="stat-card">
        <div class="stat-number">{total_pantry}</div>
        <div class="stat-label">Pantry Items</div>
    </div>
    <div class="stat-card">
        <div class="stat-number" style="color: #FFB74D; text-shadow: 0 0 12px rgba(255, 183, 77, 0.3);">{expiring_soon_count}</div>
        <div class="stat-label">Expiring Soon</div>
    </div>
    <div class="stat-card">
        <div class="stat-number" style="color: #64B5F6; text-shadow: 0 0 12px rgba(100, 181, 246, 0.3);">{total_leftovers}</div>
        <div class="stat-label">Leftovers</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{eco_score}%</div>
        <div class="stat-label">Eco Score</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Tip of the Day ---
tips = [
    "🍌 Store bananas away from other fruits to prevent them from ripening too fast.",
    "🌿 Freeze fresh herbs in olive oil using ice cube trays for easy cooking portioning.",
    "🥔 Keep potatoes away from onions; ethylene gas from onions causes potatoes to sprout.",
    "🍞 Store bread in the freezer instead of the fridge to prevent it from going stale.",
    "🥬 Wrap leafy greens in paper towels before refrigerating to absorb excess moisture."
]
st.info(f"💡 **Tip of the Day:** {random.choice(tips)}")

# --- Smart Alerts ---
if alerts:
    st.markdown('<div class="alert-box"><h4 style="color:#FF6B6B; margin:0 0 8px 0; font-weight:700;">🔔 Today\'s Urgent Alerts</h4>' + "".join([f'<div class="alert-item">{a}</div>' for a in alerts]) + '</div>', unsafe_allow_html=True)

# --- AI Recommendation Box ---
st.markdown(f"""
    <div class="rec-box">
        <h4 style="color: #00FF87; margin:0 0 6px 0; font-weight: 700; font-size: 1.05rem;">🤖 AI Insights & Recommendations</h4>
        <p style="color: #E0E0E0; margin:0; font-size: 0.95rem; line-height: 1.5;">{rec_message}</p>
    </div>
""", unsafe_allow_html=True)

# --- Quick Navigation Buttons ---
st.markdown("<div class='section-title'>⚡ Quick Dashboard Navigation</div>", unsafe_allow_html=True)

b2, b3, b4, b5, b6, b7, b8, b9 = st.columns(8)

def safe_navigate(page_path):
    try:
        st.switch_page(page_path)
    except Exception:
        st.error(f"Could not open page `{page_path}`. Please check your `pages/` directory.")

if b2.button("📋 Pantry", key="btn_pantry"):
    safe_navigate("pages/2_Pantry.py")

if b3.button("🍽 Leftovers", key="btn_leftovers"):
    safe_navigate("pages/3_Leftovers.py")

if b4.button("🤖 Assistant", key="btn_chatbot"):
    safe_navigate("pages/4_Chatbot.py")

if b5.button("ℹ️ About", key="btn_about"):
    safe_navigate("pages/5_About.py")

if b6.button("📊 Analytics", key="btn_analytics"):
    safe_navigate("pages/analytics.py")

if b7.button("📖 Recipes", key="btn_recipes"):
    safe_navigate("pages/recipe.py")

if b8.button("📷Scanner", key="btn_scanner"):
    safe_navigate("pages/scanner.py")
if b9.button("🍽️ Waste Auditor", key="btn_waste_auditor"):
    safe_navigate("pages/8_Waste_Auditor.py")

st.write("")

# --- Global Inventory Search ---
search_query = st.text_input("🔍 Quick Inventory Search...", placeholder="Type product or ingredient name (e.g., Milk, Eggs, Rice)...")
if search_query:
    filtered_pantry = pantry_df[pantry_df["Product"].str.contains(search_query, case=False, na=False)] if not pantry_df.empty else pd.DataFrame()
    st.markdown("### 🔎 Matching Results")
    if not filtered_pantry.empty:
        st.dataframe(filtered_pantry, use_container_width=True)
    else:
        st.caption("No matching items found in your active pantry.")
    st.write("")

# --- Feature Capabilities Grid ---
st.markdown("<div class='section-title'>🚀 Core System Capabilities</div>", unsafe_allow_html=True)

st.markdown("""
<div class="grid-container">
    <div class="feature-card">
        <div class="feature-icon">📦</div>
        <div class="feature-title">Smart Item Logger</div>
        <div class="feature-desc">Instantly log packaged and fresh groceries with automated expiration date calculators and storage tags.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📋</div>
        <div class="feature-title">Live Inventory Monitor</div>
        <div class="feature-desc">Keep active track of shelf life with color-coded freshness badges, sorting filters, and expiry countdowns.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🍽️</div>
        <div class="feature-title">Leftover Auto-Manager</div>
        <div class="feature-desc">Smart tracking algorithms highlight safe refrigerator storage durations for cooked food to prevent waste.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">EcoPantry AI Copilot</div>
        <div class="feature-desc">Chat directly with our integrated AI assistant to craft custom recipes using ingredients expiring soon in your pantry.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Floating Glowing Assistant Drawer Injection ---
def render_floating_bot():
    bot_code = """
    <script>
    (function() {
        if (window.parent.document.getElementById('ecopantry-chat-widget')) return;

        const container = window.parent.document.createElement('div');
        container.id = 'ecopantry-chat-widget';
        container.style.cssText = `
            position: fixed;
            bottom: 25px;
            right: 25px;
            z-index: 999999;
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 12px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        `;

        const modal = window.parent.document.createElement('div');
        modal.id = 'ecopantry-chat-modal';
        modal.style.cssText = `
            display: none;
            width: 380px;
            height: 580px;
            background: #1A1F1C;
            border: 1px solid rgba(0, 255, 135, 0.4);
            border-radius: 20px;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.7), 0 0 20px rgba(0, 255, 135, 0.2);
            overflow: hidden;
            transition: all 0.3s ease;
        `;

        modal.innerHTML = `
            <iframe
                src="https://www.chatbase.co/chatbot-iframe/voXMr1BILlDLuXX4wRTSy"
                width="100%"
                height="100%"
                frameborder="0"
                allow="microphone"
            ></iframe>
        `;

        const botBar = window.parent.document.createElement('div');
        botBar.style.cssText = `
            display: flex;
            align-items: center;
            gap: 12px;
        `;

        const tooltip = window.parent.document.createElement('div');
        tooltip.id = 'ecopantry-chat-tooltip';
        tooltip.innerHTML = "Hi! I'm your EcoPantry assistant 👋";
        tooltip.style.cssText = `
            background: rgba(26, 31, 28, 0.95);
            color: #E0E0E0;
            border: 1px solid rgba(0, 255, 135, 0.3);
            padding: 10px 18px;
            border-radius: 20px;
            font-size: 0.88rem;
            font-weight: 600;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(8px);
            white-space: nowrap;
            transition: all 0.3s ease;
        `;

        const btn = window.parent.document.createElement('button');
        btn.innerHTML = `
            <svg id="bot-svg-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00FF87" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: all 0.3s ease;">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                <path d="M12 8l1 2 2 1-2 1-1 2-1-2-2-1 2-1z"></path>
            </svg>
        `;
        btn.style.cssText = `
            background: #121614;
            border: 1px solid rgba(0, 255, 135, 0.4);
            width: 56px;
            height: 56px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 8px 20px rgba(0,0,0,0.5), 0 0 10px rgba(0, 255, 135, 0.2);
            transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        `;

        btn.onmouseover = () => { 
            btn.style.transform = 'scale(1.12)';
            btn.style.borderColor = '#00FF87';
            btn.style.boxShadow = '0 0 25px rgba(0, 255, 135, 0.7), 0 0 50px rgba(0, 255, 135, 0.3), 0 8px 20px rgba(0,0,0,0.6)';
            btn.style.background = '#1A231D';
            
            tooltip.style.borderColor = '#00FF87';
            tooltip.style.boxShadow = '0 0 15px rgba(0, 255, 135, 0.4)';

            const svgIcon = btn.querySelector('#bot-svg-icon');
            if (svgIcon) svgIcon.setAttribute('stroke', '#81C784');
        };

        btn.onmouseout = () => { 
            btn.style.transform = 'scale(1)';
            btn.style.borderColor = 'rgba(0, 255, 135, 0.4)';
            btn.style.boxShadow = '0 8px 20px rgba(0,0,0,0.5), 0 0 10px rgba(0, 255, 135, 0.2)';
            btn.style.background = '#121614';

            tooltip.style.borderColor = 'rgba(0, 255, 135, 0.3)';
            tooltip.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.4)';

            const svgIcon = btn.querySelector('#bot-svg-icon');
            if (svgIcon) svgIcon.setAttribute('stroke', '#00FF87');
        };

        let isOpen = false;
        btn.onclick = () => {
            isOpen = !isOpen;
            if (isOpen) {
                modal.style.display = 'block';
                tooltip.style.display = 'none';
            } else {
                modal.style.display = 'none';
                tooltip.style.display = 'block';
            }
        };

        botBar.appendChild(tooltip);
        botBar.appendChild(btn);
        container.appendChild(modal);
        container.appendChild(botBar);
        window.parent.document.body.appendChild(container);
    })();
    </script>
    """
    components.html(bot_code, height=0, width=0)

render_floating_bot()

# --- Footer Section ---
st.markdown("""
    <div style="
        text-align: center;
        width: 100%;
        margin-top: 3rem;
        padding-top: 1.8rem;
        padding-bottom: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        color: #6C7A70;
        font-size: 0.88rem;
        line-height: 1.6;
    ">
        <strong style="color: #00FF87;">EcoPantry</strong> — Reducing Household Food Waste Since 2026<br>
        <span style="opacity: 0.8;">Made with Python • Streamlit • Pandas • AI</span>
    </div>
""", unsafe_allow_html=True)