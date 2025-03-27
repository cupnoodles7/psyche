# Import all component functions
from .therapeutic_activities import therapeutic_activities_page
from .breathing_center import breathing_center_page
from .sleep_tracker import sleep_tracker_page
from .mood_tracker import mood_tracker_page
from .journal import journal_page
from .brainrot_memes import brainrot_corner_page
from .stress_buster import stress_burster
from .game_center import game_center_page
from .voice_assistant import VoiceAssistant
from .resources import resources_page

# Export all components
__all__ = [
    'therapeutic_activities_page',
    'breathing_center_page',
    'sleep_tracker_page',
    'mood_tracker_page',
    'journal_page',
    'brainrot_corner_page',
    'stress_burster',
    'game_center_page',
    'VoiceAssistant',
    'resources_page'
] 