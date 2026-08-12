import streamlit as st
import streamlit.components.v1 as components
from style import apply_custom_sidebar_style

# --- Initial Setup & Sidebar ---
apply_custom_sidebar_style()

st.set_page_config(
    page_title="About - EcoPantry",
    page_icon="🌿",
    layout="wide"
)

# --- Custom Styling (CSS) ---
st.markdown("""
    <style>
    /* Global Page Background */
    .stApp {
        background-color: #0E1311;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        max-width: 1050px;
    }

    /* Modern Glow Typography */
    .hero-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 0.3rem;
    }
    
    .page-title {
        background: linear-gradient(135deg, #A8E6CF 0%, #00FF87 50%, #2E7D32 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.6rem;
        letter-spacing: -0.5px;
        filter: drop-shadow(0 0 12px rgba(0, 255, 135, 0.3));
    }
    
    .page-subtitle {
        color: #8E9B90;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    /* Glassmorphic Feature Cards */
    .about-card {
        background: rgba(22, 28, 25, 0.85);
        border: 1px solid rgba(0, 255, 135, 0.18);
        border-radius: 20px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), inset 0 0 10px rgba(0, 255, 135, 0.05);
        backdrop-filter: blur(12px);
        transition: all 0.35s ease;
    }

    .about-card:hover {
        border-color: rgba(0, 255, 135, 0.4);
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0, 255, 135, 0.12);
    }

    .card-title {
        color: #00FF87;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        text-shadow: 0 0 8px rgba(0, 255, 135, 0.3);
    }

    .card-text {
        color: #E0E0E0;
        font-size: 0.98rem;
        line-height: 1.6;
    }

    .card-text ul {
        margin-top: 0.4rem;
        padding-left: 1.2rem;
    }

    .card-text li {
        margin-bottom: 0.4rem;
    }

    /* Highlight Box */
    .highlight-box {
        background: rgba(0, 255, 135, 0.06);
        border-left: 4px solid #00FF87;
        padding: 0.8rem 1.2rem;
        border-radius: 0 12px 12px 0;
        margin-top: 1rem;
        font-size: 0.92rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6C7A70;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
    <div class="hero-header">
        <h1 class="page-title">🌿 About EcoPantry</h1>
    </div>
    <p class="page-subtitle">Learn about our mission to revolutionize kitchen management and eliminate household food waste.</p>
""", unsafe_allow_html=True)

# --- Combined Content Grid ---
col1, col2 = st.columns(2)

