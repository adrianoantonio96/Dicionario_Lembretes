#DICIONÁRIO EM TKINTER
#ADRIANO ANTÓNIO - AUTOR


from tkinter import *
from tkinter import ttk
import Janela_adicionar

class dict_lembrete():
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        self.janela_principal.geometry("600x450")
        self.janela_principal.title("Dicionário de lembretes")
        self.janela_principal["bg"] = "white"

        self.design_estilos()
        self.frames_janela()
        self.widgets_todos()
        self.lista_palavras()

        janela_principal.mainloop()

    def frames_janela(self):
        self.fr_superior = ttk.Frame(self.janela_principal, width = 600, height = 25, style = "cor_frame.TFrame")
        self.fr_superior.place(x = 0, y = 0)


        self.fr_pesquisa = ttk.Frame(self.janela_principal, width = 180, height = 40, relief = GROOVE, style = "cor_frame.TFrame")
        self.fr_pesquisa.place(x = 0, y = 25)        

        self.fr_lateral = ttk.Frame(self.janela_principal, width = 180, height = 400, style = "cor_frame.TFrame")
        self.fr_lateral.place(x = 0, y = 66)



        self.fr_descricao = ttk.Frame(self.janela_principal, width = 415, height = 390, relief = GROOVE, style = "cor_frame.TFrame")
        self.fr_descricao.place(x = 181, y = 27)


    def design_estilos(self):
        self.ftpesq = ("Calibri", 13, "bold")
        self.estilo_geral = ttk.Style()
        self.estilo_geral.configure("cor_frame.TFrame", background = "#A9A9A9")



    def widgets_todos(self):
        self.imprimir = ttk.Button(self.fr_superior, text = "impr").place(x = 20, y = 2)
        self.sobre = ttk.Button(self.fr_superior, text = "sobre").place(x = 100, y = 2)
        self.sair = ttk.Button(self.fr_superior, text = "sair").place(x = 180, y = 2)

        self.pesquisar = ttk.Entry(self.fr_pesquisa, font = self.ftpesq, width = 14)
        self.pesquisar.place(x = 5, y = 8)
        self.pesquisar.bind("<KeyRelease>", self.pesquisar_item)
        self.ad = ttk.Button(self.fr_pesquisa, text = "ad", width = 4, command = self.adicionar_item)
        self.ad.place(x = 140, y = 9)

        self.descricaotxt = Text(self.fr_descricao, width = 58, height = 21, wrap = "word", font = ("Calibri", 11), relief = SOLID)
        self.descricaotxt.place(x = 2, y = 2)

        
    def adicionar_item(self):
        Janela_adicionar.janela_ad(self.pesquisar.get())
        print("Nada")

    def lista_palavras(self):
        self.lt_dados = []
        arquivo = open ("Arquivos//Palavras.txt", "r")
        self.lt_dados = arquivo.readlines()
        arquivo.close()
        
        scrollbar = Scrollbar(self.fr_lateral)
        scrollbar.place(x = 156, y = 7)

        self.listbox = Listbox(self.fr_lateral, width = 24, height = 21)
        self.listbox.place(x = 6, y = 7)

        for i in self.lt_dados:
            self.listbox.insert(END, i)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

    def pesquisar_item(self, e):
        self.lt_dadosother = []
        for a in range(len(self.lt_dados)):
            self.lt_dadosother.append(self.listbox.get(a))

        if self.pesquisar.get() in self.lt_dadosother:
            self.listbox.insert(0, self.pesquisar.get())
            
dicionario = Tk()
dict_lembrete(dicionario)
