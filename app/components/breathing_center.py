import streamlit as st
import time

def breathing_center_page():
    st.header("🫁 Breathing Center")
    
    _init_styles()
    
    container = st.container()
    
    with container:
        st.markdown('<div class="breathing-circle"></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col2:
            breathing_exercise = _select_exercise()
            _display_exercise_description(breathing_exercise)
            _setup_controls()

def _init_styles():
    st.markdown("""
        <style>
        @keyframes breathe {
            0% { transform: scale(1); opacity: 0.3; }
            50% { transform: scale(1.5); opacity: 0.8; }
            100% { transform: scale(1); opacity: 0.3; }
        }
        .breathing-circle {
            width: 150px;
            height: 150px;
            background: radial-gradient(circle, #236860, #2E7D32);
            border-radius: 50%;
            margin: 40px auto;
            animation: breathe 8s infinite ease-in-out;
            box-shadow: 0 0 30px rgba(46, 125, 50, 0.3);
        }
        </style>
    """, unsafe_allow_html=True)

def _select_exercise():
    return st.selectbox(
        "Select a breathing exercise:",
        ["Box Breathing", "4-7-8 Breathing", "Deep Breathing"]
    )

def _display_exercise_description(exercise):
    descriptions = {
        "Box Breathing": """🔲 Box breathing is a powerful stress-relief technique used by Navy SEALs. 
        Perfect for maintaining calm and focus under pressure.""",
        "4-7-8 Breathing": """🌙 The 4-7-8 breathing technique helps reduce anxiety and aids better sleep. 
        Practiced twice daily, it becomes more effective over time.""",
        "Deep Breathing": """🌊 Deep breathing is a simple yet effective way to reduce stress and increase mindfulness. 
        It helps activate your body's natural relaxation response."""
    }
    
    st.markdown(
        f'<div class="exercise-card">{descriptions[exercise]}</div>', 
        unsafe_allow_html=True
    )

def _setup_controls():
    controls_col1, controls_col2 = st.columns([2, 2])
    with controls_col1:
        start_button = st.button("Start Exercise 🎯", use_container_width=True)
    with controls_col2:
        play_music = st.checkbox("🎵 Play Meditation Music")
        
    if play_music:
        _play_meditation_music()
        
    if start_button:
        _run_breathing_exercise()

def _play_meditation_music():
    try:
        audio_file = open('app/assets/audio/meditation.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    except FileNotFoundError:
        st.error("Meditation audio file not found.")

def _run_breathing_exercise():
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    exercise_type = st.session_state.get('breathing_exercise', "Box Breathing")
    _execute_exercise(exercise_type, progress_bar, status_text)

def _execute_exercise(exercise_type, progress_bar, status_text):
    if exercise_type == "Box Breathing":
        _box_breathing(progress_bar, status_text)
    elif exercise_type == "4-7-8 Breathing":
        _four_seven_eight_breathing(progress_bar, status_text)
    else:
        _deep_breathing(progress_bar, status_text) 
        
    st.success("✨ Exercise completed! Take a moment to notice how you feel.")
    
    
def _box_breathing(progress_bar, status_text):
    for cycle in range(4):
                        for phase, duration in [("Inhale", 4), ("Hold", 4), ("Exhale", 4), ("Hold", 4)]:
                            status_text.markdown(
                                f'<p class="timer-text">{phase}</p>', unsafe_allow_html=True)
                            for i in range(duration):
                                progress_bar.progress((i + 1) / duration)
                                time.sleep(1)
                            progress_bar.progress(0)
                        
def _four_seven_eight_breathing(progress_bar, status_text):
    for cycle in range(4):
                        for phase, duration in [("Inhale", 4), ("Hold", 7), ("Exhale", 8)]:
                            status_text.markdown(
                                f'<p class="timer-text">{phase}</p>', unsafe_allow_html=True)
                            for i in range(duration):
                                progress_bar.progress((i + 1) / duration)
                                time.sleep(1)
                            progress_bar.progress(0)
                            
def _deep_breathing(progress_bar, status_text):
    for cycle in range(4):
                        for phase, duration in [("Inhale Deeply", 4), ("Hold", 2), ("Exhale Slowly", 4), ("Rest", 2)]:
                            status_text.markdown(
                                f'<p class="timer-text">{phase}</p>', unsafe_allow_html=True)
                            for i in range(duration):
                                progress_bar.progress((i + 1) / duration)
                                time.sleep(1)
                            progress_bar.progress(0)
                            