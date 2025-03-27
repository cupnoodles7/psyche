import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

def mood_tracker_page():
    st.title("📊 Mood Tracker")
    
    _initialize_mood_tracker()
    _display_mood_input()
    _display_mood_history()

def _initialize_mood_tracker():
    if 'mood_history' not in st.session_state:
        st.session_state.mood_history = []

def _display_mood_input():
    st.subheader("How are you feeling today?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        mood_scale = st.slider("Rate your mood (1-10):", 1, 10, 5)
        mood_notes = st.text_area(
            "Any notes about your mood?",
            placeholder="What's affecting your mood today?"
        )
    
    with col2:
        _display_mood_emoji(mood_scale)
        if st.button("Save Mood"):
            _save_mood_entry(mood_scale, mood_notes)

def _display_mood_emoji(mood_scale):
    mood_emojis = {
        1: "😢", 2: "😔", 3: "😕", 4: "😐",
        5: "😊", 6: "😄", 7: "😃", 8: "😁",
        9: "🤗", 10: "🥳"
    }
    st.markdown(f"### {mood_emojis[mood_scale]}")

def _save_mood_entry(mood_scale, mood_notes):
    current_time = datetime.now()
    st.session_state.mood_history.append({
        'date': current_time,
        'mood': mood_scale,
        'notes': mood_notes
    })
    st.success("Mood recorded!")

def _display_mood_history():
    if not st.session_state.mood_history:
        return
    
    st.subheader("Your Mood History")
    
    # Create mood history graph
    df = pd.DataFrame(st.session_state.mood_history)
    fig = _create_mood_graph(df)
    st.plotly_chart(fig, use_container_width=True)
    
    _display_recent_entries()

def _create_mood_graph(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['mood'],
        mode='lines+markers',
        name='Mood',
        line=dict(color='#236860'),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='Mood Over Time',
        xaxis_title='Date',
        yaxis_title='Mood Level',
        yaxis_range=[0, 11],
        height=400
    )
    return fig

def _display_recent_entries():
    st.subheader("Recent Entries")
    mood_emojis = {
        1: "😢", 2: "😔", 3: "😕", 4: "😐",
        5: "😊", 6: "😄", 7: "😃", 8: "😁",
        9: "🤗", 10: "🥳"
    }
    
    for entry in reversed(st.session_state.mood_history[-5:]):
        with st.expander(f"Entry from {entry['date'].strftime('%Y-%m-%d %H:%M')}"):
            st.write(f"Mood: {entry['mood']}/10 {mood_emojis[entry['mood']]}")
            st.write(f"Notes: {entry['notes']}") 