#Modulo que faz adição de palavras novas
from tkinter import *
from tkinter import ttk
from Dados_SQLite import Manipulacao_SQLite
from Dados_Constantes import *
import Gravar_audio

class Janela_Auxiliar(object):
    def __init__(self, janela_adicionar, palavra):
        self.janela_adicionar = janela_adicionar
        self.janela_adicionar.geometry("340x320")
        self.janela_adicionar.title("Adicionar palavra")
        self.janela_adicionar["bg"] = castanho
        self.palavra = palavra

        self.widgets()


    def widgets(self):
        self.lb_palavra = ttk.Label(self.janela_adicionar, text = self.palavra.title(), font = ("Calibre", 14, "bold"), background = castanho)
        self.lb_palavra.place(x = 30, y = 10)

        self.botaosom = ttk.Button(self.janela_adicionar, text = "Som", command = self.gravar_audio)
        self.botaosom.place(x = 255, y = 13)

        self.descricaotxt = Text(self.janela_adicionar, width = 45, height = 13, wrap = "word", font = ("Calibri", 11), relief = SOLID)
        self.descricaotxt.place(x = 10, y = 45)

        self.botaoadd = ttk.Button(self.janela_adicionar, text = "adicionar", state = desabilidado, command = self.inserir_palavra)
        self.botaoadd.place(x = 255, y = 286)
        self.descricaotxt.focus_force()
        self.descricaotxt.bind('<KeyRelease>', self.activar_btadicionar)
        self.janela_adicionar.mainloop()

    def inserir_palavra(self):
        try:
            palavra = self.lb_palavra["text"]
            significado = self.descricaotxt.get('1.0', END)
            objecto_gerado = Manipulacao_SQLite()
            objecto_gerado.inserir_mesa(palavra, significado)
            self.janela_adicionar.destroy()
        except:
            pass

    def gravar_audio(self):
        dado = "Audio\\"+self.lb_palavra["text"]
        Gravar_audio.audio_gravar(dado)

    def activar_btadicionar(self, e):
        if len(self.descricaotxt.get('1.0', END)) >= 3:
            self.botaoadd.config(state = normal)
        else:
            self.botaoadd.config(state = desabilidado)


# def info(e):
#     global fr_info
#     fr_info = Frame(jn_ad, relief = SOLID, width = 30, height = 20, background = "yellow")
#     fr_info.place(x = 265, y = 40)
#     Label(fr_info, text = "6seg").place(x = 0, y = 0)
# def sair_info(e):
#     fr_info.place_forget()

    #botaosom.bind("<Enter>", info)
   # botaosom.bind("<Leave>", sair_info)
