from resp import Resp
from tts import TTS
if __name__ == "__main__":#roda somente se main está aberto
    print("iniciando helper")
    resp = Resp()  # Cria a instância da classe Resp
    resp.ia()
    tts = TTS()
    tts.rodar_tts()
