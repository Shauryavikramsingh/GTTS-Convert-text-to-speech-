import os
import threading
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from gtts import gTTS
from kivy.core.audio import SoundLoader
import webbrowser

# UI Design in KV Language
KV = '''
MDScreen:
    md_bg_color: self.theme_cls.bg_dark

    MDBoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "15dp"

        MDTopAppBar:
            title: "VoxStream Mobile"
            elevation: 4
            pos_hint: {"top": 1}
            right_action_items: [["github", lambda x: app.open_github()]]

        MDLabel:
            text: "Enter text to convert to speech"
            halign: "center"
            theme_text_color: "Secondary"
            font_style: "H6"
            size_hint_y: None
            height: self.texture_size[1]

        MDTextField:
            id: text_input
            hint_text: "Type something..."
            mode: "fill"
            multiline: True
            fill_color_normal: 0, 0, 0, .2
            size_hint_y: 0.6

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: "20dp"
            size_hint_y: None
            height: "60dp"
            padding: [20, 0, 20, 0]

            MDRaisedButton:
                id: play_btn
                text: "START VOICE"
                md_bg_color: 0.15, 0.65, 0.27, 1 # Success Green
                size_hint_x: 0.5
                on_release: app.start_tts_thread()

            MDRaisedButton:
                id: stop_btn
                text: "STOP VOICE"
                md_bg_color: 0.86, 0.2, 0.27, 1 # Danger Red
                size_hint_x: 0.5
                disabled: True
                on_release: app.stop_audio()

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: "80dp"
            spacing: "5dp"

            MDLabel:
                text: "Made with [color=#ff0000]❤️[/color] by Shaurya Vikram Singh"
                markup: True
                halign: "center"
                theme_text_color: "Hint"
                font_style: "Caption"

            MDIconButton:
                icon: "github"
                pos_hint: {"center_x": .5}
                user_font_size: "30sp"
                on_release: app.open_github()
'''

class VoxStreamApp(MDApp):
    sound = None
    temp_file = "speech.mp3"

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def open_github(self):
        webbrowser.open("https://github.com/Shauryavikramsingh")

    def stop_audio(self):
        if self.sound:
            self.sound.stop()
            self.sound.unload()
        self.root.ids.play_btn.disabled = False
        self.root.ids.stop_btn.disabled = True
        self.root.ids.play_btn.text = "START VOICE"

    def start_tts_thread(self):
        text = self.root.ids.text_input.text.strip()
        if not text:
            return
        
        self.root.ids.play_btn.disabled = True
        self.root.ids.play_btn.text = "PROCESSING..."
        threading.Thread(target=self.generate_and_play, args=(text,), daemon=True).start()

    def generate_and_play(self, text):
        try:
            tts = gTTS(text=text, lang='en')
            tts.save(self.temp_file)
            
            # Load and play on main thread
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self.play_file())
        except Exception as e:
            print(f"Error: {e}")
            self.reset_ui()

    def play_file(self):
        self.sound = SoundLoader.load(self.temp_file)
        if self.sound:
            self.root.ids.stop_btn.disabled = False
            self.root.ids.play_btn.text = "SPEAKING..."
            self.sound.play()
            # Bind event for when audio finishes
            self.sound.bind(on_stop=lambda x: self.reset_ui())
        else:
            self.reset_ui()

    def reset_ui(self):
        self.root.ids.play_btn.disabled = False
        self.root.ids.stop_btn.disabled = True
        self.root.ids.play_btn.text = "START VOICE"

if __name__ == "__main__":
    VoxStreamApp().run()