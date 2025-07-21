import google.generativeai as gemini
from tts import TTS
import os
from dotenv import load_dotenv
# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()
class Resp:
    def ia(self):
        # Carregar a chave da API do ambiente
        API_KEY = os.getenv("GOOGLE_API_KEY")
        # Verificar se a chave API existe
        if not API_KEY:
            print("ATENÇÃO: A chave de API GOOGLE_API_KEY não foi encontrada nas variáveis de ambiente.")
            print("Por favor, defina a variável de ambiente ou substitua 'SUA_API_KEY' abaixo.")
            API_KEY = "SUA_API_KEY_AQUI"  # Substitua por sua chave real de API
        # Configurar a chave da API
        gemini.configure(api_key=API_KEY)
        try:
            # Inicializar o modelo Gemini
            model = gemini.GenerativeModel('models/gemini-1.5-flash-latest')
            # Perguntar ao usuário qual é a dúvida
            prompt = input("Digite sua pergunta: ")
            print(f"\nEnviando prompt ao Gemini: '{prompt}'")
            # Criar o prompt com instruções adicionais
            prompt_2 = f"{prompt} Você é um assistente geral. Você pode realizar tarefas como resumir eventos da semana, pesquisar sobre o assunto perguntado, entre outras coisas."
            # Obter a resposta do modelo Gemini
            resposta = model.generate_content(prompt_2)
            print("\nGemini responde:")
            print(resposta.text)
            # Usar TTS para falar a resposta
            tts = TTS()  # Instanciar o TTS
            tts.msg_voz(resposta.text)  # Passar a resposta para o TTS
            tts.rodar_tts()  # Executar o TTS
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            print("Verifique sua chave de API, a quantidade de usos ou a disponibilidade do serviço.")
# Exemplo de execução
if __name__ == "__main__":
    print("Iniciando o helper...")
    resp = Resp()  # Criar uma instância da classe Resp
    resp.ia()  # Chamar a função ia() para executar o processo
