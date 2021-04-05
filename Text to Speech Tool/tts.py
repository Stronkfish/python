# Google TTS Plugin
from gtts import gTTS

# Language
lan = 'en' 

# Text
main = input("Stronkfish Brand TTS\n\nText: ")

# Filename of Output
fn = input("File name: ")

# Creates TTS File
speech = gTTS(text=main, lang=lan, slow=False) # TTS File Create & Save (5-7)

# Saves TTS File to directory as an MP3 file
speech.save(f"{fn}.mp3")
print("Audio Saved.")
