# Temperatura das Capitais Brasileiras
Este projeto utiliza a API do OpenWeatherMap para obter a temperatura atual das capitais do Brasil e armazena os dados em um DataFrame para análise posterior.

## Requisitos
- Python instalado
- Bibliotecas Python: requests, pandas, datetime
 
## Configuração
Obtenha uma chave de API do OpenWeatherMap em https://openweathermap.org/ (gratuita para uso não comercial).
Substitua a variável api_key no código pelo valor da sua chave de API.

## Funcionalidades
O programa faz uma solicitação à API do OpenWeatherMap para cada capital brasileira e obtém os dados da temperatura atual.
Os dados da temperatura são armazenados em um DataFrame, juntamente com informações adicionais, como estado, cidade, data e hora local.
O DataFrame resultante é exibido no console.

## Como usar
Certifique-se de ter todas as bibliotecas necessárias instaladas.
Execute o código em um ambiente Python.
O programa exibirá uma lista das capitais do Brasil.

##Limitações
A disponibilidade dos dados de temperatura depende da resposta da API do OpenWeatherMap. Se a API estiver indisponível ou retornar um erro, os dados podem não ser obtidos corretamente.
A precisão da temperatura depende das informações fornecidas pela API e pode variar.
Este projeto é apenas uma demonstração e pode ser expandido ou adaptado para requisitos específicos.

## Recursos
Documentação do OpenWeatherMap: https://openweathermap.org/
Documentação das bibliotecas Python:
requests: https://docs.python-requests.org/
pandas: https://pandas.pydata.org/
datetime: https://docs.python.org/3/library/datetime.html

## Aviso Legal
Este projeto é apenas para fins educacionais e não se destina a ser usado em produção.
