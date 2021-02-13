import pandas as pd
import requests
import sys
from pathlib import Path

pd.options.plotting.backend = "plotly"

x = sys.argv[1].replace('_',' ')
y = sys.argv[2].replace('_',' ')


def xls_verifier(save=True):
    """
    Função que verifica se a planilha está no diretório de trabalho.
    Se não estiver,a função da a opção de baixar a planilha e retorna a
    classe ExcelFile do pandas.

    Parâmetros
    ----------
        save : bool
            Variável booleana que indica se o arquivo será baixado no
            diretório de trabalho ou não (não substituindo um possível
            arquivo 'movies.xls' que possa existir dentro).

    Retorna
    -------
        xls: pd.ExcelFile
            Objeto pd.ExcelFile contendo a planilha.

    Exemplo
    --------
    >>> xls = xls_verifier(save=True)
    """

    cwd = Path(".")
    url = "https://dq-blog-files.s3.amazonaws.com/movies.xls"

    if save == True:
        if cwd / "movies.xls" not in cwd.glob("*.xls"):
            r = requests.get(url, allow_redirects=True)
            with open("movies.xls", "wb") as f:
                f.write(r.content)

        xls = pd.ExcelFile(cwd / "movies.xls")
    else:
        r = requests.get(url, allow_redirects=True)
        xls = pd.ExcelFile(r.content)
    return xls
    

xls = xls_verifier(save=True)
