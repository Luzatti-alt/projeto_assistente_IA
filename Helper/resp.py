import google.generativeai as gemini
#chama a api pelo nome gemini
import os
# --- Configuração da API ---
# É altamente recomendável usar variáveis de ambiente para sua chave de API
# Por exemplo, defina a variável de ambiente 'GEMINI_API_KEY' com sua chave. Se estiver testando localmente, você pode definir diretamente para 'SUA_API_KEY',
# REMOVA antes de compartilhar ou implantar.
API_KEY = os.environ.get("API_KEY")
# Se a chave não for encontrada
if not API_KEY:
    print("ATENÇÃO: A chave de API GEMINI_API_KEY não foi encontrada nas variáveis de ambiente.")
    print("Por favor, defina a variável de ambiente ou substitua 'SUA_API_KEY' abaixo.")
    API_KEY = "AIzaSyDGfaG7gLJccDcHfxn7ooNXEEYzE2THStM" #api aqui
gemini.configure(api_key=API_KEY)
#ver modelos disponiveis(esta parte está comentada)

# print("Modelos Gemini disponíveis:")
# for m in gemini.list_models():
    # A propriedade 'name' e 'supported_generation_methods' podem dar uma ideia do que o modelo pode fazer.
    # Não há uma propriedade direta para o "tipo de plano" aqui.
    #if "generateContent" in m.supported_generation_methods:
        #print(f"- {m.name} (Suporta geração de conteúdo)")
try:
    #definir modelo de ia(limitado conforme plano)
    model = gemini.GenerativeModel('models/gemini-1.5-flash-latest')
    # Seu prompt + condição
    prompt = str(input("digite sua pergunta: "))
    #print(f"\nEnviando prompt ao Gemini: '{prompt}'") #prompt que será criado
    prompt_2 = str(prompt)+str("Você é um assitente geral você podera fazer as seguintes tarefas(temporatio enqunato fase de testes: resumir eventos da semana, pesquisar sobre o assunto perguntdo e entre outras coisas)")#{prompt} + condição
    #Gera a resposta
    resposta = model.generate_content(
        prompt_2
        )
    # Imprimir a resposta
    print("\nGemini responde:")
    print(resposta.text)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    print("Verifique sua chave de API, a quantidade de usos ou a disponibilidade do serviço.")
