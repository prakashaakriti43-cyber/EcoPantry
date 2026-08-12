import os
import html
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from style import apply_custom_sidebar_style

# --- Initial Page Config ---
st.set_page_config(
    page_title="AI Recipes - EcoPantry", 
    page_icon="🍳", 
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_sidebar_style()

# --- Competition-Grade Custom Styling (CSS) ---
st.markdown("""
    <style>
    /* Dark Cyber-Eco Theme Core */
    .stApp {
        background-color: #080C0A;
        background-image: radial-gradient(circle at 50% -20%, rgba(0, 255, 135, 0.1), transparent 75%);
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

    /* Modern Glass Cards */
    .recipe-card {
        background: rgba(18, 25, 21, 0.75);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(0, 255, 135, 0.18);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        transition: all 0.35s ease;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }

    .recipe-card:hover {
        transform: translateY(-4px);
        border-color: rgba(0, 255, 135, 0.45);
        box-shadow: 0 18px 38px rgba(0, 255, 135, 0.18);
    }

    .recipe-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.6rem;
    }

    .recipe-title {
        color: #FFFFFF;
        font-weight: 800;
        font-size: 1.35rem;
        letter-spacing: -0.3px;
    }

    /* Match Pill Badges */
    .badge-perfect {
        background: linear-gradient(135deg, rgba(0, 255, 135, 0.25) 0%, rgba(0, 200, 83, 0.35) 100%);
        color: #00FF87;
        border: 1px solid rgba(0, 255, 135, 0.5);
        padding: 6px 14px;
        border-radius: 30px;
        font-weight: 800;
        font-size: 0.82rem;
        box-shadow: 0 0 14px rgba(0, 255, 135, 0.25);
    }

    .badge-partial {
        background: rgba(255, 183, 77, 0.15);
        color: #FFB74D;
        border: 1px solid rgba(255, 183, 77, 0.35);
        padding: 6px 14px;
        border-radius: 30px;
        font-weight: 800;
        font-size: 0.82rem;
    }

    /* Ingredient Badges */
    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin: 0.8rem 0;
    }

    .tag-matched {
        background: rgba(0, 255, 135, 0.12);
        color: #00FF87;
        border: 1px solid rgba(0, 255, 135, 0.25);
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    .tag-missing {
        background: rgba(255, 255, 255, 0.05);
        color: #7A8A7E;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.8rem;
        text-decoration: line-through;
    }

    /* Summary Metric Strip */
    .metric-strip {
        background: rgba(18, 25, 21, 0.6);
        border: 1px solid rgba(0, 255, 135, 0.2);
        border-radius: 20px;
        padding: 1.2rem;
        margin-bottom: 1.5rem;
        display: flex;
        justify-content: space-around;
        text-align: center;
        backdrop-filter: blur(12px);
    }

    .metric-item-val {
        color: #00FF87;
        font-size: 1.8rem;
        font-weight: 900;
    }

    .metric-item-lbl {
        color: #8E9B90;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Missing Ingredients Shopping Quick-Card */
    .shopping-card {
        background: rgba(26, 35, 30, 0.8);
        border: 1px solid rgba(0, 255, 135, 0.25);
        border-radius: 16px;
        padding: 1.25rem;
        margin-top: 1.5rem;
        backdrop-filter: blur(10px);
    }

    .shopping-title {
        color: #00FF87;
        font-size: 1.05rem;
        font-weight: 800;
        margin-bottom: 0.6rem;
    }

    .shopping-chip {
        display: inline-block;
        background: rgba(255, 183, 77, 0.12);
        color: #FFB74D;
        border: 1px solid rgba(255, 183, 77, 0.3);
        padding: 4px 12px;
        border-radius: 14px;
        font-size: 0.82rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Hero Header ---
st.markdown("""
    <div class="hero-container">
        <h1 class="page-title">🍳 AI Zero-Waste Recipe Engine</h1>
        <p class="page-subtitle">Transform your current inventory into culinary dishes. Minimize waste, maximize flavor.</p>
    </div>
""", unsafe_allow_html=True)

# --- Expanded Recipe Database with Cook Times ---
RECIPE_DATABASE = [
    {"name": "French Toast", "category": "Breakfast", "time": "10 min", "ingredients": ["Bread", "Eggs", "Milk", "Butter"], "desc": "Whisk eggs and milk, dip bread slices thoroughly, and pan-fry in butter until crisp and golden brown."},
    {"name": "Cheese Sandwich", "category": "Snacks", "time": "5 min", "ingredients": ["Bread", "Cheese", "Butter"], "desc": "Generously butter bread, layer high-melt cheese, and grill on a pan over medium heat until melted and crunchy."},
    {"name": "Classic Pancakes", "category": "Breakfast", "time": "15 min", "ingredients": ["Flour", "Milk", "Eggs", "Butter", "Sugar"], "desc": "Whisk ingredients into a silky batter and pour onto a greased hot griddle until golden and fluffy."},
    {"name": "Avocado Toast", "category": "Breakfast", "time": "5 min", "ingredients": ["Bread", "Avocado", "Olive Oil", "Lemon"], "desc": "Toast crusty bread, mash avocado with fresh lemon juice and olive oil, then spread generously."},
    {"name": "Oatmeal Bowl", "category": "Breakfast", "time": "8 min", "ingredients": ["Oats", "Milk", "Banana", "Honey"], "desc": "Simmer oats in milk until creamy, top with freshly sliced bananas, and drizzle warm honey."},
    {"name": "Tomato Omelette", "category": "Quick Meals", "time": "10 min", "ingredients": ["Eggs", "Tomato", "Cheese"], "desc": "Beat eggs with finely diced tomatoes, cook gently on a pan, and fold over melted cheese."},
    {"name": "Scrambled Eggs with Spinach", "category": "Quick Meals", "time": "8 min", "ingredients": ["Eggs", "Spinach", "Butter", "Cheese"], "desc": "Sauté spinach in butter, pour beaten eggs over top, and scramble softly with shredded cheese."},
    {"name": "Egg Salad Sandwich", "category": "Snacks", "time": "12 min", "ingredients": ["Eggs", "Mayonnaise", "Bread", "Mustard"], "desc": "Hard boil and mash eggs, fold with mayo and mustard, then spread over toasted bread."},
    {"name": "Garlic Butter Pasta", "category": "Italian", "time": "15 min", "ingredients": ["Pasta", "Garlic", "Butter", "Parmesan Cheese"], "desc": "Toss al dente pasta directly into sautéed garlic butter and top with grated parmesan cheese."},
    {"name": "Tomato Basil Pasta", "category": "Italian", "time": "20 min", "ingredients": ["Pasta", "Tomato", "Garlic", "Olive Oil", "Basil"], "desc": "Sauté minced garlic and crushed tomatoes in olive oil, tossing with pasta and fresh basil."},
    {"name": "Creamy Alfredo Pasta", "category": "Italian", "time": "20 min", "ingredients": ["Pasta", "Cream", "Butter", "Garlic", "Parmesan Cheese"], "desc": "Simmer butter, garlic, heavy cream, and parmesan into a rich sauce to thoroughly coat the pasta."},
    {"name": "Cheese Quesadilla", "category": "Mexican", "time": "8 min", "ingredients": ["Tortilla", "Cheese", "Butter"], "desc": "Scatter cheese over half a tortilla, fold over, and toast on a buttered skillet until crisp."},
    {"name": "Chicken Fajita Wrap", "category": "Mexican", "time": "25 min", "ingredients": ["Chicken", "Tortilla", "Bell Pepper", "Onion", "Olive Oil"], "desc": "Sauté chicken, peppers, and onions in olive oil until caramelized, then wrap in warm tortillas."},
    {"name": "Guacamole & Chips", "category": "Snacks", "time": "10 min", "ingredients": ["Avocado", "Tomato", "Onion", "Lime", "Tortilla Chips"], "desc": "Mash avocado with diced tomato, onion, and fresh lime juice. Serve with crunchy tortilla chips."},
    {"name": "Egg Fried Rice", "category": "Asian Inspired", "time": "15 min", "ingredients": ["Rice", "Eggs", "Soy Sauce", "Green Onion", "Oil"], "desc": "Flash stir-fry cold cooked rice with scrambled eggs, dark soy sauce, and chopped green onions."},
    {"name": "Vegetable Stir Fry", "category": "Asian Inspired", "time": "12 min", "ingredients": ["Vegetables", "Soy Sauce", "Garlic", "Oil"], "desc": "Sauté crisp mixed vegetables with minced garlic and soy sauce on high heat."},
    {"name": "Chicken Curry", "category": "Quick Meals", "time": "30 min", "ingredients": ["Chicken", "Onion", "Garlic", "Tomato", "Curry Powder", "Rice"], "desc": "Simmer chicken with sautéed onions, garlic, tomato paste, and curry powder. Serve hot over rice."},
    {"name": "Classic Tomato Soup", "category": "Soups & Salads", "time": "20 min", "ingredients": ["Tomato", "Garlic", "Onion", "Butter", "Cream"], "desc": "Blend roasted tomatoes, garlic, and onions into a velvet broth, finished with a dash of heavy cream."},
    {"name": "Greek Salad", "category": "Soups & Salads", "time": "10 min", "ingredients": ["Cucumber", "Tomato", "Feta Cheese", "Olive Oil", "Olives"], "desc": "Toss chunky cucumber, ripe tomatoes, feta blocks, and olives with virgin olive oil."},
    {"name": "Chicken Caesar Salad", "category": "Soups & Salads", "time": "15 min", "ingredients": ["Chicken", "Lettuce", "Parmesan Cheese", "Croutons", "Caesar Dressing"], "desc": "Grill chicken breast, slice, and serve over romaine lettuce with classic dressing and crunchy croutons."},
    {"name": "Garlic Bread", "category": "Snacks", "time": "12 min", "ingredients": ["Bread", "Butter", "Garlic", "Parsley"], "desc": "Mix softened butter with garlic and parsley, spread generously onto bread, and bake until golden."},
    {"name": "Loaded Baked Potato", "category": "Snacks", "time": "35 min", "ingredients": ["Potato", "Butter", "Cheese", "Sour Cream", "Bacon"], "desc": "Bake potato until tender, slice open, and overload with butter, melted cheese, and sour cream."},
    {"name": "Mashed Potatoes", "category": "Snacks", "time": "20 min", "ingredients": ["Potato", "Butter", "Milk", "Garlic"], "desc": "Boil potatoes until tender, mash smoothly with warm butter, milk, and garlic seasoning."}
]

# --- Inventory Data Loading ---
default_items = sorted([
    "Bread", "Eggs", "Cheese", "Tomato", "Milk", "Butter",
    "Flour", "Sugar", "Pasta", "Garlic", "Onion",
    "Olive Oil", "Chicken", "Rice", "Avocado",
    "Potato", "Spinach", "Cucumber", "Tortilla",
    "Soy Sauce", "Cream", "Parmesan Cheese", "Basil",
    "Mayonnaise", "Mustard", "Tortilla Chips", "Green Onion",
    "Oil", "Curry Powder", "Feta Cheese", "Olives",
    "Lettuce", "Croutons", "Caesar Dressing", "Parsley",
    "Sour Cream", "Bacon", "Honey", "Banana"
])

pantry_path = "data/pantry.csv"

if os.path.exists(pantry_path):
    try:
        df = pd.read_csv(pantry_path)
        pantry_products = df["Product"].dropna().tolist() if "Product" in df.columns else []
        available_ingredients = sorted(list(set(pantry_products + default_items)))
    except Exception:
        available_ingredients = default_items
else:
    available_ingredients = default_items

# --- Ingredient Selection & Filter Controls ---
st.markdown("### 🛒 Active Pantry Selection")

col_sel, col_cat_filter = st.columns([3, 1])

with col_sel:
    selected = st.multiselect(
        "Select available pantry ingredients:",
        options=available_ingredients,
        default=["Bread", "Eggs", "Cheese", "Tomato", "Butter", "Garlic"]
    )

with col_cat_filter:
    all_categories = ["All Cuisine Types"] + list(set([r["category"] for r in RECIPE_DATABASE]))
    selected_cuisine = st.selectbox("Filter Cuisine / Course:", all_categories)

# --- Process Recipe Matching Logic ---
selected_set = set([s.lower() for s in selected])
matched_recipes = []
missing_ingredients_global = set()

for r in RECIPE_DATABASE:
    if selected_cuisine != "All Cuisine Types" and r["category"] != selected_cuisine:
        continue

    req_set = set([i.lower() for i in r["ingredients"]])
    matching_set = req_set.intersection(selected_set)
    missing_set = req_set - selected_set
    matching_count = len(matching_set)
    
    if matching_count > 0:
        match_percentage = int((matching_count / len(req_set)) * 100)
        missing_list = [i for i in r["ingredients"] if i.lower() in missing_set]
        
        if match_percentage < 100:
            for item in missing_list:
                missing_ingredients_global.add(item)

        matched_recipes.append({
            "recipe": r,
            "matches": matching_count,
            "percentage": match_percentage,
            "matched_ingredients": [i for i in r["ingredients"] if i.lower() in matching_set],
            "missing_ingredients": missing_list
        })

# Sort recipes by highest percentage match, then by most matching ingredients
matched_recipes.sort(
    key=lambda x: (x["percentage"], x["matches"]),
    reverse=True
)

st.markdown("<br>", unsafe_allow_html=True)

# --- Recipe Render Section ---
if matched_recipes:
    perfect_matches = [m for m in matched_recipes if m["percentage"] == 100]
    
    # Metric Summary Strip
    st.markdown(f"""
        <div class="metric-strip">
            <div>
                <div class="metric-item-val">{len(matched_recipes)}</div>
                <div class="metric-item-lbl">Dishes Available</div>
            </div>
            <div>
                <div class="metric-item-val" style="color: #00FF87;">{len(perfect_matches)}</div>
                <div class="metric-item-lbl">100% Ready To Cook</div>
            </div>
            <div>
                <div class="metric-item-val" style="color: #FFB74D;">{len(matched_recipes) - len(perfect_matches)}</div>
                <div class="metric-item-lbl">Partial Matches</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Filtering Tabs
    filter_option = st.radio(
        "Match Criteria:",
        ["All Matches", "100% Ready Only", "Partial Matches"],
        horizontal=True
    )

    if filter_option == "100% Ready Only":
        display_recipes = perfect_matches
    elif filter_option == "Partial Matches":
        display_recipes = [m for m in matched_recipes if m["percentage"] < 100]
    else:
        display_recipes = matched_recipes

    st.markdown("<br>", unsafe_allow_html=True)

    # Render Recipe Cards Grid
    col1, col2 = st.columns(2)
    
    for idx, item in enumerate(display_recipes):
        r = item["recipe"]
        pct = item["percentage"]
        matched_tags = "".join([f'<span class="tag-matched">✓ {i}</span>' for i in item["matched_ingredients"]])
        missing_tags = "".join([f'<span class="tag-missing">✗ {i}</span>' for i in item["missing_ingredients"]])
        
        badge_html = f'<span class="badge-perfect">✨ {pct}% Match</span>' if pct == 100 else f'<span class="badge-partial">⚡ {pct}% Match</span>'
        
        safe_name = html.escape(r["name"])
        safe_category = html.escape(r["category"])
        safe_time = html.escape(r["time"])
        safe_desc = html.escape(r["desc"])
        
        card_html = f"""<div class="recipe-card">
<div class="recipe-header">
<div class="recipe-title">🍽️ {safe_name}</div>
{badge_html}
</div>
<div style="color:#8E9B90; font-size:0.82rem; font-weight:700; margin-bottom:0.4rem;">
🏷️ {safe_category} • ⏱️ {safe_time}
</div>
<div class="tag-container">
{matched_tags}
{missing_tags}
</div>
<p style="color:#E0E0E0; font-size:0.92rem; line-height:1.5; margin-top:0.6rem;">
{safe_desc}
</p>
</div>"""
        
        if idx % 2 == 0:
            col1.markdown(card_html, unsafe_allow_html=True)
        else:
            col2.markdown(card_html, unsafe_allow_html=True)

    # Missing Ingredients Quick-Add Drawer
    if missing_ingredients_global:
        st.markdown(f"""
            <div class="shopping-card">
                <div class="shopping-title">🛍️ Quick Shopping List (Ingredients to Unlock More Dishes)</div>
                <div>
                    {"".join([f'<span class="shopping-chip">+ {item}</span>' for item in sorted(list(missing_ingredients_global))[:10]])}
                </div>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("No recipes found with selected ingredients. Try selecting additional items above!")

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
        <strong style="color: #00FF87;">EcoPantry AI Recipe Engine</strong> — Zero Food Waste Meal Generation<br>
        <span style="opacity: 0.8;">Made with Python • Streamlit • AI Intelligence</span>
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