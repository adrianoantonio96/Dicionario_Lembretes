class Strings(object):
    def __init__(self):
        """Classe de funções auxiliares, todas as funções auxiliares cá estarão excepto as de SQLite"""
        self.descricao = str()

    def comprimento_vogais(self, palavra):
        """Metodo que conta a palavra e quantas vogais tem"""
        tamanho = len(palavra)
        a = palavra.count("a")#count("a") - contar quantas vezes aparece o a na palavra
        A = palavra.count("A")
        e = palavra.count("e")
        i = palavra.count("i")
        o = palavra.count("o")
        u = palavra.count("u")
        vogais = a + e + i + o + u + A
        self.descricao = "Tamanho: "+str(tamanho)+", vogais: "+str(vogais)


