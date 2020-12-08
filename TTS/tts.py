from gtts import gTTS
lan = 'en'
main = input("Stronkfish Brand TTS\n\nText: ")
fn = input("File name: ")
speech = gTTS(text=main, lang=lan, slow=False) 
speech.save(f"{fn}.mp3")
print("Audio Saved.")
