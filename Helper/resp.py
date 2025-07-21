import google.generativeai as gemini
#chama a api pelo nome gemini
import os
class resp:
    def ia:
        API_KEY = os.environ.get("API_KEY")
        if not API_KEY:
            print("ATENÇÃO: A chave de API GEMINI_API_KEY não foi encontrada nas variáveis de ambiente.")
            print("Por favor, defina a variável de ambiente ou substitua 'SUA_API_KEY' abaixo.")
            API_KEY = "AIzaSyDGfaG7gLJccDcHfxn7ooNXEEYzE2THStM" #api aqui
        gemini.configure(api_key=API_KEY)
    try:
        model = gemini.GenerativeModel('models/gemini-1.5-flash-latest')
        prompt = str(input("digite sua pergunta: "))
        print(f"\nEnviando prompt ao Gemini: '{prompt}'") #prompt que será criado
        prompt_2 = str(prompt)+str("Você é um assitente geral você podera fazer as seguintes tarefas(temporatio enqunato fase de testes: resumir eventos da semana, pesquisar sobre o assunto perguntdo e entre outras coisas)")#{prompt} + condição
        resposta = model.generate_content(
            prompt_2
        )
        print("\nGemini responde:")
        print(resposta.text)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print("Verifique sua chave de API, a quantidade de usos ou a disponibilidade do serviço.")
