#Modulo que faz adição de palavras novas
from tkinter import *
from tkinter import ttk
from Dados_SQLite import Manipulacao_SQLite
from Dados_Constantes import *
import Gravar_audio

class Janela_Auxiliar(object):
    def __init__(self, janela_adicionar, palavra):
        """Classe auxiliar e principal para adição de uma nova palavra no dicionário, com aúdio e significado"""
        self.janela_adicionar = janela_adicionar
        self.janela_adicionar.geometry("340x320")
        self.janela_adicionar.title("Adicionar palavra")
        self.janela_adicionar.iconbitmap(r"Imagens/icone_principal.ico")
        self.janela_adicionar["bg"] = castanho
        self.palavra = palavra #o atributo palavra já faz parte da classe em questão
        self.widgets()

    def widgets(self):
        """Metodo de criação e instanciação de widgets na janela"""
        self.lb_palavra = ttk.Label(self.janela_adicionar, text = self.palavra.title(), font = ("Calibre", 14, "bold"), background = castanho)
        self.lb_palavra.place(x = 30, y = 10)
        #Botão de som
        self.botaosom = ttk.Button(self.janela_adicionar, text = "Som", command = self.gravar_audio)
        self.botaosom.place(x = 255, y = 13)
        #Widget de inserção de significado
        self.descricaotxt = Text(self.janela_adicionar, width = 45, height = 13, wrap = "word", font = ("Calibri", 11), relief = SOLID)
        self.descricaotxt.place(x = 10, y = 45)
        #Botão de adicionar
        self.botaoadd = ttk.Button(self.janela_adicionar, text = "adicionar", state = desabilidado, command = self.inserir_palavra)
        self.botaoadd.place(x = 255, y = 286)
        ###Eventos
        #Colocar o foco da janela da caixa de inserção de significados
        self.descricaotxt.focus_force()
        #Activação do botão de adicionar caso esteja o significado seja inserido
        self.descricaotxt.bind('<KeyRelease>', self.activar_btadicionar)
        #Frame de informação de tempo quando se aproxima do frame de som
        self.botaosom.bind("<Enter>", self.info)
        self.botaosom.bind("<Leave>", self.sair_info)
        #Loop da janela
        self.janela_adicionar.mainloop()

    def inserir_palavra(self):
        """Metodo de insserção de palavra no data base com significado"""
        try:
            palavra = self.lb_palavra["text"]
            significado = self.descricaotxt.get('1.0', END)
            objecto_gerado = Manipulacao_SQLite()
            objecto_gerado.inserir_mesa(palavra, significado)
            self.janela_adicionar.destroy()
        except:
            pass

    def gravar_audio(self):
        """Metodo de gravação de aúdio na pasta Aúdio do sistema"""
        dado = "Audio\\"+self.lb_palavra["text"]
        Gravar_audio.audio_gravar(dado)

    def activar_btadicionar(self, e):
        """Validação do botão de adicionar"""
        if len(self.descricaotxt.get('1.0', END)) >= 3:
            self.botaoadd.config(state = normal)
        else:
            self.botaoadd.config(state = desabilidado)


    def info(self, e):
        """Metodo que informa ao utilizador quanto tempo de gravação tem quando se aproxima do frame de som"""
        self.fr_info = Frame(self.janela_adicionar, relief = SOLID, width = 30, height = 20, background = castanho)
        self.fr_info.place(x = 265, y = 40)
        ttk.Label(self.fr_info, text = "6seg", background = castanho).place(x = 0, y = 0)

    def sair_info(self, e):
        """Saída do frame de som"""
        self.fr_info.place_forget()

