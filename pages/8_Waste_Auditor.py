import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import random
from style import apply_custom_sidebar_style

# --- Page Config ---
st.set_page_config(
    page_title="AI Food Waste Auditor",
    page_icon="🍽️",
    layout="wide"
)

# --- Apply Custom Sidebar Theme ---
apply_custom_sidebar_style()

# --- Custom Page Styling ---
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 950px;
    }
    
    /* Neon Green Glow Heading */
    .page-title {
        color: #00FF87 !important;
        font-weight: 800;
        font-size: 2.3rem;
        margin-bottom: 0.2rem;
        text-shadow: 0 0 10px rgba(0, 255, 135, 0.5), 
                     0 0 20px rgba(0, 255, 135, 0.3);
    }
    
    .page-subtitle {
        color: #A3B18A;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }

    /* Container Box Styling */
    div[data-testid="stForm"], .stMetric, .info-card {
        background-color: #1A1F1C;
        border: 1px solid #2D3732;
        border-radius: 12px;
        padding: 1rem;
    }

    /* Custom Button Styling */
    div.stButton > button {
        background-color: #2E7D32 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.6rem 2rem !important;
        width: 100%;
        margin-top: 0.5rem;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background-color: #388E3C !important;
        box-shadow: 0 0 15px rgba(0, 255, 135, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("<h1 class='page-title'>🍽️ AI Food Waste Auditor</h1>", unsafe_allow_html=True)
st.markdown("<p class='page-subtitle'>Upload a photo of your plate after eating to analyze leftover food waste and environmental impact.</p>", unsafe_allow_html=True)

# --- File Uploader ---
uploaded = st.file_uploader(
    "Upload Plate Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 📸 Uploaded Plate")
        image = Image.open(uploaded)
        st.image(image, use_container_width=True)
        analyze_btn = st.button("Analyze Plate")

    with col2:
        if analyze_btn:
            # Simulated audit logic
            waste = random.randint(80, 250)
            nutrition = random.randint(50, 100)
            calories = random.randint(250, 900)
            percent = random.randint(20, 60)
            money = waste * 0.25
            co2 = round(waste * 0.002, 2)

            st.success("Analysis Complete")
            st.markdown("### 📊 Audit Metrics")

            # Displaying metrics in neat grids
            m1, m2 = st.columns(2)
            m1.metric("Nutrition Score", f"{nutrition}/100")
            m2.metric("Estimated Waste", f"{waste} g")

            m3, m4 = st.columns(2)
            m3.metric("Waste Percentage", f"{percent}%")
            m4.metric("Estimated Money Lost", f"₹{money:.0f}")

            st.metric("CO₂ Impact", f"{co2} kg")

            st.info(
                "💡 **Tip:** Serve slightly smaller portions next time to reduce food waste."
            )

            st.success("🌍 Supports **SDG 2 (Zero Hunger)** & **SDG 12 (Responsible Consumption)**")


# --- Floating Chatbot Integration ---
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
            background: #121815;
            border: 1px solid rgba(0, 255, 135, 0.4);
            border-radius: 20px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0, 255, 135, 0.15);
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
            background: rgba(18, 26, 22, 0.95);
            color: #E2E8F0;
            border: 1px solid rgba(0, 255, 135, 0.3);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
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
            background: #0E1411;
            border: 1px solid rgba(0, 255, 135, 0.4);
            width: 54px;
            height: 54px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 8px 20px rgba(0,0,0,0.5), 0 0 12px rgba(0, 255, 135, 0.2);
            transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        `;

        btn.onmouseover = () => { 
            btn.style.transform = 'scale(1.1)';
            btn.style.borderColor = '#00FF87';
            btn.style.boxShadow = '0 0 25px rgba(0, 255, 135, 0.6), 0 8px 20px rgba(0,0,0,0.6)';
            btn.style.background = '#141E19';
        };

        btn.onmouseout = () => { 
            btn.style.transform = 'scale(1)';
            btn.style.borderColor = 'rgba(0, 255, 135, 0.4)';
            btn.style.boxShadow = '0 8px 20px rgba(0,0,0,0.5), 0 0 12px rgba(0, 255, 135, 0.2)';
            btn.style.background = '#0E1411';
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