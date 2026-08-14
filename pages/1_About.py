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
# CUSTOM STYLING
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 50% -20%, rgba(0, 255, 135, 0.10), transparent 55%),
        #080C0A;
}

/* Main content */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
    max-width: 1050px;
}

/* Hero */
.hero-header {
    margin-bottom: 1.5rem;
}

.hero-title {
    font-size: 2.8rem;
    font-weight: 900;
    letter-spacing: -1px;
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #A8E6CF 40%,
        #00FF87 90%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 15px rgba(0,255,135,0.20));
    margin-bottom: 0.4rem;
}

.hero-subtitle {
    color: #8E9B90;
    font-size: 1.05rem;
    line-height: 1.6;
    margin-bottom: 2rem;
}


/* Divider */
.green-divider {
    height: 1px;
    background: rgba(0, 255, 135, 0.18);
    margin: 2rem 0;
}


/* Statistics cards */
.stat-card {
    background: rgba(18, 25, 21, 0.78);
    border: 1px solid rgba(0, 255, 135, 0.30);
    border-radius: 18px;
    padding: 1.7rem 1.5rem;
    min-height: 120px;
    box-shadow:
        0 10px 30px rgba(0,0,0,0.35),
        inset 0 0 15px rgba(0,255,135,0.025);
    transition: all 0.3s ease;
}

.stat-card:hover {
    border-color: rgba(0,255,135,0.65);
    transform: translateY(-3px);
    box-shadow:
        0 12px 35px rgba(0,0,0,0.45),
        0 0 25px rgba(0,255,135,0.10);
}

.stat-number {
    color: #00FF87;
    font-size: 1.9rem;
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 0.8rem;
    text-shadow: 0 0 12px rgba(0,255,135,0.25);
}

.stat-label {
    color: #8E9B90;
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.7px;
    text-transform: uppercase;
}


/* SDG Banner */
.sdg-card {
    background: rgba(0, 45, 25, 0.38);
    border: 1px solid rgba(0,255,135,0.45);
    border-radius: 20px;
    padding: 1.5rem 1.8rem;
    margin: 2rem 0;
    box-shadow:
        0 0 25px rgba(0,255,135,0.06),
        inset 0 0 20px rgba(0,255,135,0.025);
}

.sdg-icon {
    font-size: 2.6rem;
}

.sdg-title {
    color: #00FF87;
    font-size: 1.15rem;
    font-weight: 850;
    margin-bottom: 0.5rem;
}

.sdg-text {
    color: #B8C6BC;
    font-size: 0.92rem;
    line-height: 1.6;
}


/* Content cards */
.about-card {
    background: rgba(18, 25, 21, 0.80);
    border: 1px solid rgba(0,255,135,0.22);
    border-radius: 20px;
    padding: 1.7rem;
    margin-bottom: 1.5rem;
    min-height: 230px;
    box-shadow:
        0 10px 30px rgba(0,0,0,0.35),
        inset 0 0 15px rgba(0,255,135,0.025);
    transition: all 0.3s ease;
}

.about-card:hover {
    transform: translateY(-3px);
    border-color: rgba(0,255,135,0.45);
    box-shadow:
        0 12px 35px rgba(0,0,0,0.45),
        0 0 25px rgba(0,255,135,0.08);
}

.card-title {
    color: #00FF87;
    font-size: 1.2rem;
    font-weight: 850;
    margin-bottom: 1rem;
    text-shadow: 0 0 8px rgba(0,255,135,0.20);
}

.card-text {
    color: #D0D8D2;
    font-size: 0.94rem;
    line-height: 1.7;
}

.card-text ul {
    margin-top: 0.4rem;
    padding-left: 1.2rem;
}

.card-text li {
    margin-bottom: 0.7rem;
}

.card-text strong {
    color: #E9F5ED;
}


/* Highlight box */
.highlight-box {
    background: rgba(0,255,135,0.055);
    border-left: 3px solid #00FF87;
    padding: 0.9rem 1rem;
    margin-top: 1.2rem;
    border-radius: 0 10px 10px 0;
    color: #BFD0C5;
}


