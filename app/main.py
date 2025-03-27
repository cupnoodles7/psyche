import streamlit as st
from components import resources_page
from utils.styles import init_styles
from dotenv import load_dotenv

from components import (
    VoiceAssistant,
    breathing_center_page,
    therapeutic_activities_page,
    sleep_tracker_page,
    mood_tracker_page,
    journal_page,
    brainrot_corner_page,
    stress_burster,
    game_center_page
) 

def configure():
    load_dotenv()

def main():
    configure()
    init_styles()

    # Create columns to put image and title on the same line
    col1, col2 = st.columns([1.5, 10])

    with col1:
        st.image('logo-no-bg.png', width=100)

    with col2:
        st.title("psyche")
        st.markdown("Your Safe Space for Healing: diagnose and digress.")

    tabs = st.tabs([
        "Chatbot", "Breathing Center", "Therapeutic Activities",
        "Sleep Tracker", "Mood Tracker", "Journal Center", 
        "BrainRot Memes", "Stress Buster", "Game Center"
    ])

    # Map tabs to their respective functions
    tab_functions = {
        0: lambda: VoiceAssistant().run_voice_assistant(),
        1: breathing_center_page,
        2: therapeutic_activities_page,
        3: sleep_tracker_page,
        4: mood_tracker_page,
        5: journal_page,
        6: brainrot_corner_page,
        7: stress_burster,
        8: game_center_page
    }

    # Execute the function for each tab
    for i, tab in enumerate(tabs):
        with tab:
            tab_functions[i]()

    # Add Resources section in sidebar
    with st.sidebar:
        st.title("Additional Resources")
        if st.button("View Mental Health Resources"):
            resources_page()

    st.markdown("""
    Created with ❤ for mental health awareness""", unsafe_allow_html=True)

if __name__ == "__main__":
    main() 