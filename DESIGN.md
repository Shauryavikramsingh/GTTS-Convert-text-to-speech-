Design and Architecture: VoxStream Pro

🎯 User-Centric Vision

The primary design goal was Accessibility. Because the target audience includes people who may suffer from eye strain (like my mother), the interface follows these rules:

High Contrast: A dark theme is used by default to reduce blue light exposure.

Large Touch Targets: Buttons are sized appropriately for mobile use and for users who may not have precise motor control.

Simplicity: No hidden menus. Every function (Play, Stop, Language) is visible on the main screen.

🏗️ Technical Stack

UI Framework: Kivy & KivyMD. Chosen for cross-platform compatibility (Windows/Android) and GPU acceleration.

TTS Engine: gTTS (Google Text-to-Speech). Chosen for its high-quality, natural-sounding synthesis and native support for Hindi Unicode.

State Management: Uses Python's threading module to ensure the UI remains responsive (non-blocking) while generating audio files.

🧩 Architectural Flow

Input Layer: Captures UTF-8 text from the user.

Processing Layer: A background thread sends the text to the Google TTS API.

Storage Layer: A temporary .mp3 file is cached locally.

Output Layer: Kivy's SoundLoader interacts with the device's native audio drivers to play or stop the sound.

🌍 Language Strategy

To support Hindi and Emojis, the app utilizes UTF-8 encoding throughout the pipeline. The Language Toggle updates the gTTS lang parameter, switching the phonetic engine to provide the correct accent and pronunciation for the selected culture.