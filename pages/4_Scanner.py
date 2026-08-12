import os
import re
import html
import requests
import numpy as np
import pandas as pd
from datetime import datetime, date
from PIL import Image
import cv2
import easyocr
from pyzbar.pyzbar import decode
import streamlit as st
import streamlit.components.v1 as components
from style import apply_custom_sidebar_style

# --- Initial Page Config ---
st.set_page_config(
    page_title="Smart Scanner - EcoPantry",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_sidebar_style()

# --- Competition-Grade Cyber-Eco Glass CSS ---
st.markdown("""
    <style>
    /* Dark Cyber-Eco Theme Core */
    .stApp {
        background-color: #080C0A;
        background-image: radial-gradient(circle at 50% -20%, rgba(0, 255, 135, 0.12), transparent 75%);
    }

    /* Page Hero Header */
    .hero-container {
        padding: 1rem 0 1.2rem 0;
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

    /* Modern Glass Card Base */
    .glass-card {
        background: rgba(18, 25, 21, 0.75);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(0, 255, 135, 0.2);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }

    /* Glow Cards for Diagnostic Results */
    .glow-card-green {
        background: rgba(0, 255, 135, 0.06);
        border: 1px solid rgba(0, 255, 135, 0.45);
        border-radius: 16px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 0 25px rgba(0, 255, 135, 0.18);
        transition: all 0.3s ease;
    }

    .glow-card-green:hover {
        box-shadow: 0 0 35px rgba(0, 255, 135, 0.3);
        border-color: rgba(0, 255, 135, 0.75);
    }

    .glow-card-orange {
        background: rgba(255, 183, 77, 0.06);
        border: 1px solid rgba(255, 183, 77, 0.35);
        border-radius: 16px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }

    /* Typography Utilities */
    .metric-label {
        color: #8E9B90;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 0.3rem;
    }

    .metric-value-primary {
        color: #00FF87;
        font-size: 1.5rem;
        font-weight: 900;
        text-shadow: 0 0 12px rgba(0, 255, 135, 0.4);
    }

    .metric-value-warning {
        color: #FFB74D;
        font-size: 1.05rem;
        font-weight: 700;
    }

    /* OCR Console Terminal Display */
    .ocr-box {
        background: rgba(8, 12, 10, 0.9);
        border: 1px solid rgba(0, 255, 135, 0.25);
        border-radius: 14px;
        padding: 1rem;
        color: #A8E6CF;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.88rem;
        max-height: 220px;
        overflow-y: auto;
        white-space: pre-wrap;
    }

    /* Quick Add Form Container */
    .add-form-card {
        background: rgba(20, 28, 24, 0.85);
        border: 1px solid rgba(0, 255, 135, 0.35);
        border-radius: 20px;
        padding: 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5);
    }

    /* File Uploader Custom Tweaks */
    div[data-testid="stFileUploader"] {
        background: rgba(18, 25, 21, 0.6);
        border: 2px dashed rgba(0, 255, 135, 0.35);
        border-radius: 20px;
        padding: 1.2rem;
        transition: all 0.3s ease;
    }
    
    div[data-testid="stFileUploader"]:hover {
        border-color: rgba(0, 255, 135, 0.7);
        box-shadow: 0 0 20px rgba(0, 255, 135, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# --- Hero Header ---
st.markdown("""
    <div class="hero-container">
        <h1 class="page-title">📷 AI Smart Package Scanner</h1>
        <p class="page-subtitle">Computer vision barcode recognition & OCR expiration date extraction with 1-click pantry sync.</p>
    </div>
""", unsafe_allow_html=True)

# --- Cache OCR Engine to Prevent Reload Lag ---
@st.cache_resource
def load_ocr_reader():
    return easyocr.Reader(['en'], gpu=False)

reader = load_ocr_reader()

# --- Smart Helper Functions ---
def parse_date_to_iso(date_str):
    """Converts various date string formats into standard YYYY-MM-DD for Streamlit inputs"""
    if not date_str:
        return date.today()
        
    date_str = date_str.strip()
    formats = [
        "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%m-%d-%Y",
        "%d/%m/%y", "%m/%d/%y", "%d-%m-%y", "%m-%d-%y",
        "%B %d, %Y", "%b %d, %Y", "%d %B %Y", "%d %b %Y"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
            
    # Handle month/year formats like "08/2026"
    m_y_match = re.match(r'^(\d{2})[/-](\d{4})$', date_str)
    if m_y_match:
        m, y = int(m_y_match.group(1)), int(m_y_match.group(2))
        return date(y, m, 28)
        
    return date.today()

def extract_expiry(text):
    """Enhanced regex patterns for package expiration keywords"""
    patterns = [
        r'(?:EXP|BEST BEFORE|USE BY|BEST BY|EXPIRY)?\s*:?\s*(\d{2}[/-]\d{2}[/-]\d{4})',
        r'(?:EXP|BEST BEFORE|USE BY|BEST BY|EXPIRY)?\s*:?\s*(\d{2}[/-]\d{2}[/-]\d{2})',
        r'(?:EXP|BEST BEFORE|USE BY|BEST BY|EXPIRY)?\s*:?\s*(\d{4}[/-]\d{2}[/-]\d{2})',
        r'(?:EXP|BEST BEFORE|USE BY|BEST BY|EXPIRY)?\s*:?\s*([A-Za-z]{3,9}\s+\d{1,2},?\s+\d{4})',
        r'(?:EXP|BEST BEFORE|USE BY|BEST BY|EXPIRY)?\s*:?\s*(\d{1,2}\s+[A-Za-z]{3,9}\s+\d{4})',
        r'(\d{2}[/-]\d{4})'
    ]
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None

def get_barcode(image):
    codes = decode(image)
    if len(codes) == 0:
        return None
    return codes[0].data.decode("utf-8")

def lookup_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    try:
        r = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "EcoPantryScanner/1.0"}
        )
        if r.status_code == 200:
            data = r.json()
            if data.get("status") == 1:
                product = data.get("product", {})
                name = product.get("product_name") or product.get("product_name_en")
                if name:
                    return name.title()
    except Exception:
        pass
    return "Scanned Package Item"

def save_to_pantry(product_name, category, quantity, expiry_date):
    """Appends scanned product to data/pantry.csv"""
    pantry_path = "data/pantry.csv"
    os.makedirs("data", exist_ok=True)
    
    new_entry = pd.DataFrame([{
        "Product Name": product_name,
        "Category": category,
        "Quantity": quantity,
        "Expiry Date": expiry_date.strftime("%Y-%m-%d"),
        "Added Date": date.today().strftime("%Y-%m-%d")
    }])

    if os.path.exists(pantry_path):
        try:
            df = pd.read_csv(pantry_path)
            df = pd.concat([df, new_entry], ignore_index=True)
        except Exception:
            df = new_entry
    else:
        df = new_entry

    df.to_csv(pantry_path, index=False)

# --- Layout Grid ---
uploaded_file = st.file_uploader(
    "Drop or select a food package image to analyze:",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="metric-label">🖼️ Uploaded Package Media</div>', unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        with st.spinner("⚡ Running AI vision engine & decoding barcode..."):
            # 1. Barcode Search
            barcode = get_barcode(img_array)
            product_name = lookup_product(barcode) if barcode else "Scanned Package Item"

            # 2. OCR Search
            ocr_results = reader.readtext(img_array)
            extracted_text = "\n".join([r[1] for r in ocr_results])
            detected_expiry_str = extract_expiry(extracted_text)
            parsed_expiry_date = parse_date_to_iso(detected_expiry_str)

        st.markdown('### 🔍 Analysis Diagnostics')

        # Product Identification Display
        if barcode:
            safe_prod = html.escape(product_name)
            st.markdown(f"""
                <div class="glow-card-green">
                    <div class="metric-label">📦 Identified Product</div>
                    <div class="metric-value-primary">{safe_prod}</div>
                    <div style="color: #A8E6CF; font-size: 0.85rem; margin-top: 4px;">Barcode: {barcode}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="glow-card-orange">
                    <div class="metric-label">📦 Barcode Recognition</div>
                    <div class="metric-value-warning">⚠️ No barcode pattern detected</div>
                </div>
            """, unsafe_allow_html=True)

        # Expiry Date Display
        if detected_expiry_str:
            safe_exp = html.escape(detected_expiry_str)
            st.markdown(f"""
                <div class="glow-card-green">
                    <div class="metric-label">📅 Detected Expiration Date</div>
                    <div class="metric-value-primary">{safe_exp}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="glow-card-orange">
                    <div class="metric-label">📅 Expiration Recognition</div>
                    <div class="metric-value-warning">⚠️ Expiration text not recognized directly</div>
                </div>
            """, unsafe_allow_html=True)

        # View Raw OCR Logs
        with st.expander("📄 Raw Vision Console Logs"):
            if extracted_text.strip():
                safe_text = html.escape(extracted_text)
                st.markdown(f'<div class="ocr-box">{safe_text}</div>', unsafe_allow_html=True)
            else:
                st.write("No OCR text strings captured.")

    # --- Direct Sync to Pantry Section ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('### 📥 Directly Sync Item to EcoPantry Inventory')
    
    with st.form(key="pantry_sync_form"):
        st.markdown('<div class="add-form-card">', unsafe_allow_html=True)
        
        f1, f2, f3, f4 = st.columns([2, 1.5, 1, 1.5])
        
        with f1:
            form_product_name = st.text_input("Product Name", value=product_name if product_name != "Scanned Package Item" else "")
            
        with f2:
            form_category = st.selectbox(
                "Category", 
                ["Dairy", "Produce", "Bakery", "Beverages", "Snacks", "Meat & Seafood", "Pantry Staples", "Other"],
                index=0
            )
            
        with f3:
            form_quantity = st.number_input("Quantity", min_value=1, value=1, step=1)
            
        with f4:
            form_expiry = st.date_input("Expiry Date", value=parsed_expiry_date)
            
        submit_btn = st.form_submit_button("🚀 Add to Pantry Inventory", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if submit_btn:
            if form_product_name.strip():
                save_to_pantry(form_product_name.strip(), form_category, form_quantity, form_expiry)
                st.success(f"🎉 **{form_product_name}** added to your pantry successfully!")
            else:
                st.error("Please specify a valid product name before submitting.")

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
        <strong style="color: #00FF87;">EcoPantry AI Computer Vision</strong> — Automatic Expiration Extraction<br>
        <span style="opacity: 0.8;">Powered by OpenCV • EasyOCR • PyZbar • OpenFoodFacts</span>
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
