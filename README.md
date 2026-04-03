VoxStream Pro 🎙️

VoxStream Pro is a modern, cross-platform Text-to-Speech (TTS) application designed to bridge the gap between complex digital documents and accessible information.

💖 The Inspiration

This project was created with a special purpose: For my Mother. Many people, including our parents and those with visual impairments, find it difficult or exhausting to read massive text documents or long digital articles. The strain of focusing on small fonts for extended periods can be a significant barrier to staying informed.

VoxStream Pro was built to solve this by transforming any text into clear, spoken audio—enabling users to "read" with their ears and experience their documents without putting unnecessary pressure on their eyes.

🚀 Features

Multi-Language Support: Seamlessly switch between English and Hindi (हिंदी).

Emoji Compatibility: Handles modern text including emojis.

Stable Playback: Dedicated Start and Stop controls for a reliable experience.

Mobile Ready: Built using the Kivy framework, ready to be compiled into an Android APK.

Clean UI/UX: Designed for simplicity so that anyone, regardless of tech-savviness, can use it.

🛠️ Requirements

To run this project locally on Windows/Linux/Mac, you need Python 3.8+ and the following dependencies:

kivy
kivymd
gTTS
requests
certifi
urllib3
idna
charset-normalizer


Installation

pip install -r requirements.txt


📱 How to Build the APK

This app is designed to be built using Buildozer.

Upload main.py and buildozer.spec to a Linux environment (or Google Colab).

Ensure requirements in .spec includes all items from the list above.

Run: buildozer -v android debug

🤝 Credits

Made with ❤️ by Shaurya Vikram Singh
GitHub Profile