with col1:
    # Mission Card
    st.markdown("""
        <div class="about-card">
            <div class="card-title">🚀 Our Mission</div>
            <div class="card-text">
                Every year, millions of tons of fresh food are wasted simply due to overlooked expiration dates and inefficient storage. 
                <strong>EcoPantry</strong> aims to empower households to reduce food waste, optimize grocery spending, and build sustainable cooking habits through automated tracking and AI insights.
            </div>
            <div class="highlight-box">
                <span style="color: #00FF87; font-weight: bold;">Goal:</span> Reduce household grocery waste by up to 30%.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # UN SDG Goal Card
    st.markdown("""
        <div class="about-card">
            <div class="card-title">🌍 UN SDG Goal 12</div>
            <div class="card-text">
                We align with United Nations Sustainable Development Goal 12: <strong>Responsible Consumption and Production</strong> (SDG 12.3) to halve per capita global food waste at the retail and consumer levels.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Core Features Card
    st.markdown("""
        <div class="about-card">
            <div class="card-title">⚡ Smart Core Features</div>
            <div class="card-text">
                <ul>
                    <li><strong>📷 Barcode & Vision Logger:</strong> Instantly scan and log packaged groceries.</li>
                    <li><strong>📦 Real-time Tracker:</strong> Dynamic freshness badges & expiry countdowns.</li>
                    <li><strong>🍳 Leftover Magic:</strong> AI recipe ideas utilizing remaining inventory.</li>
                    <li><strong>💬 Assistant Drawer:</strong> 24/7 AI guide for food preservation queries.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Technologies Card
    st.markdown("""
        <div class="about-card">
            <div class="card-title">🛠️ Technologies Used</div>
            <div class="card-text">
                <ul>
                    <li><strong>Frontend / Framework:</strong> Streamlit</li>
                    <li><strong>Data Processing:</strong> Pandas, NumPy</li>
                    <li><strong>Data Visualizations:</strong> Plotly</li>
                    <li><strong>Computer Vision & AI:</strong> OpenCV, Gemini Vision API</li>
                    <li><strong>AI Chatbot:</strong> Embedded Chatbase Widget</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Future Scope Card
    st.markdown("""
        <div class="about-card">
            <div class="card-title">🚀 Future Scope</div>
            <div class="card-text">
                <ul>
                    <li><strong>IoT Hardware:</strong> Smart Refrigerator camera & weight sensor integration.</li>
                    <li><strong>OCR Receipt Reader:</strong> Automated grocery receipt scanning and item intake.</li>
                    <li><strong>Community Sharing:</strong> Local peer-to-peer excess food donation portal.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# --- Floating Chatbot Widget Injection ---
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

# --- Footer ---
st.divider()
st.markdown("""
    <div style="
        text-align: center;
        width: 100%;
        padding: 1.5rem 0 2rem 0;
        color: #6C7A70;
        font-size: 0.88rem;
        line-height: 1.6;
    ">
        <strong style="color: #00FF87;">EcoPantry</strong> — Reducing Food Waste Since 2026<br>
        <span style="opacity: 0.8;">Made with Python • Streamlit • Pandas • AI</span>
    </div>
""", unsafe_allow_html=True) 
import streamlit as st
import streamlit.components.v1 as components
from style import apply_custom_sidebar_style

# --- Initial Setup & Sidebar ---
apply_custom_sidebar_style()

st.set_page_config(
    page_title="About - EcoPantry",
    page_icon="🌿",
    layout="wide"
)

# --- Award-Winning Custom Styling (CSS) ---
st.markdown("""
    <style>
    /* Force-remove all default Streamlit horizontal lines/dividers */
    hr {
        display: none !important;
    }

    /* Global Page Canvas */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #111A15 0%, #080C0A 100%);
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1180px;
    }

    /* Hero Typography */
    .hero-container {
        border-bottom: 1px solid rgba(0, 255, 135, 0.15);
        padding-bottom: 1.5rem;
        margin-bottom: 2rem;
    }

    .page-title {
        background: linear-gradient(135deg, #A8E6CF 0%, #00FF87 50%, #2E7D32 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.8rem;
        letter-spacing: -0.8px;
        margin: 0;
        filter: drop-shadow(0 0 15px rgba(0, 255, 135, 0.25));
    }
    
    .page-subtitle {
        color: #8E9B90;
        font-size: 1.05rem;
        margin-top: 0.4rem;
    }

    /* Global Impact Stat Metrics */
    .impact-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.25rem;
        margin-bottom: 2rem;
    }

    .impact-card {
        background: rgba(18, 25, 21, 0.75);
        border: 1px solid rgba(0, 255, 135, 0.2);
        border-radius: 18px;
        padding: 1.25rem 1.5rem;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }

    .impact-card:hover {
        transform: translateY(-3px);
        border-color: rgba(0, 255, 135, 0.45);
        box-shadow: 0 12px 30px rgba(0, 255, 135, 0.15);
    }

    .impact-number {
        font-size: 2rem;
        font-weight: 900;
        color: #00FF87;
        margin-bottom: 0.2rem;
    }

    .impact-label {
        color: #8E9B90;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* SDG Highlight Banner */
    .sdg-banner {
        background: linear-gradient(135deg, rgba(0, 255, 135, 0.1) 0%, rgba(46, 125, 50, 0.08) 100%);
        border: 1px solid rgba(0, 255, 135, 0.3);
        border-radius: 18px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        gap: 1.25rem;
        backdrop-filter: blur(10px);
    }

    .sdg-icon {
        font-size: 2.8rem;
        line-height: 1;
    }

    .sdg-title {
        color: #00FF87;
        font-size: 1.2rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }

    .sdg-text {
        color: #D0E3D4;
        font-size: 0.95rem;
        line-height: 1.5;
        margin: 0;
    }

    /* Glassmorphic Cards */
    .about-card {
        background: linear-gradient(145deg, rgba(22, 30, 26, 0.75), rgba(12, 16, 14, 0.85));
        border: 1px solid rgba(0, 255, 135, 0.18);
        border-radius: 20px;
        padding: 1.75rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 32px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
    }

    .about-card:hover {
        border-color: rgba(0, 255, 135, 0.4);
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0, 255, 135, 0.12);
    }

    .card-title {
        color: #00FF87;
        font-size: 1.25rem;
        font-weight: 800;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .card-text {
        color: #E0E0E0;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* Tech Stack Badges */
    .tech-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 0.8rem;
    }

    .tech-pill {
        background: rgba(0, 255, 135, 0.08);
        border: 1px solid rgba(0, 255, 135, 0.25);
        color: #A8E6CF;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        transition: all 0.25s ease;
    }

    .tech-pill:hover {
        background: rgba(0, 255, 135, 0.2);
        color: #FFFFFF;
        border-color: #00FF87;
        box-shadow: 0 0 10px rgba(0, 255, 135, 0.2);
    }

    /* Highlight Container */
    .highlight-box {
        background: rgba(0, 255, 135, 0.06);
        border-left: 4px solid #00FF87;
        padding: 0.85rem 1.2rem;
        border-radius: 0 12px 12px 0;
        margin-top: 1.2rem;
        font-size: 0.92rem;
        color: #C8E6C9;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
    <div class="hero-container">
        <h1 class="page-title">🌿 About EcoPantry</h1>
        <p class="page-subtitle">Revolutionizing kitchen inventory management through automation, computer vision, and AI-driven sustainability.</p>
    </div>
""", unsafe_allow_html=True)

# --- Impact Metrics Overview ---
st.markdown("""
    <div class="impact-grid">
        <div class="impact-card">
            <div class="impact-number">1.3 Billion</div>
            <div class="impact-label">Tons of Food Wasted Annually</div>
        </div>
        <div class="impact-card">
            <div class="impact-number">30%</div>
            <div class="impact-label">Target Household Reduction</div>
        </div>
        <div class="impact-card">
            <div class="impact-number">100%</div>
            <div class="impact-label">Automated Freshness Tracking</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- UN SDG Alignment Banner ---
st.markdown("""
    <div class="sdg-banner">
        <div class="sdg-icon">🌍</div>
        <div>
            <div class="sdg-title">United Nations SDG Goal 12: Responsible Consumption</div>
            <p class="sdg-text">
                EcoPantry directly aligns with <b>Target 12.3</b> to halve global per capita food waste at retail and consumer levels by equipping households with intelligent expiration reminders and leftover recipe intelligence.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Main Feature & Tech Grid ---
col1, col2 = st.columns(2)

with col1:
    # Mission Card
    st.markdown("""
        <div class="about-card">
            <div class="card-title">🚀 Our Mission</div>
            <div class="card-text">
                Every year, households lose hundreds of dollars in spoiled groceries due to overlooked storage dates and disorganization. 
                <strong>EcoPantry</strong> bridges this gap by transforming everyday kitchens into proactive, zero-waste hubs through real-time freshness telemetry and computer vision.
            </div>
            <div class="highlight-box">
                <b>Core Purpose:</b> Eliminate unnecessary food waste, save consumer expenditure, and foster sustainable eating habits seamlessly.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Core Features Card
    st.markdown("""
        <div class="about-card">
            <div class="card-title">⚡ Core Innovations</div>
            <div class="card-text">
                <ul style="padding-left: 1.2rem; margin: 0;">
                    <li style="margin-bottom: 0.5rem;"><b>📷 Barcode & Vision Scanner:</b> Auto-extract product metadata and store dates instantly.</li>
                    <li style="margin-bottom: 0.5rem;"><b>📊 Freshness Ledger:</b> Visual progress bars showing remaining shelf life at a glance.</li>
                    <li style="margin-bottom: 0.5rem;"><b>🍳 Leftover Recipe Engine:</b> Dynamic AI meal generation based on expiring ingredients.</li>
                    <li style="margin-bottom: 0.5rem;"><b>🤖 24/7 AI Culinary Assistant:</b> On-demand shelf-life, freezing, and preservation advice.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Technology Stack Card
    st.markdown("""
        <div class="about-card">
            <div class="card-title">🛠️ Technology Stack</div>
            <div class="card-text">
                Built using modern Python ecosystem tools for speed, scalability, and seamless user interaction:
                <div class="tech-grid">
                    <span class="tech-pill">Python 3.11</span>
                    <span class="tech-pill">Streamlit UI</span>
                    <span class="tech-pill">Pandas Dataframes</span>
                    <span class="tech-pill">OpenCV Computer Vision</span>
                    <span class="tech-pill">Gemini Vision API</span>
                    <span class="tech-pill">Plotly Analytics</span>
                    <span class="tech-pill">Chatbase AI Assistant</span>
                    <span class="tech-pill">Custom CSS Glassmorphism</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Future Scope Card
    st.markdown("""
        <div class="about-card">
            <div class="card-title">🔮 Future Expansion</div>
            <div class="card-text">
                <ul style="padding-left: 1.2rem; margin: 0;">
                    <li style="margin-bottom: 0.5rem;"><b>📡 Smart Fridge IoT:</b> Integrated camera sensors for automated inventory updates.</li>
                    <li style="margin-bottom: 0.5rem;"><b>🧾 Receipt OCR Reader:</b> Scan grocery store receipts for instantaneous bulk logging.</li>
                    <li style="margin-bottom: 0.5rem;"><b>🤝 Community Food Sharing:</b> Peer-to-peer portal to donate surplus unexpired items locally.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- Floating Chatbot Widget Injection ---
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

# --- Footer ---
st.markdown("""
    <div style="
        text-align: center;
        width: 100%;
        margin-top: 2.5rem;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        color: #6C7A70;
        font-size: 0.88rem;
        line-height: 1.6;
    ">
        <strong style="color: #00FF87;">EcoPantry</strong> — Smart Zero-Waste Kitchen Management System<br>
        <span style="opacity: 0.8;">Built with Python • Streamlit • Pandas • AI</span>
    </div>
""", unsafe_allow_html=True)