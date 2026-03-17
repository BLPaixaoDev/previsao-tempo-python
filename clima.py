import requests

def buscar_clima():
    # 1. Configurações da API
    # Substitua "SUA_CHAVE_AQUI" pela chave que você pegou no site
    API_KEY = "eef903a6db71b3a158c197711268a162" 
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    # 2. Entrada do usuário
    cidade = input("Digite o nome da cidade: ")

    # 3. Montando o link da requisição 
    # Usamos lang=pt_br para português e units=metric para graus Celsius
    link = f"{BASE_URL}?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

    # 4. Fazendo a requisição na internet
    print("Buscando informações...\n")
    resposta = requests.get(link)

    # 5. Verificando se deu certo (O código 200 significa "Sucesso!")
    if resposta.status_code == 200:
        # Transformando a resposta em um formato que o Python entende (JSON/Dicionário)
        dados = resposta.json()
        
        # Extraindo as informações que queremos do dicionário
        descricao = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        sensacao = dados['main']['feels_like']
        umidade = dados['main']['humidity']
        
        # 6. Exibindo o resultado na tela
        print(f"🌤️  Clima agora em {cidade.capitalize()}:")
        print(f"- Situação: {descricao.capitalize()}")
        print(f"- Temperatura: {temperatura}°C")
        print(f"- Sensação Térmica: {sensacao}°C")
        print(f"- Umidade do ar: {umidade}%")
        
    else:
        # Caso o usuário digite uma cidade que não existe ou a API falhe
        print(f"❌ Erro na API! Código: {resposta.status_code}")
        print(f"Motivo: {resposta.text}")

# Executa o programa
buscar_clima()