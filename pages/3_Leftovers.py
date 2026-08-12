import os
from datetime import date, datetime, timedelta
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from style import apply_custom_sidebar_style

# --- Initial Setup ---
apply_custom_sidebar_style()

st.set_page_config(
    page_title="Leftovers - EcoPantry",
    page_icon="🍽️",
    layout="wide"
)

# --- Recommended Shelf-Life Rules (Days) ---
SHELF_LIFE_MAP = {
    "🍚 Rice & Grains": 2,
    "🥘 Cooked Curries / Dal": 3,
    "🍞 Bread & Bakery": 2,
    "🥦 Cooked Veggies": 3,
    "🍗 Cooked Meat / Fish": 3,
    "🥛 Dairy / Cream Items": 2,
    "🍰 Desserts": 3,
    "🍿 Snacks": 4,
    "🍲 Soup / Stew": 3,
    "📦 Others": 2
}

FILE_PATH = "data/leftovers.csv"

# --- EcoPantry Glassmorphism Theme (CSS) ---
st.markdown("""
    <style>
    /* Global Page Styling */
    .stApp {
        background: #0B0F0D;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        max-width: 1150px;
    }

    /* Hero Typography */
    .hero-container {
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        padding-bottom: 1.25rem;
        margin-bottom: 1.75rem;
    }
    
    .page-title {
        background: linear-gradient(135deg, #A8E6CF 0%, #00FF87 50%, #388E3C 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.75rem;
        letter-spacing: -0.8px;
        margin: 0;
    }
    
    .page-subtitle {
        color: #8E9B90;
        font-size: 1.05rem;
        margin-top: 0.4rem;
    }

    /* Glassmorphism Metric Cards */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.25rem;
        margin-bottom: 2rem;
    }

    .metric-card {
        background: linear-gradient(145deg, rgba(26, 35, 30, 0.7), rgba(15, 20, 17, 0.8));
        border: 1px solid rgba(0, 255, 135, 0.15);
        border-radius: 18px;
        padding: 1.25rem 1.5rem;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .metric-card:hover {
        border-color: rgba(0, 255, 135, 0.4);
        transform: translateY(-3px);
        box-shadow: 0 12px 30px rgba(0, 255, 135, 0.15);
    }

    .metric-label {
        color: #8E9B90;
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    .metric-value {
        color: #FFFFFF;
        font-size: 2.1rem;
        font-weight: 800;
        margin-top: 0.3rem;
    }

    /* Recommendation Banner */
    .ai-banner {
        background: linear-gradient(90deg, rgba(0, 255, 135, 0.08) 0%, rgba(56, 142, 60, 0.05) 100%);
        border-left: 4px solid #00FF87;
        border-radius: 8px 14px 14px 8px;
        padding: 1rem 1.25rem;
        color: #C8E6C9;
        font-size: 0.95rem;
        margin-top: 0.8rem;
        margin-bottom: 1.5rem;
    }

    /* Forms & Containers */
    div[data-testid="stForm"] {
        background: rgba(18, 24, 21, 0.75);
        border: 1px solid rgba(0, 255, 135, 0.2);
        border-radius: 20px;
        padding: 2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.4);
    }

    /* Form Buttons */
    div[data-testid="stForm"] button[kind="primary"] {
        background: linear-gradient(135deg, #00C853 0%, #1B5E20 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(0, 255, 135, 0.4) !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stForm"] button[kind="primary"]:hover {
        background: linear-gradient(135deg, #00FF87 0%, #2E7D32 100%) !important;
        color: #000000 !important;
        box-shadow: 0 0 25px rgba(0, 255, 135, 0.5) !important;
        transform: translateY(-2px);
    }

    /* Status Badges */
    .badge-safe {
        background: rgba(76, 175, 80, 0.2);
        color: #81C784;
        padding: 4px 10px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.85rem;
    }

    .badge-warn {
        background: rgba(255, 152, 0, 0.2);
        color: #FFB74D;
        padding: 4px 10px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.85rem;
    }

    .badge-danger {
        background: rgba(244, 67, 54, 0.2);
        color: #E57373;
        padding: 4px 10px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Helper Data Functions ---
def load_data():
    if os.path.exists(FILE_PATH):
        try:
            return pd.read_csv(FILE_PATH)
        except Exception:
            pass
    return pd.DataFrame(columns=[
        "Food Item", "Category", "Quantity", "Date Stored", "Eat By Date", "Max Days", "Notes"
    ])

def save_data(df):
    os.makedirs("data", exist_ok=True)
    df.to_csv(FILE_PATH, index=False)

df_existing = load_data()

# --- Header Section ---
st.markdown("""
    <div class="hero-container">
        <h1 class="page-title">🍽️ Leftover Manager</h1>
        <p class="page-subtitle">Track cooked meal portions, prevent food spoilage, and auto-calculate safe consumption windows.</p>
    </div>
""", unsafe_allow_html=True)

# --- Dynamic Metrics Calculation ---
today_date = date.today()
total_leftovers = len(df_existing)
eat_soon_count = 0
expired_count = 0

if not df_existing.empty:
    for _, row in df_existing.iterrows():
        try:
            eat_by = datetime.strptime(str(row["Eat By Date"]), "%Y-%m-%d").date()
            diff = (eat_by - today_date).days
            if diff < 0:
                expired_count += 1
            elif diff <= 1:
                eat_soon_count += 1
        except Exception:
            pass

# --- Display Metric Cards ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Active Stored Portions</div>
            <div class="metric-value">🍱 {total_leftovers}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Consume Within 24 Hours</div>
            <div class="metric-value" style="color: #FFD54F;">⚠️ {eat_soon_count}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Expired / Need Discard</div>
            <div class="metric-value" style="color: #E57373;">🔴 {expired_count}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# --- Form Header & Category Selector ---
st.markdown("### ➕ Log New Leftover Portion")

category = st.selectbox(
    "Select Food Category for AI Shelf-Life Auto-Detection",
    list(SHELF_LIFE_MAP.keys())
)

auto_days = SHELF_LIFE_MAP.get(category, 2)

st.markdown(f"""
    <div class="ai-banner">
        💡 <b>Smart Safety Recommendation:</b> Items classified under <b>{category.split(' ', 1)[-1]}</b> stay fresh for approximately <b>{auto_days} days</b> when stored below 4°C in airtight containers.
    </div>
""", unsafe_allow_html=True)

# --- Entry Form ---
with st.form("leftover_form", clear_on_submit=True):

    r1_col1, r1_col2 = st.columns(2)

    with r1_col1:
        food = st.text_input(
            "Food Item Name",
            placeholder="e.g. Creamy Paneer Butter Masala"
        )

    with r1_col2:
        q_col1, q_col2 = st.columns([2, 1])
        with q_col1:
            amount = st.number_input(
                "Amount",
                min_value=0.0,
                value=250.0,
                step=50.0
            )
        with q_col2:
            unit = st.selectbox(
                "Unit",
                ["g", "kg", "ml", "L", "pcs", "pack", "bowls"]
            )
        quantity = f"{amount:g} {unit}"

    r2_col1, r2_col2 = st.columns(2)

    with r2_col1:
        stored_date = st.date_input(
            "Date Stored",
            value=date.today()
        )

    with r2_col2:
        use_within = st.number_input(
            "Safe Window (Days)",
            min_value=1,
            max_value=14,
            value=auto_days,
            help="Auto-filled according to health standard rules. Editable if needed."
        )

    notes = st.text_area(
        "Storage & Reheating Notes",
        placeholder="e.g. Stored in glass container. Heat thoroughly to 75°C before consuming..."
    )

    save = st.form_submit_button(
        "💾 Log Leftover Portion",
        type="primary",
        use_container_width=True
    )

# --- Form Submission Handler ---
if save:
    if not food.strip():
        st.error("⚠️ Please enter a valid food item name.")
    else:
        exp_date = stored_date + timedelta(days=use_within)

        new_item = {
            "Food Item": food.strip(),
            "Category": category,
            "Quantity": quantity,
            "Date Stored": stored_date.strftime("%Y-%m-%d"),
            "Eat By Date": exp_date.strftime("%Y-%m-%d"),
            "Max Days": use_within,
            "Notes": notes.strip() if notes else "N/A"
        }

        updated_df = pd.concat([df_existing, pd.DataFrame([new_item])], ignore_index=True)
        save_data(updated_df)

        st.toast(f"🎉 **{food}** logged successfully! Consume before {exp_date.strftime('%b %d, %Y')}.", icon="✅")
        st.rerun()

st.divider()

# --- Interactive Ledger Section ---
st.markdown("### 📋 Stored Leftovers Ledger")

if not df_existing.empty:
    
    # Filter and Search Bar
    f_col1, f_col2, f_col3 = st.columns([2, 1, 1])
    
    with f_col1:
        search_query = st.text_input("🔍 Search Inventory", placeholder="Filter by item name...").strip().lower()
    with f_col2:
        category_filter = st.selectbox("Filter Category", ["All Categories"] + list(SHELF_LIFE_MAP.keys()))
    with f_col3:
        # Download CSV Export
        csv_data = df_existing.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Ledger CSV",
            data=csv_data,
            file_name=f"leftovers_export_{date.today()}.csv",
            mime="text/csv",
            use_container_width=True
        )

    # Status Computation
    df_display = df_existing.copy()
    statuses = []
    days_remaining_list = []

    for _, row in df_display.iterrows():
        try:
            eat_by = datetime.strptime(str(row["Eat By Date"]), "%Y-%m-%d").date()
            diff = (eat_by - today_date).days
            days_remaining_list.append(max(0, diff))

            if diff < 0:
                statuses.append("🔴 Discard (Expired)")
            elif diff <= 1:
                statuses.append("🟡 Eat Soon!")
            else:
                statuses.append("🟢 Safe to Eat")
        except Exception:
            statuses.append("⚪ Unknown")
            days_remaining_list.append(0)

    df_display["Status"] = statuses
    df_display["Days Remaining"] = days_remaining_list

    # Apply Search & Filter
    if search_query:
        df_display = df_display[df_display["Food Item"].str.lower().str.contains(search_query)]
    if category_filter != "All Categories":
        df_display = df_display[df_display["Category"] == category_filter]

    # Data Table View
    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Food Item": st.column_config.TextColumn("Food Item", help="Name of stored leftover"),
            "Category": st.column_config.TextColumn("Category"),
            "Quantity": st.column_config.TextColumn("Portion Size"),
            "Date Stored": st.column_config.DateColumn("Stored On"),
            "Eat By Date": st.column_config.DateColumn("Consume Before"),
            "Days Remaining": st.column_config.ProgressColumn(
                "Freshness Window",
                min_value=0,
                max_value=7,
                format="%d Days"
            ),
            "Status": st.column_config.TextColumn("Freshness Status"),
            "Notes": st.column_config.TextColumn("Storage Notes")
        }
    )

    # Item Removal Feature
    with st.expander("🗑️ Manage / Remove Specific Portions"):
        item_to_remove = st.selectbox("Select consumed or discarded item to remove:", df_existing["Food Item"].unique())
        if st.button("Remove Selected Item", type="secondary"):
            df_updated = df_existing[df_existing["Food Item"] != item_to_remove]
            save_data(df_updated)
            st.success(f"Removed **{item_to_remove}** from ledger.")
            st.rerun()

else:
    st.info("💡 No active leftovers recorded yet. Use the form above to log cooked portions!")

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

# --- Reset Data Section ---
st.divider()

with st.expander("⚙️ System Control & Reset"):
    st.warning("⚠️ Warning: Clearing ledger data will remove all logged leftover entries permanently.")
    if st.button("🗑️ Clear All Leftovers Ledger Data", key="btn_reset_data", type="primary"):
        empty_df = pd.DataFrame(columns=[
            "Food Item", "Category", "Quantity", "Date Stored", "Eat By Date", "Max Days", "Notes"
        ])
        save_data(empty_df)
        st.success("✅ Ledger reset successfully!")
        st.rerun()

# --- Footer ---
st.markdown("""
    <div style="
        text-align: center;
        width: 100%;
        padding: 2rem 0 1rem 0;
        color: #6C7A70;
        font-size: 0.88rem;
        line-height: 1.6;
    ">
        <strong style="color: #00FF87;">EcoPantry</strong> — Smart Zero-Waste Food Management System<br>
        <span style="opacity: 0.8;">Built with Python • Streamlit • Pandas • Glassmorphism UI</span>
    </div>
""", unsafe_allow_html=True)