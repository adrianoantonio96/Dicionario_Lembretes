class Strings(object):
    def __init__(self):
        self.descricao = str()

    def comprimento_vogais(self, palavra):
        tamanho = len(palavra)
        a = palavra.count("a")
        A = palavra.count("A")
        e = palavra.count("e")
        i = palavra.count("i")
        o = palavra.count("o")
        u = palavra.count("u")
        vogais = a + e + i + o + u + A
        self.descricao = "Tamanho: "+str(tamanho)+", vogais: "+str(vogais)


