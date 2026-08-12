import os
from datetime import date, datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components
from style import apply_custom_sidebar_style

# --- Initial Page Config ---
st.set_page_config(
    page_title="Analytics - EcoPantry", 
    page_icon="📊", 
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_sidebar_style()

# --- Ultra-Modern Competition Styling (CSS) ---
st.markdown("""
    <style>
    /* Dark Theme Core */
    .stApp {
        background-color: #080C0A;
        background-image: radial-gradient(circle at 50% -20%, rgba(0, 255, 135, 0.12), transparent 75%);
    }

    /* Animated Neon Page Header */
    .hero-container {
        padding: 1rem 0 1.5rem 0;
        border-bottom: 1px solid rgba(0, 255, 135, 0.15);
        margin-bottom: 1.5rem;
    }
    
    .page-title {
        background: linear-gradient(135deg, #FFFFFF 0%, #A8E6CF 40%, #00FF87 80%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.8rem;
        letter-spacing: -0.8px;
        margin-bottom: 0.2rem;
        filter: drop-shadow(0 0 12px rgba(0, 255, 135, 0.2));
    }

    .page-subtitle {
        color: #8E9B90;
        font-size: 1.05rem;
        font-weight: 400;
    }

    /* Metric Cards Grid */
    .stat-card {
        background: rgba(18, 25, 21, 0.75);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(0, 255, 135, 0.2);
        border-radius: 20px;
        padding: 1.3rem 1.5rem;
        position: relative;
        overflow: hidden;
        transition: all 0.35s ease;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }

    .stat-card:hover {
        transform: translateY(-4px);
        border-color: rgba(0, 255, 135, 0.45);
        box-shadow: 0 15px 35px rgba(0, 255, 135, 0.15);
    }

    .stat-card::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, transparent, #00FF87, transparent);
        opacity: 0.8;
    }

    .stat-val {
        color: #00FF87;
        font-size: 2.2rem;
        font-weight: 900;
        letter-spacing: -0.5px;
        line-height: 1.1;
        text-shadow: 0 0 15px rgba(0, 255, 135, 0.3);
    }

    .stat-lbl {
        color: #8E9B90;
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 0.4rem;
    }

    /* Section Headers */
    .section-header {
        color: #00FF87;
        font-size: 1.25rem;
        font-weight: 800;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Empty State Wrapper */
    .empty-state {
        background: rgba(18, 25, 21, 0.6);
        border: 1px dashed rgba(0, 255, 135, 0.25);
        border-radius: 24px;
        padding: 4rem 2rem;
        text-align: center;
        backdrop-filter: blur(10px);
    }

    /* At-Risk Items Card */
    .risk-card {
        background: rgba(22, 30, 26, 0.8);
        border: 1px solid rgba(255, 82, 82, 0.3);
        border-radius: 16px;
        padding: 1.2rem;
        margin-top: 1rem;
    }

    .risk-title {
        color: #FF5252;
        font-weight: 800;
        font-size: 1rem;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
    <div class="hero-container">
        <h1 class="page-title">📊 Pantry Analytics & Impact Radar</h1>
        <p class="page-subtitle">Interactive intelligence on food preservation, financial savings, carbon offsets, and expiry forecasts.</p>
    </div>
""", unsafe_allow_html=True)

# --- Data Loading & Preprocessing ---
pantry_path = "data/pantry.csv"

if os.path.exists(pantry_path):
    pantry_df = pd.read_csv(pantry_path)
else:
    pantry_df = pd.DataFrame(columns=["Item Name", "Category", "Quantity", "Expiry Date", "Added Date"])

# --- Content Render ---
if pantry_df.empty:
    st.markdown("""
        <div class="empty-state">
            <div style="font-size: 4.5rem; margin-bottom: 1rem; filter: drop-shadow(0 0 15px rgba(0,255,135,0.3));">🌱</div>
            <h2 style="color: #E0E0E0; font-weight: 800; margin-bottom: 0.5rem;">Your EcoPantry Analytics are Offline</h2>
            <p style="color: #8E9B90; max-width: 460px; margin: 0 auto 1.5rem auto; line-height: 1.5;">
                Add items to your pantry inventory to generate real-time carbon offset estimates, category distributions, and freshness health gauges.
            </p>
        </div>
    """, unsafe_allow_html=True)
else:
    # Pre-calculate Expiry Statuses
    today = date.today()
    expiring_soon_items = []
    expired_count = 0
    expiring_soon_count = 0
    fresh_count = 0

    for idx, row in pantry_df.iterrows():
        try:
            exp_date = datetime.strptime(str(row["Expiry Date"]), "%Y-%m-%d").date()
            days_left = (exp_date - today).days
            if days_left < 0:
                expired_count += 1
            elif days_left <= 3:
                expiring_soon_count += 1
                expiring_soon_items.append({"Item": row["Item Name"], "Days": days_left, "Category": row["Category"]})
            else:
                fresh_count += 1
        except Exception:
            fresh_count += 1

    total_items = len(pantry_df)
    saved_food = total_items * 0.85                  # kg of food saved
    saved_money = saved_food * 260                   # Estimate ₹260/kg
    saved_co2 = saved_food * 1.9                     # 1.9 kg CO2e per kg food saved
    trees_equivalent = round(saved_co2 / 20, 1)      # ~20kg CO2 per tree per year
    pantry_health = int(((fresh_count + (expiring_soon_count * 0.5)) / total_items) * 100)

    # --- Interactive Filter Control Bar ---
    st.markdown('<div class="section-header">🎛️ Analytics Filter Controls</div>', unsafe_allow_html=True)
    f_col1, f_col2 = st.columns([1, 2])
    
    with f_col1:
        categories = ["All Categories"] + list(pantry_df["Category"].dropna().unique())
        selected_cat = st.selectbox("Filter Inventory Category:", categories)
        
    with f_col2:
        st.write("") # Spacer

    # Apply Filter to dataframe for visualizations
    filtered_df = pantry_df.copy()
    if selected_cat != "All Categories":
        filtered_df = filtered_df[filtered_df["Category"] == selected_cat]

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Key Impact Metrics Bar ---
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-lbl">💰 Money Saved</div>
                <div class="stat-val">₹{saved_money:,.0f}</div>
                <div style="color: #6C7A70; font-size: 0.8rem; margin-top: 0.4rem;">Prevented waste value</div>
            </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-lbl">🍏 Food Saved</div>
                <div class="stat-val">{saved_food:,.1f} <span style="font-size: 1.1rem;">kg</span></div>
                <div style="color: #6C7A70; font-size: 0.8rem; margin-top: 0.4rem;">Diverted from landfills</div>
            </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-lbl">☁️ CO₂ Offset</div>
                <div class="stat-val">{saved_co2:,.1f} <span style="font-size: 1.1rem;">kg</span></div>
                <div style="color: #6C7A70; font-size: 0.8rem; margin-top: 0.4rem;">Reduced emissions</div>
            </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-lbl">🌳 Tree Offset Eq.</div>
                <div class="stat-val">{trees_equivalent} <span style="font-size: 1.1rem;">trees</span></div>
                <div style="color: #6C7A70; font-size: 0.8rem; margin-top: 0.4rem;">Annual absorption rate</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Middle Section: Visualizations ---
    col_chart1, col_chart2 = st.columns(2)

    # 1. Donut Chart: Inventory Distribution
    with col_chart1:
        st.markdown('<div class="section-header">🏷️ Inventory Share by Category</div>', unsafe_allow_html=True)
        cat_counts = filtered_df["Category"].value_counts().reset_index()
        cat_counts.columns = ["Category", "Count"]

        custom_palette = ["#00FF87", "#00E5FF", "#7C4DFF", "#FF4081", "#FFD700", "#69F0AE"]

        fig_pie = px.pie(
            cat_counts, 
            values="Count", 
            names="Category", 
            hole=0.62,
            color_discrete_sequence=custom_palette
        )
        
        fig_pie.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            marker=dict(line=dict(color='#080C0A', width=2)),
            hovertemplate="<b>%{label}</b><br>Items: %{value}<br>Share: %{percent}<extra></extra>"
        )
        
        fig_pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#E0E0E0", family="Sans-Serif"),
            showlegend=False,
            margin=dict(t=20, b=20, l=20, r=20),
            annotations=[dict(
                text=f"<b>{len(filtered_df)}</b><br><span style='font-size:12px;color:#8E9B90;'>Items Tracked</span>",
                x=0.5, y=0.5, font_size=18, showarrow=False, font_color="#00FF87"
            )]
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    # 2. Expiry Forecast Bar Chart
    with col_chart2:
        st.markdown('<div class="section-header">⏳ Expiry Risk Distribution</div>', unsafe_allow_html=True)
        
        categories_list = ["Fresh (>3 Days)", "Expiring Soon (≤3 Days)", "Expired"]
        counts_list = [fresh_count, expiring_soon_count, expired_count]
        colors_list = ["#00FF87", "#FFB74D", "#FF5252"]

        fig_bar = go.Figure(data=[
            go.Bar(
                x=categories_list,
                y=counts_list,
                marker=dict(
                    color=colors_list,
                    cornerradius=12
                ),
                text=counts_list,
                textposition='auto',
                textfont=dict(color='#000000', size=14, family='sans-serif'),
                hovertemplate="<b>%{x}</b>: %{y} items<extra></extra>"
            )
        ])

        fig_bar.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#E0E0E0", family="Sans-Serif"),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)", zeroline=False),
            margin=dict(t=20, b=20, l=20, r=20),
            height=360
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- Bottom Section: Health Gauge & Risk Table ---
    row2_col1, row2_col2 = st.columns([1, 1])

    with row2_col1:
        st.markdown('<div class="section-header">🎯 Overall Pantry Freshness Health</div>', unsafe_allow_html=True)
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = pantry_health,
            number = {'suffix': "%", 'font': {'color': '#00FF87', 'size': 48}},
            title = {'text': "Health Score", 'font': {'size': 16, 'color': '#8E9B90'}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "rgba(255,255,255,0.2)"},
                'bar': {'color': "#00FF87"},
                'bgcolor': "rgba(255,255,255,0.05)",
                'borderwidth': 0,
                'steps': [
                    {'range': [0, 40], 'color': 'rgba(255, 82, 82, 0.3)'},
                    {'range': [40, 75], 'color': 'rgba(255, 183, 77, 0.3)'},
                    {'range': [75, 100], 'color': 'rgba(0, 255, 135, 0.3)'}
                ]
            }
        ))
        
        fig_gauge.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#E0E0E0"),
            height=260,
            margin=dict(t=20, b=10, l=30, r=30)
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

    with row2_col2:
        st.markdown('<div class="section-header">🚨 Priority Expiry Action Radar</div>', unsafe_allow_html=True)
        if expiring_soon_items:
            risk_df = pd.DataFrame(expiring_soon_items)
            st.dataframe(
                risk_df,
                column_config={
                    "Item": st.column_config.TextColumn("Expiring Product", width="medium"),
                    "Days": st.column_config.NumberColumn("Days Remaining", format="%d days"),
                    "Category": st.column_config.TextColumn("Category", width="small")
                },
                use_container_width=True,
                hide_index=True
            )
        else:
            st.markdown("""
                <div class="risk-card" style="border-color: rgba(0,255,135,0.3);">
                    <div class="risk-title" style="color: #00FF87;">✅ No Immediate Expiry Risk</div>
                    <div style="color: #A8E6CF; font-size: 0.9rem;">
                        All inventory items have 4+ days of freshness remaining. No intervention required!
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div style="
        text-align: center;
        width: 100%;
        margin-top: 3rem;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        color: #6C7A70;
        font-size: 0.88rem;
        line-height: 1.6;
    ">
        <strong style="color: #00FF87;">EcoPantry Analytics Core</strong> — Quantifying Zero-Waste Impact<br>
        <span style="opacity: 0.8;">Built with Python • Streamlit • Plotly • Pandas</span>
    </div>
""", unsafe_allow_html=True)

