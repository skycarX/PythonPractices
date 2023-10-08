from gtts import gTTS
from playsound import playsound

a = input()
s = gTTS(a)
s.save('sample.mp3')
playsound('sample.mp3')