import streamlit as st
import streamlit.components.v1 as components
from style import apply_custom_sidebar_style

# --- Initial Setup ---
apply_custom_sidebar_style()

st.set_page_config(
    page_title="AI Assistant - EcoPantry",
    page_icon="🤖",
    layout="wide"
)

# --- EcoPantry Award-Winning Theme Styling (CSS) ---
st.markdown("""
    <style>
    /* Force-remove default Streamlit horizontal rules */
    hr {
        display: none !important;
    }

    /* Global Page Styling */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #131F19 0%, #080C0A 100%);
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px;
    }

    /* Header & Hero Section */
    .hero-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(0, 255, 135, 0.15);
        padding-bottom: 1.5rem;
        margin-bottom: 1.8rem;
    }

    .page-title {
        background: linear-gradient(135deg, #A8E6CF 0%, #00FF87 50%, #2E7D32 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.8rem;
        letter-spacing: -0.8px;
        margin: 0;
    }
    
    .page-subtitle {
        color: #8E9B90;
        font-size: 1.05rem;
        margin-top: 0.4rem;
    }

    /* System Status Indicator */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(0, 255, 135, 0.08);
        border: 1px solid rgba(0, 255, 135, 0.3);
        padding: 8px 16px;
        border-radius: 30px;
        color: #00FF87;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        box-shadow: 0 0 15px rgba(0, 255, 135, 0.15);
    }

    .pulse-dot {
        width: 8px;
        height: 8px;
        background-color: #00FF87;
        border-radius: 50%;
        box-shadow: 0 0 8px #00FF87;
        animation: pulse 1.8s infinite;
    }

    @keyframes pulse {
        0% { opacity: 0.4; transform: scale(0.9); }
        50% { opacity: 1; transform: scale(1.2); }
        100% { opacity: 0.4; transform: scale(0.9); }
    }

    /* Capabilities Dashboard Grid */
    .cap-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.25rem;
        margin-bottom: 1.8rem;
    }

    .cap-card {
        background: linear-gradient(145deg, rgba(22, 30, 26, 0.7), rgba(12, 16, 14, 0.8));
        border: 1px solid rgba(0, 255, 135, 0.15);
        border-radius: 16px;
        padding: 1.25rem;
        backdrop-filter: blur(12px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
    }

    .cap-card:hover {
        border-color: rgba(0, 255, 135, 0.4);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 255, 135, 0.15);
    }

    .cap-icon {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }

    .cap-title {
        color: #E0E0E0;
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }

    .cap-desc {
        color: #7A8A7E;
        font-size: 0.82rem;
        line-height: 1.4;
    }

    /* Suggested Prompts Bar */
    .prompts-container {
        background: rgba(18, 24, 21, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1rem 1.25rem;
        margin-bottom: 1.5rem;
    }

    .prompts-header {
        color: #00FF87;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 0.75rem;
    }

    .prompt-chip {
        display: inline-block;
        background: rgba(26, 35, 30, 0.8);
        border: 1px solid rgba(0, 255, 135, 0.2);
        color: #C8E6C9;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        margin-right: 8px;
        margin-bottom: 8px;
        cursor: pointer;
        transition: all 0.25s ease;
    }

    .prompt-chip:hover {
        background: rgba(0, 255, 135, 0.15);
        border-color: #00FF87;
        color: #FFFFFF;
        box-shadow: 0 0 12px rgba(0, 255, 135, 0.2);
    }

    /* Chat Frame Container */
    .chat-wrapper {
        border-radius: 22px;
        overflow: hidden;
        border: 1px solid rgba(0, 255, 135, 0.3);
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.7), 0 0 30px rgba(0, 255, 135, 0.12);
        background-color: #121714;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header & Status Section ---
st.markdown("""
    <div class="hero-container">
        <div>
            <h1 class="page-title">🤖 EcoPantry AI Assistant</h1>
            <p class="page-subtitle">Your real-time culinary intelligence hub for recipe generation, shelf-life advice, and zero-waste storage.</p>
        </div>
        <div class="status-badge">
            <span class="pulse-dot"></span>
            <span>AI CORE ONLINE</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Capabilities Overview Grid ---
st.markdown("""
    <div class="cap-grid">
        <div class="cap-card">
            <div class="cap-icon">🥗</div>
            <div class="cap-title">Leftover Recipes</div>
            <div class="cap-desc">Transform cooked portions into fresh, delicious gourmet meals instantly.</div>
        </div>
        <div class="cap-card">
            <div class="cap-icon">📅</div>
            <div class="cap-title">Safe Shelf-Life</div>
            <div class="cap-desc">Check optimal storage guidelines for dairy, meat, grains, and produce.</div>
        </div>
        <div class="cap-card">
            <div class="cap-icon">🧊</div>
            <div class="cap-title">Freezer Hacks</div>
            <div class="cap-desc">Learn smart prep and freezing techniques to double ingredient lifespan.</div>
        </div>
        <div class="cap-card">
            <div class="cap-icon">♻️</div>
            <div class="cap-title">Zero-Waste Tips</div>
            <div class="cap-desc">Get actionable steps to reduce household organic waste effectively.</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Interactive Quick Prompts Section ---
st.markdown("""
    <div class="prompts-container">
        <div class="prompts-header">💡 Try asking the AI Assistant:</div>
        <div style="display: flex; flex-wrap: wrap;">
            <span class="prompt-chip">"What can I cook with leftover cooked rice and spinach?"</span>
            <span class="prompt-chip">"How long does paneer butter masala last in the fridge?"</span>
            <span class="prompt-chip">"Give me 3 zero-waste storage tips for fresh herbs."</span>
            <span class="prompt-chip">"Can I safely freeze cooked lentil dal?"</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Embedded Chatbot Experience ---
st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)

components.html(
    """
    <iframe
        src="https://www.chatbase.co/chatbot-iframe/voXMr1BILlDLuXX4wRTSy"
        width="100%"
        style="height: 100%; min-height: 720px; border: none; border-radius: 20px;"
        allow="microphone"
    ></iframe>
    """,
    height=720,
    scrolling=False,
)

st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div style="
        text-align: center;
        width: 100%;
        margin-top: 3rem;
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        color: #6C7A70;
        font-size: 0.88rem;
        line-height: 1.6;
    ">
        <strong style="color: #00FF87;">EcoPantry AI Assistant</strong> — Powered by Intelligent Culinary Models<br>
        <span style="opacity: 0.8;">Made with Python • Streamlit • Chatbase AI</span>
    </div>
""", unsafe_allow_html=True)