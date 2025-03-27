import streamlit as st

def resources_page():
    st.title("🆘 Mental Health Resources")
    
    _display_emergency_contacts()
    _display_self_help_resources()
    _display_mental_health_tips()

def _display_emergency_contacts():
    st.header("Emergency Contacts")
    
    emergency_contacts = {
        "National Crisis Hotline": "1-800-273-8255",
        "Crisis Text Line": "Text HOME to 741741",
        "Emergency Services": "911"
    }
    
    for service, contact in emergency_contacts.items():
        st.markdown(f"*{service}*: {contact}")

def _display_self_help_resources():
    st.header("Self-Help Resources")
    
    resources = {
        "Meditation Apps": [
            "Headspace",
            "Calm",
            "Insight Timer",
            "Simple Habit"
        ],
        "Educational Resources": [
            "National Institute of Mental Health",
            "Mental Health America",
            "Psychology Today",
            "Mind.org"
        ],
        "Support Groups": [
            "NAMI Support Groups",
            "Depression and Bipolar Support Alliance",
            "Anxiety and Depression Association of America"
        ]
    }
    
    for category, items in resources.items():
        with st.expander(category):
            for item in items:
                st.markdown(f"- {item}")

def _display_mental_health_tips():
    st.header("Quick Mental Health Tips")
    
    tips = [
        "Practice deep breathing exercises",
        "Maintain a regular sleep schedule",
        "Exercise regularly",
        "Stay connected with loved ones",
        "Practice mindfulness",
        "Set realistic goals",
        "Take breaks when needed"
    ]
    
    for tip in tips:
        st.markdown(f"• {tip}") 