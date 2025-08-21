import google.generativeai as gemini
import os
from dotenv import load_dotenv
from mic import Ouvir
from tts import TTS
load_dotenv()
class Resp:
    def ia(self):
        # Carregar a chave da API do arquivo .env
        API_KEY = os.environ.get("G_API_KEY")
        # Verificar se a chave foi carregada corretamente
        if not API_KEY:
            print("ATENÇÃO: A chave de API 'API_KEY' não foi encontrada nas variáveis de ambiente.")
            print("Por favor, defina a variável de ambiente ou substitua diretamente a chave de API no código.")
            API_KEY = G_API_KEY  # Substitua pela sua chave de API, caso não use variáveis de ambiente.
        # Configurar a API Gemini com a chave fornecida
        gemini.configure(api_key=API_KEY)
        try:
            # Definir o modelo Gemini
            model = gemini.GenerativeModel('models/gemini-1.5-flash-latest')
            # Solicitar o prompt do usuário
            prompt = Ouvir()
            print(f"\nEnviando prompt ao Gemini: '{prompt}'")  # Exibir o prompt gerado
            # Adicionar uma condição para a resposta (exemplo: comportamento do assistente)
            prompt_2 = f"{prompt} Você é um assistente geral e pode realizar as seguintes tarefas (temporário enquanto está em fase de testes): resumir eventos da semana, pesquisar sobre o assunto perguntado, entre outras coisas."
            # Gerar a resposta do modelo
            resposta = model.generate_content(prompt_2)
            # Exibir a resposta
            print("\nGemini responde:")
            print(resposta.text)#resposta.text num obj e e, tts ele consulata o resposta.text
            voz = resposta.text  # Agora 'voz' é simplesmente o texto gerado
            print(voz)
            # Instanciar o TTS e passar o texto para ser falado
            tts = TTS()
            tts.msg_voz(voz)  # Passando o texto para o TTS
            tts.rodar_tts()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            print("Verifique sua chave de API, a quantidade de usos ou a disponibilidade do serviço.")
# Main program loop
if __name__ == "__main__":
    resp_instance = Resp()
    while True:
        resp_instance.ia()
