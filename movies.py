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


def generate_data_frame(xls):
    """
    Função que gera um pd.DataFrame contendo os dados da planilha
    de entrada.

    Parâmetros
    ----------
        xls : pd.ExcelFile
           Objeto que contêm a planilha a ser analisada.

    Retorna
    ------
        df: pd.DataFrame
          Objeto que contêm as informações relacionadas a entrada xls.

    Exemplo
    --------
    >>> xls = xls_verifier(save=False)
    >>> df = generate_data_frame(xls)
    """
    df_list = []
    for sheet_name in xls.sheet_names:
        df_list.append(pd.read_excel(xls, sheet_name=sheet_name))

    df = pd.concat(df_list)
    df.reset_index(drop=True, inplace=True)
    return df


def plot_data(x, y, df):
    """
    Função que plota os dados das colunas x e y.

    Parâmetros
    ----------
        x: str
            Coluna "x" a ser analisada.
        y: str
            Coluna "y" a ser analisada.
        df: pd.DataFrame
            Dataframe contendo as colunas a serem analisadas.
    Retorna
    ------
        None

    Exemplo
    --------
    >>> x = "Year"
    >>> y = "Duration"
    >>> xls = xls_verifier(save=False)
    >>> df = generate_data_frame(xls)
    >>> df.plot_data(x,y,df)
    """

    df_columns_list = list(df.columns)

    assert x in df_columns_list, f"Coluna {x} não existe."
    assert y in df_columns_list, f"Coluna {y} não existe."

    assert x in list(
        (df._get_numeric_data()).columns
    ), f"Coluna {x} não possui valores numéricos."

    assert y in list(
        (df._get_numeric_data()).columns
    ), f"Coluna {y} não possui valores numéricos."

    df_plot = pd.DataFrame({x: df[x], y: df[y]})
    df_plot.dropna(inplace=True)

    fig = df_plot.plot.scatter(x, y)
    fig.show()


xls = xls_verifier(save=True)
df = generate_data_frame(xls)
plot_data(x, y, df)
