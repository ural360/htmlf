import speech_recognition as speech_recog
from googletrans import Translator
#### V1 - function
def speach():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        word = recog.recognize_google(audio, language="ru-RU")
    
    translator = Translator()
    result = translator.translate(word, dest = 'en')
    return(result.text)



