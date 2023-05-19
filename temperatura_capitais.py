import requests
import pandas as pd
from datetime import datetime

api_key = "API_KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?q="

# Obter a data e hora atual
date_time = datetime.now()

# Lista das capitais do Brasil
capitais = ['Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília', 'Vitória',
            'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 'Belo Horizonte', 'Belém', 'João Pessoa',
            'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal', 'Porto Alegre', 'Porto Velho',
            'Boa Vista', 'Florianópolis', 'São Paulo', 'Aracaju', 'Palmas']

# Lista das siglas dos estados do Brasil
estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
           'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

# Lista vazia para armazenar os dados das capitais
dados_capitais = []

# Obter a temperatura das capitais
for capital in capitais:
    url = f"{base_url}{capital}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        # Se houver dados de temperatura disponíveis, adicionar à lista 'dados_capitais'
        if "main" in data:
            temp = data["main"]["temp"]
            temp_celsius = round(temp - 273.15, 2)
            estado = estados[capitais.index(capital)]
            hora_local = date_time.strftime('%H:%M:%S')
            dados_capitais.append({"uf": estado, "cidade": capital, "temperatura": temp_celsius, "data": date_time,
                                   "hora_local": hora_local})
        else:
            print(f"Não foi possível obter a temperatura de {capital}.")
    except:
        print(f"Não foi possível acessar a API para obter a temperatura de {capital}.")

# Criar um DataFrame com os dados das capitais
df = pd.DataFrame(dados_capitais)

# Converter temperatura para formato 'int'
df["temperatura"] = df["temperatura"].apply(lambda x: round(float(x)))

# Converter as colunas 'data' e 'hora_local' em objeto de data e hora
df['data'] = pd.to_datetime(df['data']).dt.date
hora_local = pd.to_datetime(df['hora_local'], format='%H:%M:%S').dt.time.astype(str)

# Exibe o DataFrame
data_frame = df
print(data_frame)
