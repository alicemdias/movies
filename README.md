# Análise para filmes
Esse repositório tem como objetivo gerar gráficos sobre dados de filmes.
## Instalação
Para utilizar o código, primeiramente crie um [ambiente virtual](https://docs.python.org/3/library/venv.html) e o ative.  

Se estiver utilizando o Windows:  

* Adicione o diretorio do python às [variáveis de ambiente do windows](https://medium.com/@victorromariopazdejesus/python-3-configurando-vari%C3%A1veis-de-ambiente-no-windows-10-63059c7192e6); 
* Para criar o venv, com o terminal dentro da pasta "movies", rode:  
    ```
    python -m venv venv
    ```
* Agora para ativar o venv, se estiver utilizando o PowerShell (o vscode geralmente tem como seu terminal o PowerShell), dentro da pasta "movies" rode o seguinte código:
    ```
    .\venv\Scripts\Activate.ps1
    ```

Para instalar as dependências, abra o prompt de comando e na pasta "movies" rode o seguinte código:
```
pip install -r requirements.txt
```  
## Utilização
Para utilizar o código e gerar o gráfico, dentro da pasta "movies" rode:
```
python movies.py arg1 arg2
```
Onde "arg1" e "arg2" são os argumentos desejados e são respectivamente os eixos x e y do gráfico.

Os seguintes argumentos podem ser dados como entrada para plotar o gráfico (devemos substituir espaços por underscores):

*  Year
*  Duration
*  Aspect_Ratio
*  Budget
*  Gross_Earnings
*  Facebook_Likes_-_Director
*  Facebook_Likes_-_Actor_1
*  Facebook_Likes_-_Actor_2
*  Facebook_Likes_-_Actor_3
*  Facebook_Likes_-_cast_Total
*  Facebook_likes_-_Movie
*  Facenumber_in_posters
*  User_Votes
*  Reviews_by_Users
*  Reviews_by_Crtiics
*  IMDB_Score
