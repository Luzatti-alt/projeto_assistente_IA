import google.generativeai as gemini
from tts import TTS
import os
from dotenv import load_dotenv
load_dotenv()
class Resp:
    def ia(self):
        # Carregar a chave da API do arquivo .env
        API_KEY = os.environ.get("GOOGLE_API_KEY")
        # Verificar se a chave foi carregada corretamente
        if not API_KEY:
            print("ATENÇÃO: A chave de API 'GOOGLE_API_KEY' não foi encontrada nas variáveis de ambiente.")
            print("Por favor, defina a variável de ambiente ou substitua diretamente a chave de API no código.")
            API_KEY = "SUA_CHAVE_AQUI"  # Substitua pela sua chave de API, caso não use variáveis de ambiente.
        # Configurar a API Gemini com a chave fornecida
        gemini.configure(api_key=API_KEY)
        try:
            # Definir o modelo Gemini
            model = gemini.GenerativeModel('models/gemini-1.5-flash-latest')
            # Solicitar o prompt do usuário
            prompt = str(input("Digite sua pergunta: "))
            print(f"\nEnviando prompt ao Gemini: '{prompt}'")  # Exibir o prompt gerado
            # Adicionar uma condição para a resposta (exemplo: comportamento do assistente)
            prompt_2 = f"{prompt} Você é um assistente geral e pode realizar as seguintes tarefas (temporário enquanto está em fase de testes): resumir eventos da semana, pesquisar sobre o assunto perguntado, entre outras coisas."
            # Gerar a resposta do modelo
            resposta = model.generate_content(prompt_2)
            # Exibir a resposta
            print("\nGemini responde:")
            print(resposta.text)
            # Instanciar a classe TTS e gerar a voz a partir da resposta
            tts = TTS()
            print("Passando a resposta para o TTS...")
            tts.msg_voz(resposta.text)
            # Executar o TTS para gerar o áudio
            print("Iniciando o TTS...")
            tts.rodar_tts()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            print("Verifique sua chave de API, a quantidade de usos ou a disponibilidade do serviço.")
# Criar um objeto da classe e chamar o método ia
resp = Resp()
resp.ia()
