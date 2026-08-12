import streamlit as st

def apply_custom_sidebar_style():
    st.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background-color:#111412 !important;
        border-right:1px solid #1E2521 !important;
    }

    section[data-testid="stSidebar"] ul li a{
        border-radius:10px !important;
        padding:10px 14px !important;
        color:#9EABA2 !important;
        font-weight:500 !important;
        transition:0.2s;
    }

    section[data-testid="stSidebar"] ul li a:hover{
        background:#1A221D !important;
        color:white !important;
    }

    section[data-testid="stSidebar"] ul li a[aria-selected="true"]{
        background:#1E2B22 !important;
        color:white !important;
        font-weight:700 !important;
        border:1px solid rgba(76,175,80,.3) !important;
        box-shadow:0 4px 12px rgba(0,0,0,.3) !important;
    }

    button[data-testid="stSidebarCollapseButton"]{
        color:#818C85 !important;
    }

    button[data-testid="stSidebarCollapseButton"]:hover{
        color:white !important;
    }

    </style>
    """, unsafe_allow_html=True)