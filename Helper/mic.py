import speech_recognition as sr
def Ouvir():
    #aqui pega o audio e manda para a ia
    mic = sr.Microphone()
    recognizer = sr.Recognizer()
    with mic as source:
        print("escutando")
        audio = recognizer.listen(source)
        try:
            frase = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Foi dito: {frase}")
        except sr.UnknownValueError:
            print("Não entendi o que foi dito")
        except sr.RequestError as e:
            print(f"Erro ao se conectar ao serviço Google: {e}")
Ouvir()