import speech_recognition as sr


 
class GoliasEar():

    def __init__(self):
        self.a = 1
        
    def ouvir_microfone(self):
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            print("Diga alguma coisa: ")
            audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio,language='pt-BR')
            print("Você disse: " + frase)
        except sr.UnkownValueError:
            print("Não entendi")
        return frase

a = GoliasEar()
a.ouvir_microfone()