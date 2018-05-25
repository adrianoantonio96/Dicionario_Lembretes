from sqlite3 import *
class Manipulacao_SQLite(object):
    def __init__(self):
        """Classe de manipulação de dados do banco de dados"""
        self.inicio_sqlite()

    def inicio_sqlite(self):
        """Metodo que trata da inicialização da base de dados"""
        try:
            self.conectar = connect("Dict.db")
            self.conectado = self.conectar.cursor()
        except:
            pass

    def inserir_mesa(self, palavra, significado):
            self.conectado.execute("""INSERT INTO Palavras(
            Palavra,
            Significado) VALUES (?, ?)""", (palavra, significado))
            self.conectar.commit()

    def selecionar_palavras(self):
        """Metodo que seleciona todas as palavras e significados e coloca-os numa lista e dicionário"""
        self.lt_palavras = list()
        self.dict_palavrasign = dict()
        termo_pesquisa = """SELECT * FROM Palavras"""
        for item in self.conectado.execute(termo_pesquisa, ):
            self.lt_palavras.append(item[0])
            self.dict_palavrasign[item[0]] = item[1]

        #print(list(self.dict_palavrasign))


            #self.lt_palavras.append(list(item))
        #print(self.lt_palavras)

objecto = Manipulacao_SQLite()
objecto.selecionar_palavras()