# %%
# imports
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crud import CRUD
from relacoes import Livro

load_dotenv()

# %%
# Conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")
url = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

livro_crud = CRUD(Livro, session)


# %%
# testes
def test_read_as_dataframe():
    # TOD: Este teste deve ler os livros do banco de dados como um DataFrame
    # e verificar se o ISBN do primeiro livro no DataFrame é igual a "9788521630814".
    livros_df = livro_crud.read(as_dataframe=True)
    assert livros_df.shape[0] > 0
    assert livros_df['isbn'].iloc[0] == "9788521630814"


def test_read_as_list():
    # TOD: Este teste deve ler os livros do banco de dados como uma lista de objetos Livro
    # e verificar se o ISBN do primeiro livro retornado é igual a "9788521630814".
    livros_lista = livro_crud.read()
    assert len(livros_lista) > 0
    assert livros_lista[0].isbn == "9788521630814"


def test_create():
    # TOD: Este teste deve criar um novo livro no banco de dados com os dados fornecidos
    # e, em seguida, verificar se o livro foi realmente adicionado verificando seu ISBN.
    livro_crud.update(
        obj_id="9788521630814",
        titulo="Updated Test Book",
    )
    updated_livro = livro_crud.read(isbn="9788521630814")[0]
    assert updated_livro.titulo == "Updated Test Book"


def test_update():
    # TOD: Este teste deve atualizar o título do livro com ISBN "9788521630814"
    # para "Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações"
    # e, em seguida, verificar se a atualização foi bem-sucedida, confirmando que o título
    # do livro foi alterado.
    livro_crud.update(
        obj_id="9788521630814",
        titulo="Updated Test Book",
    )
    updated_livro = livro_crud.read(isbn="9788521630814")[0]
    assert updated_livro.titulo == "Updated Test Book"


def test_delete():
    # TOD: Este teste deve deletar do banco de dados o livro criado no test_create
    # e, em seguida, verificar se ele foi realmente removido, confirmando que não
    # existem mais livros com esse ISBN no banco.
    livro_crud.delete(obj_id="9788521630814")
    assert livro_crud.read(isbn="9788521630814") == "Registro não encontrado"
