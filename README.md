# psyche🪼

## Overview

Psyche is an AI-powered mental health diagnosis and support system designed to assist individuals in evaluating their mental well-being and engaging in therapeutic activities. The platform integrates artificial intelligence with interactive wellness tools, making mental health support more accessible and personalized.

## ✨ Features

### AI-Powered Mental Health Assessment

- **AI-driven chat** for preliminary mental health evaluations
- **Sentiment analysis** for mood detection
- **Personalized mental wellness recommendations**

### Interactive Wellness Tools

- **Breathing Center** 🧐: Guided breathing exercises
- **Therapeutic Activities** 🎨: Art and sound therapy
- **Sleep Tracker** 😴: Monitor sleep patterns
- **Mood Tracker** 📊: Visualize emotional states
- **Journal Center** 📝: Private space for self-reflection
- **Stress Buster** 🧘‍♀️: Interactive stress relief activities
- **Game Center** 🎮: Mental wellness games

### Additional Features

- **BrainRot Memes** 😄: Lighthearted entertainment
- **Resources Hub** 🆘: Access to mental health resources

### Deployed Link on Streamlit Cloud

- **https://psyche-qwqywyuekbgvtsejkzrtkk.streamlit.app/**
  (Currently does not support the voice input feature and large audio files due to Streamlit Cloud limitations )

### Demonstrations & Screenshots

![Image](https://github.com/user-attachments/assets/874c4deb-c9e7-4d0c-b0a4-be839d2d99a8)

![Image](https://github.com/user-attachments/assets/7f487cf2-6b86-4eb6-86af-619ad74622bc)

![Image](https://github.com/user-attachments/assets/3a1ae3f8-c788-4dbc-b9d0-8b84bb03c9d4)

![Image](https://github.com/user-attachments/assets/c8cd7c27-3d06-496b-8e48-481d9344b301)

![Image](https://github.com/user-attachments/assets/6e0b70c5-666e-4061-8753-82f7783ad1cf)

![Image](https://github.com/user-attachments/assets/083d8e8f-e787-4406-8c1a-34e1266b0aad)

![Image](https://github.com/user-attachments/assets/52da5966-c29b-41d5-8899-abaeaa0a818b)

![Image](https://github.com/user-attachments/assets/9e727ca5-1090-4389-b5af-90e4c8b7cdc6)

![Image](https://github.com/user-attachments/assets/d99d3f6e-fa5d-4410-8caa-c9688809c36f)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/cupnoodles7/psyche.git
cd psyche
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows
venv\Scripts\activate

# For Unix/MacOS
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API keys

## 🎮 Running the Application

### 1. Start the Streamlit Server

```bash
streamlit run app.py
```

### 2. Access the Application

Open your web browser and navigate to:

```
http://localhost:8501
```

## 🛋️ Dependencies

- streamlit
- speech_recognition
- clarifai-grpc
- gTTS
- streamlit-drawable-canvas
- plotly
- pandas
- numpy
- scipy
- requests

## 🛠 Configuration

- Clarifai API for AI chat functionality
- Gemini API for voice assistance
- Various audio files for sound therapy
- Custom UI components and styling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
