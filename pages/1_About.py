import streamlit as st
import streamlit.components.v1 as components
from style import apply_custom_sidebar_style

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="About - EcoPantry",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_sidebar_style()

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>
.stApp {
    background-color: #0E1311;
}

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
    max-width: 1050px;
}

.hero-header {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 8px;
}

.page-title {
    background: linear-gradient(
        135deg,
        #A8E6CF 0%,
        #00FF87 50%,
        #2E7D32 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: 2.6rem;
    letter-spacing: -0.5px;
    filter: drop-shadow(0 0 12px rgba(0,255,135,0.3));
}

.page-subtitle {
    color: #8E9B90;
    font-size: 1.05rem;
    margin-bottom: 2rem;
}

.about-card {
    background: rgba(22,28,25,0.85);
    border: 1px solid rgba(0,255,135,0.22);
    border-radius: 20px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
    box-shadow:
        0 10px 30px rgba(0,0,0,0.4),
        inset 0 0 10px rgba(0,255,135,0.05);
    backdrop-filter: blur(12px);
}

.about-card:hover {
    border-color: rgba(0,255,135,0.45);
}

.card-title {
    color: #00FF87;
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 0 0 8px rgba(0,255,135,0.3);
}

.card-text {
    color: #E0E0E0;
    font-size: 0.98rem;
    line-height: 1.65;
}

.card-text ul {
    margin: 0;
    padding-left: 1.3rem;
}

.card-text li {
    margin-bottom: 0.7rem;
}

.highlight-box {
    background: rgba(0,255,135,0.06);
    border-left: 4px solid #00FF87;
    padding: 0.8rem 1.2rem;
    border-radius: 0 12px 12px 0;
    margin-top: 1.2rem;
    color: #E0E0E0;
}

.footer {
    text-align: center;
    color: #6C7A70;
    font-size: 0.88rem;
    margin-top: 2rem;
    padding-top: 1.5rem;
}

@media (max-width: 768px) {
    .page-title {
        font-size: 2rem;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero-header"><h1 class="page-title">🌿 About EcoPantry</h1></div>
<p class="page-subtitle">Learn about our mission to revolutionize kitchen management and eliminate household food waste.</p>
""", unsafe_allow_html=True)

# =========================================================
# TWO COLUMN LAYOUT
# =========================================================

col1, col2 = st.columns(2)

# =========================================================
# LEFT COLUMN
# =========================================================

with col1:

    st.markdown("""
<div class="about-card">
<div class="card-title">🚀 Our Mission</div>
<div class="card-text">
Every year, millions of tons of fresh food are wasted simply due to overlooked expiration dates and inefficient storage.
<br><br>
<strong>EcoPantry</strong> aims to empower households to reduce food waste, optimize grocery spending, and build sustainable cooking habits through automated tracking and AI insights.
</div>
<div class="highlight-box">
<span style="color:#00FF87;font-weight:bold;">Goal:</span>
Reduce household grocery waste by up to 30%.
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="about-card">
<div class="card-title">🌍 UN SDG Goal 12</div>
<div class="card-text">
We align with United Nations Sustainable Development Goal 12:
<strong>Responsible Consumption and Production</strong>.
<br><br>
EcoPantry specifically supports SDG 12.3, which focuses on reducing food waste at the retail and consumer levels.
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="about-card">
<div class="card-title">⚡ Smart Core Features</div>
<div class="card-text">
<ul>
<li><strong>📷 Barcode & Vision Scanner:</strong> Quickly scan and log packaged groceries.</li>
<li><strong>📦 Real-Time Pantry:</strong> Track freshness and expiry dates.</li>
<li><strong>🍳 AI Recipes:</strong> Generate recipe ideas using available ingredients.</li>
<li><strong>💬 AI Chatbot:</strong> Get instant food preservation and pantry guidance.</li>
<li><strong>📊 Analytics:</strong> Monitor food waste, savings and sustainability progress.</li>
<li><strong>🔔 Smart Notifications:</strong> Receive reminders about expiring food.</li>
</ul>
</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# RIGHT COLUMN
# =========================================================

with col2:

    st.markdown("""
<div class="about-card">
<div class="card-title">🛠️ Technologies Used</div>
<div class="card-text">
<ul>
<li><strong>Frontend / Framework:</strong> Streamlit</li>
<li><strong>Data Processing:</strong> Pandas, NumPy</li>
<li><strong>Data Visualization:</strong> Plotly</li>
<li><strong>Computer Vision:</strong> OpenCV</li>
<li><strong>OCR:</strong> Tesseract OCR</li>
<li><strong>AI:</strong> Gemini Vision API</li>
<li><strong>AI Chatbot:</strong> Chatbase Widget</li>
</ul>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="about-card">
<div class="card-title">🚀 Future Scope</div>
<div class="card-text">
<ul>
<li><strong>IoT Integration:</strong> Smart refrigerator cameras and weight sensors.</li>
<li><strong>Receipt Scanner:</strong> Automatically detect groceries from receipts.</li>
<li><strong>Community Sharing:</strong> Connect users with local food donation networks.</li>
<li><strong>Smarter Predictions:</strong> Predict consumption patterns and recommend grocery quantities.</li>
<li><strong>Environmental Impact:</strong> Track estimated CO₂ and water savings from reduced food waste.</li>
</ul>
</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# CHATBOT
# =========================================================

def render_floating_bot():

    bot_code = """
<script>
(function() {

    if (window.parent.document.getElementById("ecopantry-chat-widget")) {
        return;
    }

    const container = window.parent.document.createElement("div");
    container.id = "ecopantry-chat-widget";

    container.style.cssText =
        "position:fixed;" +
        "bottom:25px;" +
        "right:25px;" +
        "z-index:999999;" +
        "display:flex;" +
        "flex-direction:column;" +
        "align-items:flex-end;" +
        "gap:12px;" +
        "font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;";

    const modal = window.parent.document.createElement("div");
    modal.id = "ecopantry-chat-modal";

    modal.style.cssText =
        "display:none;" +
        "width:380px;" +
        "height:580px;" +
        "background:#1A1F1C;" +
        "border:1px solid rgba(0,255,135,0.4);" +
        "border-radius:20px;" +
        "box-shadow:0 12px 40px rgba(0,0,0,0.7),0 0 20px rgba(0,255,135,0.2);" +
        "overflow:hidden;";

    modal.innerHTML =
        '<iframe src="https://www.chatbase.co/chatbot-iframe/voXMr1BILlDLuXX4wRTSy" ' +
        'width="100%" height="100%" frameborder="0" allow="microphone"></iframe>';

    const botBar = window.parent.document.createElement("div");

    botBar.style.cssText =
        "display:flex;" +
        "align-items:center;" +
        "gap:12px;";

    const tooltip = window.parent.document.createElement("div");

    tooltip.innerHTML = "Hi! I'm your EcoPantry assistant 👋";

    tooltip.style.cssText =
        "background:rgba(26,31,28,0.95);" +
        "color:#E0E0E0;" +
        "border:1px solid rgba(0,255,135,0.3);" +
        "padding:10px 18px;" +
        "border-radius:20px;" +
        "font-size:0.88rem;" +
        "font-weight:600;" +
        "box-shadow:0 8px 24px rgba(0,0,0,0.4);" +
        "white-space:nowrap;";

    const btn = window.parent.document.createElement("button");

    btn.innerHTML =
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" ' +
        'stroke="#00FF87" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
        '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>' +
        '<path d="M12 8l1 2 2 1-2 1-1 2-1-2-2-1 2-1z"></path>' +
        '</svg>';

    btn.style.cssText =
        "background:#121614;" +
        "border:1px solid rgba(0,255,135,0.4);" +
        "width:56px;" +
        "height:56px;" +
        "border-radius:50%;" +
        "display:flex;" +
        "align-items:center;" +
        "justify-content:center;" +
        "cursor:pointer;" +
        "box-shadow:0 8px 20px rgba(0,0,0,0.5),0 0 10px rgba(0,255,135,0.2);";

    btn.onmouseover = function() {
        btn.style.transform = "scale(1.12)";
        btn.style.borderColor = "#00FF87";
    };

    btn.onmouseout = function() {
        btn.style.transform = "scale(1)";
        btn.style.borderColor = "rgba(0,255,135,0.4)";
    };

    let isOpen = false;

    btn.onclick = function() {

        isOpen = !isOpen;

        if (isOpen) {
            modal.style.display = "block";
            tooltip.style.display = "none";
        } else {
            modal.style.display = "none";
            tooltip.style.display = "block";
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

    components.html(
        bot_code,
        height=0,
        width=0
    )


render_floating_bot()

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown("""
<div class="footer">
<strong style="color:#00FF87;">EcoPantry</strong>
— Reducing Food Waste Since 2026
<br>
<span style="opacity:0.8;">Made with Python • Streamlit • Pandas • AI</span>
</div>
""", unsafe_allow_html=True)
