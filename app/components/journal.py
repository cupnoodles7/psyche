import streamlit as st
from datetime import datetime

def journal_page():
    st.title("📝 Personal Journal")
    
    _initialize_journal()
    
    with st.container():
        col1, col2 = st.columns([2, 1])
        
        with col1:
            journal_entry = _create_entry_section()
            
        with col2:
            _journal_actions(journal_entry)
    
    _search_and_display_entries()

def _initialize_journal():
    if 'journal_entries' not in st.session_state:
        st.session_state.journal_entries = []

def _create_entry_section():
    return st.text_area(
        "Write your journal entry here:", 
        height=200, 
        placeholder="What's on your mind today?"
    )

def _journal_actions(journal_entry):
    st.write("### Journal Actions")
    
    if st.button("💾 Save Entry", use_container_width=True):
        _save_entry(journal_entry)
        
    if st.button("🗑️ Clear All Entries", use_container_width=True):
        _clear_entries()

def _save_entry(journal_entry):
    if journal_entry.strip():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.journal_entries.append((current_time, journal_entry))
        st.success("Entry saved successfully!")
        st.rerun()
    else:
        st.error("Please write something before submitting!")

def _clear_entries():
    if st.session_state.journal_entries:
        if st.checkbox("Are you sure you want to clear all entries?"):
            st.session_state.journal_entries = []
            st.success("All entries have been cleared!")
            st.rerun()
    else:
        st.warning("No entries to clear.")

def _search_and_display_entries():
    with st.container():
        st.write("### Search Entries")
        search_term = st.text_input("Search your journal entries:")
        
        if st.session_state.journal_entries:
            _display_filtered_entries(search_term)
        else:
            st.info("No journal entries yet. Start writing your first entry!")

def _display_filtered_entries(search_term):
    filtered_entries = [
        entry for entry in st.session_state.journal_entries 
        if search_term.lower() in entry[1].lower()
    ]
    
    if filtered_entries:
        st.write("### Your Journal Entries")
        for time_sent, message in reversed(filtered_entries):
            with st.expander(f"Entry from {time_sent}"):
                st.write(message)
    else:
        st.info("No entries match your search term.") 