/* Footer */
.footer {
    text-align: center;
    color: #6C7A70;
    font-size: 0.85rem;
    line-height: 1.6;
    margin-top: 2rem;
    padding: 1.5rem 0 2rem 0;
    border-top: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero-header">

    <div class="hero-title">
        🌿 About Us
    </div>

    <div class="hero-subtitle">
        Revolutionizing kitchen inventory management through automation,
        computer vision, and AI-driven sustainability.
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# DIVIDER
# =========================================================

st.markdown('<div class="green-divider"></div>', unsafe_allow_html=True)


# =========================================================
# STATISTICS
# =========================================================

stat1, stat2, stat3 = st.columns(3, gap="large")

with stat1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">1.3 Billion</div>
        <div class="stat-label">Tons of Food Wasted Annually</div>
    </div>
    """, unsafe_allow_html=True)

with stat2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">30%</div>
        <div class="stat-label">Target Household Reduction</div>
    </div>
    """, unsafe_allow_html=True)

with stat3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">100%</div>
        <div class="stat-label">Automated Freshness Tracking</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# SDG SECTION
# =========================================================

st.markdown("""
<div class="sdg-card">

    <div style="display:flex; align-items:center; gap:22px;">

        <div class="sdg-icon">
            🌍
        </div>

        <div>

            <div class="sdg-title">
                United Nations SDG Goal 12: Responsible Consumption
            </div>

            <div class="sdg-text">
                EcoPantry directly aligns with
                <strong>Target 12.3</strong> to halve global per capita
                food waste at retail and consumer levels by equipping
                households with intelligent expiration reminders and
                leftover recipe intelligence.
            </div>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# TWO-COLUMN CONTENT
# =========================================================

col1, col2 = st.columns(2, gap="large")


# =========================================================
# LEFT COLUMN
# =========================================================

with col1:

    st.markdown("""
    <div class="about-card">

        <div class="card-title">
            🚀 Our Mission
        </div>

        <div class="card-text">

            Every year, households lose hundreds of dollars in spoiled
            groceries due to overlooked storage dates and inefficient
            kitchen inventory management.

            <br><br>

            Our mission is to help households make smarter decisions
            about the food they already own while reducing unnecessary
            food waste.

            <div class="highlight-box">
                <strong style="color:#00FF87;">Goal:</strong>
                Reduce household grocery waste through intelligent
                tracking, timely reminders, and sustainable food habits.
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# RIGHT COLUMN
# =========================================================

with col2:

    st.markdown("""
    <div class="about-card">

        <div class="card-title">
            🛠️ Technology Stack
        </div>

        <div class="card-text">

            Built using modern Python-based technologies designed
            for scalability, intelligent automation, and seamless
            user interaction.

            <br><br>

            <ul>
                <li>
                    <strong>Frontend / Framework:</strong>
                    Streamlit
                </li>

                <li>
                    <strong>Data Processing:</strong>
                    Pandas & NumPy
                </li>

                <li>
                    <strong>Data Visualization:</strong>
                    Plotly
                </li>

                <li>
                    <strong>Computer Vision:</strong>
                    OpenCV & EasyOCR
                </li>

                <li>
                    <strong>AI Assistant:</strong>
                    Embedded Chatbase
                </li>

                <li>
                    <strong>Product Database:</strong>
                    OpenFoodFacts
                </li>
            </ul>

        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# CORE FEATURES
# =========================================================

st.markdown("""
<div class="about-card">

    <div class="card-title">
        ⚡ What Makes EcoPantry Smart?
    </div>

    <div class="card-text">

        <ul>

            <li>
                <strong>📷 AI Smart Scanner:</strong>
                Uses computer vision and OCR to identify package
                information and extract expiration dates.
            </li>

            <li>
                <strong>📦 Smart Pantry Tracking:</strong>
                Keeps track of food inventory and freshness status.
            </li>

            <li>
                <strong>🍳 Leftover Intelligence:</strong>
                Suggests recipe ideas based on available leftovers.
            </li>

            <li>
                <strong>📊 Sustainability Analytics:</strong>
                Visualizes pantry activity and helps users understand
                their food-waste habits.
            </li>

            <li>
                <strong>💬 AI Assistant:</strong>
                Provides an interactive guide for pantry and
                food-preservation questions.
            </li>

        </ul>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FUTURE SCOPE
# =========================================================

st.markdown("""
<div class="about-card">

    <div class="card-title">
        🚀 Future Scope
    </div>

    <div class="card-text">

        <ul>

            <li>
                <strong>🏠 Smart Kitchen Integration:</strong>
                Integration with smart refrigerators, cameras,
                and weight sensors.
            </li>

            <li>
                <strong>🧾 Receipt Intelligence:</strong>
                Automated grocery receipt scanning and item intake.
            </li>

            <li>
                <strong>🤝 Community Food Sharing:</strong>
                Local peer-to-peer sharing of excess food.
            </li>

            <li>
                <strong>🌱 Sustainability Expansion:</strong>
                More detailed environmental-impact tracking
                and personalized waste-reduction goals.
            </li>

        </ul>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# DIVIDER
# =========================================================

st.divider()


# =========================================================
# FLOATING CHATBOT
# =========================================================

def render_floating_bot():

    bot_code = """
    <script>

    (function() {

        if (
            window.parent.document.getElementById(
                'ecopantry-chat-widget'
            )
        ) return;


        const container =
            window.parent.document.createElement('div');

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
            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                Roboto,
                sans-serif;
        `;


        const modal =
            window.parent.document.createElement('div');

        modal.id = 'ecopantry-chat-modal';

        modal.style.cssText = `
            display: none;
            width: 380px;
            height: 580px;
            background: #1A1F1C;
            border: 1px solid rgba(0, 255, 135, 0.4);
            border-radius: 20px;
            box-shadow:
                0 12px 40px rgba(0,0,0,0.7),
                0 0 20px rgba(0,255,135,0.2);
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


        const botBar =
            window.parent.document.createElement('div');

        botBar.style.cssText = `
            display: flex;
            align-items: center;
            gap: 12px;
        `;


        const tooltip =
            window.parent.document.createElement('div');

        tooltip.id = 'ecopantry-chat-tooltip';

        tooltip.innerHTML =
            "Hi! I'm your EcoPantry assistant 👋";

        tooltip.style.cssText = `
            background: rgba(26, 31, 28, 0.95);
            color: #E0E0E0;
            border: 1px solid rgba(0, 255, 135, 0.3);
            padding: 10px 18px;
            border-radius: 20px;
            font-size: 0.88rem;
            font-weight: 600;
            box-shadow:
                0 8px 24px rgba(0,0,0,0.4);
            backdrop-filter: blur(8px);
            white-space: nowrap;
            transition: all 0.3s ease;
        `;


        const btn =
            window.parent.document.createElement('button');

        btn.innerHTML = `
            <svg
                id="bot-svg-icon"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#00FF87"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round">

                <path d="
                    M21 15a2 2 0 0 1-2 2H7
                    l-4 4V5a2 2 0 0 1 2-2h14
                    a2 2 0 0 1 2 2z
                "></path>

                <path d="
                    M12 8l1 2 2 1-2 1
                    -1 2-1-2-2-1 2-1z
                "></path>

            </svg>
        `;


        btn.style.cssText = `
            background: #121614;
            border: 1px solid rgba(0,255,135,0.4);
            width: 56px;
            height: 56px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow:
                0 8px 20px rgba(0,0,0,0.5),
                0 0 10px rgba(0,255,135,0.2);
            transition:
                all 0.35s cubic-bezier(
                    0.175,
                    0.885,
                    0.32,
                    1.275
                );
        `;


        btn.onmouseover = () => {

            btn.style.transform = 'scale(1.12)';

            btn.style.borderColor = '#00FF87';

            btn.style.boxShadow =
                '0 0 25px rgba(0,255,135,0.7),' +
                '0 0 50px rgba(0,255,135,0.3),' +
                '0 8px 20px rgba(0,0,0,0.6)';

            btn.style.background = '#1A231D';

            tooltip.style.borderColor = '#00FF87';

            tooltip.style.boxShadow =
                '0 0 15px rgba(0,255,135,0.4)';

            const svgIcon =
                btn.querySelector('#bot-svg-icon');

            if (svgIcon) {
                svgIcon.setAttribute(
                    'stroke',
                    '#81C784'
                );
            }
        };


        btn.onmouseout = () => {

            btn.style.transform = 'scale(1)';

            btn.style.borderColor =
                'rgba(0,255,135,0.4)';

            btn.style.boxShadow =
                '0 8px 20px rgba(0,0,0,0.5),' +
                '0 0 10px rgba(0,255,135,0.2)';

            btn.style.background = '#121614';

            tooltip.style.borderColor =
                'rgba(0,255,135,0.3)';

            tooltip.style.boxShadow =
                '0 8px 24px rgba(0,0,0,0.4)';

            const svgIcon =
                btn.querySelector('#bot-svg-icon');

            if (svgIcon) {
                svgIcon.setAttribute(
                    'stroke',
                    '#00FF87'
                );
            }
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

    components.html(
        bot_code,
        height=0,
        width=0
    )


render_floating_bot()


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    <strong style="color:#00FF87;">
        EcoPantry
    </strong>
    — Reducing Food Waste Since 2026
    <br>

    <span style="opacity:0.8;">
        Made with Python • Streamlit • Pandas • AI
    </span>

</div>
""", unsafe_allow_html=True)
