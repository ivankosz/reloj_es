from gtts import gTTS

from playsound import playsound

def decir_hora(text):
    
    audio = 'audio.mp3'

    language = 'es'

    sp = gTTS(text, lang=language, slow=False)

    sp.save(audio)
    playsound(audio)

