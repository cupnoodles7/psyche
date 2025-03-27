import streamlit as st
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import sounddevice as sd
import wave
import numpy as np
from threading import Thread
import os

class VoiceAssistant:
    def __init__(self):
        self._initialize_components()

    def _initialize_components(self):
        try:
            api_key = os.getenv("GOOGLE_AI_API_KEY") or st.secrets.get("GOOGLE_AI_API_KEY")

            if not api_key:
                st.error("Google AI API Key is missing. Please configure it.")
                st.stop()

            genai.configure(api_key=api_key)

            # Initialize components
            self.model = genai.GenerativeModel(model_name='gemini-1.5-flash')
            self.recognizer = sr.Recognizer()
            self.tts_engine = pyttsx3.init()
            
            # Configure TTS settings
            self.tts_engine.setProperty("rate", 150)
            self.tts_engine.setProperty("volume", 0.8)

        except Exception as e:
            st.error(f"Initialization Error: {e}")
            st.stop()

    @st.cache_resource
    def generate_response(_self, user_message):
        if not user_message:
            return "Sorry, I didn't hear anything."

        try:
            prompt = f"""Answer as a mental health therapist in English language only. 
            Reply within 100 words. 
            Give answers as a mental health diagnosis response, 
            if not reply 'I cannot answer that question'.
            User message: {user_message}"""
        
            response = _self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            st.error(f"AI response generation error: {e}")
            return "Sorry, I encountered an error processing your request."

    def record_audio(self, duration=5):
        try:
            st.info(f"Recording for {duration} seconds...")
            recording = sd.rec(
                int(duration * 16000),
                samplerate=16000,
                channels=1,
                dtype='float32'
            )
            sd.wait()

            wav_filename = "recorded_audio.wav"
            with wave.open(wav_filename, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(16000)
                wf.writeframes((recording * 32767).astype(np.int16).tobytes())

            return wav_filename
        except Exception as e:
            st.error(f"Audio recording error: {e}")
            return None

    @st.cache_data
    def transcribe_audio(_self, wav_filename):
        if not wav_filename:
            return ""

        try:
            with sr.AudioFile(wav_filename) as source:
                audio = _self.recognizer.record(source)
                return _self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            st.warning("Could not understand audio")
            return ""
        except sr.RequestError as e:
            st.error(f"Speech recognition service error: {e}")
            return ""
        except Exception as e:
            st.error(f"Transcription error: {e}")
            return ""

    def text_to_speech(self, text):
        try:
            def speak():
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()

            tts_thread = Thread(target=speak, daemon=True)
            tts_thread.start()
        except Exception as e:
            st.error(f"Speech synthesis error: {e}")

    def run_voice_assistant(self):
        st.title("🌼Real-Time Mental health Diagnosis Assistance")
        st.markdown("### Say hi to your personal assistant!")

        user_message = st.text_input("Or type your message")

        if st.button("Click to address your concerns") or user_message:
            if user_message:
                self._handle_text_input(user_message)
            else:
                self._handle_voice_input()

    def _handle_text_input(self, user_message):
        st.markdown(f"You: {user_message}")
        response = self.generate_response(user_message)
        st.markdown(f"Assistant: {response}")
        self.text_to_speech(response)

    def _handle_voice_input(self):
        audio_file = self.record_audio(duration=10)
        if audio_file:
            user_message = self.transcribe_audio(audio_file)
            if user_message:
                st.markdown(f"You: {user_message}")
                response = self.generate_response(user_message)
                st.markdown(f"Assistant: {response}")
                self.text_to_speech(response)
            else:
                st.warning("No speech detected. Please try again.") 