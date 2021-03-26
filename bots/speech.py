from gtts import *

text = "Decode online"
speech = gTTS(text= text, lang='en', slow=False)
speech.save("text.mp3")
