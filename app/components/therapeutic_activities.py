import streamlit as st
from pathlib import Path
from streamlit_drawable_canvas import st_canvas

def therapeutic_activities_page():
    # Get the absolute path to the assets directory
    assets_dir = Path(__file__).parent.parent / "assets"
    audio_dir = assets_dir / "audio"

    st.title("🎨 Therapeutic Activities")
    
    _init_styles()
    
    # Activities Selection
    activity = st.selectbox(
        "Choose an Activity:",
        ["Art Therapy", "Sound Therapy"]
    )

    activities = {
        "Art Therapy": _art_therapy,
        "Sound Therapy": lambda: _sound_therapy(audio_dir)
    }

    activities[activity]()

def _init_styles():
    st.markdown("""
    <style>
    .activity-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f0);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .activity-card:hover {
        transform: translateY(-5px);
    }
    .canvas-container {
        background: white;
        border-radius: 10px;
        padding: 10px;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
    }
    .visualization-text {
        font-size: 1.2em;
        line-height: 1.6;
        padding: 20px;
        background: rgba(255,255,255,0.9);
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

def _art_therapy():
    st.subheader("🎨 Express Yourself Through Art")
    
    # Initialize session state
    if 'drawing_mode' not in st.session_state:
        st.session_state.drawing_mode = "freedraw"
    if 'stroke_width' not in st.session_state:
        st.session_state.stroke_width = 2
    if 'stroke_color' not in st.session_state:
        st.session_state.stroke_color = "#000000"
    
    # Art tools
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.session_state.drawing_mode = st.selectbox(
            "Drawing Tool:",
            ("freedraw", "line", "rect", "circle")
        )
    with col2:
        st.session_state.stroke_width = st.slider("Brush Size:", 1, 25, 2)
    with col3:
        st.session_state.stroke_color = st.color_picker("Color:", "#000000")
    
    # Canvas for drawing
    st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=st.session_state.stroke_width,
        stroke_color=st.session_state.stroke_color,
        background_color="#FFFFFF",
        background_image=None,
        update_streamlit=True,
        height=400,
        drawing_mode=st.session_state.drawing_mode,
        key="canvas",
    )

def _sound_therapy(audio_dir):
    st.subheader("🎵 Therapeutic Sounds")
    
    sounds = {
        "Ocean Waves": audio_dir / "ocean.mp3",
        "Forest Birds": audio_dir / "forest.mp3",
        "Rainfall": audio_dir / "rain.mp3"
    }
    
    col1, col2 = st.columns(2)
    with col1:
        selected_sound = st.selectbox("Choose a sound:", list(sounds.keys()))
        
    with col2:
        st.markdown("### Sound Settings")
        volume = st.slider("Volume:", 0.0, 1.0, 0.5)
        
    if st.button("Play Sound"):
        try:
            with open(sounds[selected_sound], "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")
        except FileNotFoundError:
            st.error(f"Audio file for {selected_sound} not found. Please ensure it exists in the assets directory.") 