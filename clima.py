import requests

def buscar_clima():
    API_KEY = "eef903a6db71b3a158c197711268a162" 
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    cidade = input("Digite o nome da cidade: ")
    link = f"{BASE_URL}?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

    print("Buscando informações...\n")
    resposta = requests.get(link)

    if resposta.status_code == 200:
        dados = resposta.json()
        descricao = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        sensacao = dados['main']['feels_like']
        umidade = dados['main']['humidity']
        
        print(f"🌤️  Clima agora em {cidade.capitalize()}:")
        print(f"- Situação: {descricao.capitalize()}")
        print(f"- Temperatura: {temperatura}°C")
        print(f"- Sensação Térmica: {sensacao}°C")
        print(f"- Umidade do ar: {umidade}%")
        
    else:
        print(f"❌ Erro na API! Código: {resposta.status_code}")
        print(f"Motivo: {resposta.text}")

buscar_clima()
