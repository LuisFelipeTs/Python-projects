#from gtts import gTTS
import os
import pyttsx3


class GoliasSay():

    def __init__(self):
        #self.golias_lenguage = lenguage
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def talk_golias(self, text_say , devagar):
        #self.obj_sayed = gTTS(text=text_say, lang=self.golias_lenguage, slow = devagar)
        #self.obj_sayed.save("golias_sayed.mp3")
        #os.system("mpg321 golias_sayed.mp3")
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate -40)

        self.engine.say(text_say)
        self.engine.runAndWait()
        self.engine.stop()

    
    def remember_last_say(self):
        return
   
    def repeat_golias(self):
        return

        
a = GoliasSay()
a.talk_golias("casa suja chão sujo", False)