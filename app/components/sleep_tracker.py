import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

def sleep_tracker_page():
    st.title("😴 Sleep Tracker")
    
    _initialize_sleep_tracker()
    _display_sleep_input()
    _display_sleep_statistics()

def _initialize_sleep_tracker():
    if 'sleep_data' not in st.session_state:
        st.session_state.sleep_data = []

def _display_sleep_input():
    st.subheader("Log Your Sleep")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sleep_date = st.date_input("Date:")
        sleep_duration = st.number_input(
            "Hours of sleep:",
            min_value=0.0,
            max_value=24.0,
            value=7.0,
            step=0.5
        )
    
    with col2:
        sleep_quality = st.select_slider(
            "Sleep quality:",
            options=["Poor", "Fair", "Good", "Very Good", "Excellent"],
            value="Good"
        )
        
        factors = st.multiselect(
            "Factors affecting sleep:",
            ["Stress", "Exercise", "Caffeine", "Screen Time", "Noise", "Temperature"]
        )
    
    if st.button("Save Sleep Log"):
        _save_sleep_entry(sleep_date, sleep_duration, sleep_quality, factors)

def _save_sleep_entry(sleep_date, sleep_duration, sleep_quality, factors):
    st.session_state.sleep_data.append({
        'date': sleep_date,
        'duration': sleep_duration,
        'quality': sleep_quality,
        'factors': factors
    })
    st.success("Sleep log saved!")

def _display_sleep_statistics():
    if not st.session_state.sleep_data:
        return
        
    st.subheader("Sleep Statistics")
    
    df = pd.DataFrame(st.session_state.sleep_data)
    fig = _create_sleep_graph(df)
    st.plotly_chart(fig, use_container_width=True)
    
    _display_sleep_metrics(df)

def _create_sleep_graph(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['date'],
        y=df['duration'],
        name='Sleep Duration',
        marker_color='#236860'
    ))
    
    fig.update_layout(
        title='Sleep Duration Over Time',
        xaxis_title='Date',
        yaxis_title='Hours of Sleep',
        height=400
    )
    return fig

def _display_sleep_metrics(df):
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Average Sleep Duration", f"{df['duration'].mean():.1f} hours")
    with col2:
        st.metric("Most Common Quality", df['quality'].mode()[0]) 