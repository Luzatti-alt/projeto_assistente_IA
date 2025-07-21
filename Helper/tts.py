import pyttsx3
class TTS:
    def __init__(self):#metodo que inicia o tts
        self.engine = pyttsx3.init()
        #self.text_to_speak = "iniciando"  # Mensagem default
        self.rate = 150  # Rate padrão
        self.volume = 0.9  # Volume padrão
        self.msg = input("digite seu texto que será convertido para voz: \n")
    def propriedades(self,rate:int,vol:int):
        #indica que o parâmetro e seu tipo
        #tts rate
        self.rate = rate
        self.volume = vol
        self.engine.setProperty('rate', self.rate)
        #tts volume(0-1)
        self.engine.setProperty('volume', self.volume)
    def msg_voz(self,msg : str):
        text_to_speak = msg
    def rodar_tts(self):
        #conversao e tocar
        self.engine.say(self.msg)
        self.engine.runAndWait()
        self.engine.stop()
tts = TTS()
tts.propriedades(150,1)
tts.msg_voz("teste")
tts.rodar_tts()