# --- Floating Assistant Widget Injection ---
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
            background: #141916;
            border: 1px solid rgba(0, 255, 135, 0.4);
            border-radius: 24px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0, 255, 135, 0.25);
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.1, 0.9, 0.2, 1);
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
        tooltip.innerHTML = "Ask EcoPantry AI 👋";
        tooltip.style.cssText = `
            background: rgba(20, 25, 22, 0.9);
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
            <svg id="bot-svg-icon" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#00FF87" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: all 0.3s ease;">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                <path d="M12 8l1 2 2 1-2 1-1 2-1-2-2-1 2-1z"></path>
            </svg>
        `;
        btn.style.cssText = `
            background: #101412;
            border: 1px solid rgba(0, 255, 135, 0.4);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 8px 20px rgba(0,0,0,0.5), 0 0 15px rgba(0, 255, 135, 0.2);
            transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        `;

        btn.onmouseover = () => { 
            btn.style.transform = 'scale(1.1)';
            btn.style.borderColor = '#00FF87';
            btn.style.boxShadow = '0 0 30px rgba(0, 255, 135, 0.8), 0 8px 20px rgba(0,0,0,0.6)';
            btn.style.background = '#18201C';
            tooltip.style.borderColor = '#00FF87';
        };

        btn.onmouseout = () => { 
            btn.style.transform = 'scale(1)';
            btn.style.borderColor = 'rgba(0, 255, 135, 0.4)';
            btn.style.boxShadow = '0 8px 20px rgba(0,0,0,0.5), 0 0 15px rgba(0, 255, 135, 0.2)';
            btn.style.background = '#101412';
            tooltip.style.borderColor = 'rgba(0, 255, 135, 0.3)';
        };

        let isOpen = false;
        btn.onclick = () => {
            isOpen = !isOpen;
            modal.style.display = isOpen ? 'block' : 'none';
            tooltip.style.display = isOpen ? 'none' : 'block';
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