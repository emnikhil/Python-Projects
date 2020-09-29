from gtts import gTTS
from playsound import playsound

#Output file 
audio = 'speech.mp3'
language = 'en'

sp = gTTS(text = "enter your text here which you want to convert into audio file", lang = lanuage, slow = False)

sp.save(audio)
playsound(audio)
