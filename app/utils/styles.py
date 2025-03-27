import streamlit as st

def init_styles():
    st.set_page_config(
        page_title="psyche",
        page_icon="🪼",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    page_bg_style = """
    <style>
        .stButton button {
            background-color: #236860;
            color: white;
            padding: 15px 30px;
            border-radius: 25px;
            width: 100%;
        }
        .stTab {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        .css-1d391kg {
            padding: 1rem;
        }
    </style>
    """
    st.markdown(page_bg_style, unsafe_allow_html=True) 