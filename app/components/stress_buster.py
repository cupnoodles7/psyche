import streamlit as st

def stress_burster():
    st.title("🧘 Stress Burster")
    
    _init_styles()
    _display_intro()
    _display_spline_design()
    _display_stress_relief_tips()

def _init_styles():
    st.markdown("""
    <style>
    .spline-container {
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        overflow: hidden;
        margin-bottom: 20px;
    }
    .tip-card {
        background: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #236860;
    }
    </style>
    """, unsafe_allow_html=True)

def _display_intro():
    st.markdown("""
    ### Take a Moment to Unwind 
    Interact with our BlueBall and let your stress melt away.
    """)

def _display_spline_design():
    st.markdown("""
    <div class="spline-container">
    <iframe 
        src='https://my.spline.design/aitherapist-e7816283ccca0cc7f2e74c543a304ec1/' 
        frameborder='0' 
        width='100%' 
        height='500px'>
    </iframe>
    </div>
    """, unsafe_allow_html=True)

def _display_stress_relief_tips():
    st.subheader("Quick Stress Relief Tips")
    
    tips = [
        "Take deep, slow breaths",
        "Practice mindfulness",
        "Stretch or do light exercise",
        "Listen to calming music",
        "Take a short walk",
        "Practice progressive muscle relaxation",
        "Visualize a peaceful place"
    ]
    
    for tip in tips:
        st.markdown(f'<div class="tip-card">• {tip}</div>', unsafe_allow_html=True) 