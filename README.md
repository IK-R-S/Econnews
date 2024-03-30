# Econnews 📈
**Notícias descentralizadas sobre economia e finanças**

Econnews consiste em uma API pública que fornece notícias sobre economia de diferentes fontes midiáticas. A API é acessada através de endpoints específicos e retorna informações atualizadas em tempo real.

![Econnews](https://i.postimg.cc/Yq52PJG8/Econnews.png)

## Funcionalidades

- **Endpoint Principal (`/`)**: Este endpoint retorna a página inicial da API, que apresenta informações sobre o projeto e um banner promocional.

- **Endpoint de Status (`/status`)**: Retorna um JSON indicando se o servidor Flask está em execução.

- **Endpoint UOL (`/uol`)**: Retorna notícias de economia obtidas do site UOL. As notícias são obtidas através de web scraping e fornecem títulos e links para artigos relevantes.

## Como usar

Para utilizar esta API, você pode acessar os endpoints mencionados acima através de um cliente HTTP ou navegador da web. Abaixo estão os passos básicos para começar:

1. Clone o repositório do projeto do GitHub:
   ```
   git clone https://github.com/IK-R-S/Econnews-API.git
   ```

2. Instale as dependências do projeto:
   ```
   pip install -r requirements.txt
   ```

3. Inicie o servidor Flask:
   ```
   python index.py
   ```

4. Acesse os endpoints da API conforme necessário:
   - Página inicial: [http://localhost:5000/](http://localhost:5000/)
   - Status do servidor: [http://localhost:5000/status](http://localhost:5000/status)
   - Notícias do UOL: [http://localhost:5000/uol](http://localhost:5000/uol)

## Contribuição

Este projeto é de código aberto e contribuições são bem-vindas. Se você deseja propor melhorias, corrigir bugs ou adicionar novos recursos, sinta-se à vontade para abrir um problema ou enviar uma solicitação de pull request para o repositório do GitHub.
