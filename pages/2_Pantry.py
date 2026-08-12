import os
import sys
from datetime import date, datetime, timedelta

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# Ensure root folder is accessible for module imports
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# Correct imports
from style import apply_custom_sidebar_style
from utils import check_and_send_notifications

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Pantry Inventory - EcoPantry",
    page_icon="📦",
    layout="wide"
)

# Apply sidebar styling
apply_custom_sidebar_style()

# ---------------------------------------------------------
# Custom Styling (CSS)
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Global Page Background & Padding */
    .stApp {
        background-color: #0B0F0D;
        background-image: 
            radial-gradient(at 0% 0%, rgba(0, 255, 135, 0.05) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(14, 30, 22, 0.5) 0px, transparent 50%);
    }

    .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        max-width: 1100px;
    }

    /* Modern Hero Banner Header */
    .hero-container {
        background: linear-gradient(135deg, rgba(20, 32, 26, 0.8) 0%, rgba(12, 20, 16, 0.9) 100%);
        border: 1px solid rgba(0, 255, 135, 0.2);
        border-radius: 24px;
        padding: 2.2rem 2.5rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(16px);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.05);
        position: relative;
        overflow: hidden;
    }

    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(0, 255, 135, 0.08) 0%, transparent 60%);
        pointer-events: none;
    }

    .page-title {
        background: linear-gradient(135deg, #FFFFFF 0%, #00FF87 60%, #60EFFF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
        letter-spacing: -1px;
        margin-bottom: 0.4rem;
    }

    .page-subtitle {
        color: #94A3B8;
        font-size: 1.05rem;
        font-weight: 400;
        margin: 0;
    }

    /* Metric Cards */
    .metric-card {
        background: rgba(18, 26, 22, 0.7);
        border: 1px solid rgba(0, 255, 135, 0.15);
        border-radius: 20px;
        padding: 1.4rem 1.6rem;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .metric-card:hover {
        border-color: rgba(0, 255, 135, 0.4);
        transform: translateY(-4px);
        box-shadow: 0 14px 35px rgba(0, 255, 135, 0.12);
    }

    .metric-label {
        color: #8E9B90;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .metric-value {
        color: #00FF87;
        font-size: 2rem;
        font-weight: 800;
        margin-top: 0.4rem;
        text-shadow: 0 0 12px rgba(0, 255, 135, 0.3);
    }

    /* Form Design */
    div[data-testid="stForm"] {
        background: rgba(16, 23, 19, 0.75) !important;
        border: 1px solid rgba(0, 255, 135, 0.2) !important;
        border-radius: 24px !important;
        padding: 2.2rem !important;
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4) !important;
        backdrop-filter: blur(16px) !important;
    }

    .form-header-text {
        color: #00FF87;
        font-size: 1.35rem;
        font-weight: 700;
        letter-spacing: -0.3px;
        margin-bottom: 0.2rem;
    }

    /* Tip Cards */
    .tip-card {
        background: rgba(18, 26, 22, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.25rem 1.4rem;
        height: 100%;
        transition: border-color 0.3s ease;
    }
    
    .tip-card:hover {
        border-color: rgba(0, 255, 135, 0.3);
    }

    /* Global Input Overrides */
    .stTextInput input, .stSelectbox > div > div, .stNumberInput input, .stDateInput input {
        background-color: #0E1411 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #F1F5F9 !important;
        transition: all 0.2s ease !important;
    }

    .stTextInput input:focus, .stSelectbox > div > div:focus, .stNumberInput input:focus, .stDateInput input:focus {
        border-color: #00FF87 !important;
        box-shadow: 0 0 0 3px rgba(0, 255, 135, 0.15) !important;
    }

    /* Primary Submit Button Styling */
    div[data-testid="stForm"] button[kind="primary"] {
        background: linear-gradient(135deg, #00FF87 0%, #00B862 100%) !important;
        color: #051A10 !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 20px rgba(0, 255, 135, 0.3) !important;
    }

    div[data-testid="stForm"] button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 255, 135, 0.5) !important;
    }

    /* Expander Styling */
    .streamlit-expanderHeader {
        background: rgba(18, 26, 22, 0.5) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        color: #E2E8F0 !important;
        font-weight: 600 !important;
    }

    /* Clean Dividers */
    hr {
        border-color: rgba(255, 255, 255, 0.08) !important;
        margin: 2.5rem 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Data Handling
# ---------------------------------------------------------
file_path = "data/pantry.csv"
if os.path.exists(file_path):
    existing_df = pd.read_csv(file_path)
else:
    existing_df = pd.DataFrame(columns=["Product", "Category", "Purchase Date", "Expiry Date", "Quantity"])

# ---------------------------------------------------------
# Header Section
# ---------------------------------------------------------
st.markdown("""
    <div class="hero-container">
        <h1 class="page-title">📦 Pantry Inventory</h1>
        <p class="page-subtitle">Track, manage, and prevent food waste with your smart glowing pantry ledger.</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Quick Metrics
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

total_items = len(existing_df)
categories_count = existing_df["Category"].nunique() if not existing_df.empty else 0
today_str = date.today().strftime("%b %d, %Y")

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Stocked Items</div>
            <div class="metric-value">{total_items}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Active Categories</div>
            <div class="metric-value">{categories_count}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Today's Date</div>
            <div class="metric-value">{today_str}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------------
# Form Section
# ---------------------------------------------------------
with st.form("add_item_form", clear_on_submit=True):
    st.markdown('<div class="form-header-text">✨ Log New Inventory Item</div>', unsafe_allow_html=True)
    st.caption("Fill in the details below to log fresh produce or packaged items into your database.")
    st.write("")
    
    r1_col1, r1_col2 = st.columns(2)
    with r1_col1:
        product = st.text_input("Product Name", placeholder="e.g. Organic Oat Milk")
    with r1_col2:
        category = st.selectbox(
            "Category",
            [
                "🥛 Dairy",
                "🥦 Vegetables",
                "🍎 Fruits",
                "🍞 Bakery",
                "🥨 Snacks",
                "🧃 Beverages",
                "🧊 Frozen",
                "📦 Others"
            ]
        )

    r2_col1, r2_col2, r2_col3 = st.columns(3)
    with r2_col1:
        quantity = st.number_input("Quantity", min_value=1, value=1, step=1)
    with r2_col2:
        purchase = st.date_input("Purchase Date", value=date.today())
    with r2_col3:
        expiry = st.date_input("Expiry Date", value=date.today() + timedelta(days=7))

    st.write("")
    submitted = st.form_submit_button("➕ Save Item to Inventory", use_container_width=True)

# ---------------------------------------------------------
# Form Submission Processing
# ---------------------------------------------------------
if submitted:
    if not product.strip():
        st.error("⚠️ Please enter a valid product name.")
    elif expiry < purchase:
        st.warning("⚠️ Expiry date cannot be earlier than purchase date.")
    else:
        new_item = {
            "Product": product.strip(),
            "Category": category,
            "Purchase Date": purchase.strftime("%Y-%m-%d"),
            "Expiry Date": expiry.strftime("%Y-%m-%d"),
            "Quantity": quantity
        }

        os.makedirs("data", exist_ok=True)
        df_concat = pd.concat([existing_df, pd.DataFrame([new_item])], ignore_index=True)
        df_concat.to_csv(file_path, index=False)

        st.toast(f"🎉 **{product}** added to inventory!", icon="✅")
        st.rerun()

st.divider()

# ---------------------------------------------------------
# Inventory List Section
# ---------------------------------------------------------
st.markdown("### 📋 Current Pantry Stock")

if not existing_df.empty:
    display_df = existing_df.copy()
    
    # Calculate Freshness / Status logic
    today = date.today()
    display_df['Days Left'] = pd.to_datetime(display_df['Expiry Date']).dt.date.apply(lambda d: (d - today).days)
    
    def calculate_status(days):
        if days < 0:
            return "🔴 Expired"
        elif days <= 3:
            return "🟡 Expiring Soon"
        return "🟢 Fresh"

    display_df['Status'] = display_df['Days Left'].apply(calculate_status)

    # Interactive Dataframe Configuration
    st.dataframe(
        display_df,
        column_config={
            "Product": st.column_config.TextColumn("Product Name"),
            "Category": st.column_config.TextColumn("Category"),
            "Quantity": st.column_config.NumberColumn("Qty", format="%d"),
            "Purchase Date": st.column_config.DateColumn("Purchased"),
            "Expiry Date": st.column_config.DateColumn("Expires On"),
            "Days Left": st.column_config.ProgressColumn(
                "Shelf Life Remaining (Days)",
                help="Days remaining until expiration",
                format="%d days",
                min_value=0,
                max_value=30,
            ),
            "Status": st.column_config.TextColumn("Freshness Status")
        },
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("💡 Your pantry inventory is currently empty. Use the form above to log groceries!")

st.divider()

# ---------------------------------------------------------
# Notifications Section
# ---------------------------------------------------------
leftovers_data = []
leftover_file = "data/leftovers.csv"

if os.path.exists(leftover_file):
    leftovers_df = pd.read_csv(leftover_file)
    for _, row in leftovers_df.iterrows():
        try:
            stored = datetime.strptime(str(row["Date Stored"]), "%Y-%m-%d").date()
            days_stored = (date.today() - stored).days
            leftovers_data.append({
                "name": row["Food Item"],
                "days_stored": days_stored
            })
        except Exception:
            pass

st.markdown("### 🔔 Notifications & Alerts")

pantry_items = []
if not existing_df.empty:
    for _, row in existing_df.iterrows():
        pantry_items.append({
            "name": row["Product"],
            "expiry_date": str(row["Expiry Date"])
        })

leftovers = leftovers_data

notif_col1, notif_col2 = st.columns([3, 1], vertical_alignment="bottom")

with notif_col1:
    user_email = st.text_input("Recipient Email", placeholder="your.email@example.com")

with notif_col2:
    send_notif = st.button("📧 Send Reminders", use_container_width=True)

if send_notif:
    if not user_email:
        st.warning("⚠️ Please enter a recipient email address first.")
    else:
        success, message = check_and_send_notifications(
    pantry_items=pantry_items,
    user_email=user_email
)
        

        if success:
            st.success(message)
        else:
            st.error(message)

st.divider()

# ---------------------------------------------------------
# Preservation & Storage Tips Section
# ---------------------------------------------------------
st.markdown("### 💡 Preservation & Storage Tips")

with st.expander("📌 Learn how to make different categories last longer", expanded=False):
    t1, t2, t3 = st.columns(3)
    
    with t1:
        st.markdown("""
        <div class="tip-card">
            <h4 style="color: #00FF87; margin-top:0; font-size: 1.05rem;">🥛 Dairy & Milk</h4>
            <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin:0;">
            Keep stored in the main body of the fridge rather than door shelves, as temperatures fluctuate near the door.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with t2:
        st.markdown("""
        <div class="tip-card">
            <h4 style="color: #00FF87; margin-top:0; font-size: 1.05rem;">🥦 Produce & Veggies</h4>
            <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin:0;">
            Wrap leafy greens in paper towels inside sealed containers to absorb unwanted moisture and extend freshness.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with t3:
        st.markdown("""
        <div class="tip-card">
            <h4 style="color: #00FF87; margin-top:0; font-size: 1.05rem;">🍞 Bakery & Bread</h4>
            <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin:0;">
            Freeze extra slices if you won't consume the loaf within 3 to 4 days to prevent premature molding.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Floating Chatbot Injection
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# Reset Data Section (Danger Zone)
# ---------------------------------------------------------
st.divider()
st.markdown("### ⚙️ System Reset")

with st.expander("🗑️ Reset Pantry Data", expanded=False):
    st.warning("⚠️ **Warning**: This action will clear all saved pantry items. It cannot be undone!")
    if st.button("Clear All Inventory Data", key="btn_reset_data_add_page", type="secondary"):
        os.makedirs("data", exist_ok=True)
        
        p_path = "data/pantry.csv"
        
        empty_pantry = pd.DataFrame(columns=["Product", "Category", "Purchase Date", "Expiry Date", "Quantity"])
        empty_pantry.to_csv(p_path, index=False)
        
        st.success("All inventory data has been reset successfully!")
        st.rerun()

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.divider()
st.markdown("""
    <div style="
        text-align: center;
        width: 100%;
        padding: 1rem 0 2rem 0;
        color: #64748B;
        font-size: 0.85rem;
        line-height: 1.6;
    ">
        <strong style="color: #00FF87;">EcoPantry</strong> — Reducing Food Waste<br>
        <span style="opacity: 0.8;">Made with Python • Streamlit • Pandas • AI</span>
    </div>
""", unsafe_allow_html=True)