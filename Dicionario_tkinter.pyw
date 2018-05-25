from tkinter import *
from tkinter import ttk
import Janela_adicionar
from Dados_SQLite import Manipulacao_SQLite
from Janela_adicionar import Janela_Auxiliar
from Dados_Constantes import *
import Reproduzir_audio

class Dicionario():
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal

        self.design_estilos()
        self.frame_superior()
        self.frame_pesquisa_insercao()
        self.frame_lateral_vista()
        self.imagens()
        self.frame_lateral_descricao()
        ####Eventos
        #self.janela_principal.protocol("<Motion>", self.ocultar_mostrarframesuperior)


    def design_estilos(self):
        self.ftpesq = ("Calibri", 13, "bold")
        self.estilo_geral = ttk.Style()
        self.estilo_geral.configure("cor_frame.TFrame", background = "#BC8F8F")

    def frame_superior(self):
        """Metodo que trata da criação e empacotação do frame superior da janela, que
        contém os principais botões de informação e o botão de impressão"""
        #Criação do frame
        self.fr_superior = ttk.Frame(self.janela_principal, width = 600, height = 30, style = "cor_frame.TFrame")
        self.fr_superior.place(x = 3, y = 5)
        #Widgets empacotados no frame no superior, imprimir, sobre o software, sair do programa
        self.imprimir = ttk.Button(self.fr_superior, text = "impr").place(x = 20, y = 2)
        self.sobre = ttk.Button(self.fr_superior, text = "sobre").place(x = 100, y = 2)
        self.sair = ttk.Button(self.fr_superior, text = "sair").place(x = 180, y = 2)

    def frame_pesquisa_insercao(self):
        """Metodo que trata da inserção e pesquisa de palavras"""
        #Criação do frame
        self.fr_pesquisa_insercao = ttk.Frame(self.janela_principal, width = 180, height = 40, relief = GROOVE, style = "cor_frame.TFrame")
        self.fr_pesquisa_insercao.place(x = 3, y = 45)
        #Widgets empacotados no frame de pesquisa de palavra
        self.pesquisar = ttk.Entry(self.fr_pesquisa_insercao, font = self.ftpesq, width = 14)
        self.pesquisar.place(x = 5, y = 8)
        self.bt_ad = ttk.Button(self.fr_pesquisa_insercao, text = "ad", width = 4, state = desabilidado, command = self.adicionar_item)
        self.bt_ad.place(x = 140, y = 9)
        ##Eventos
        #Colocar foco no widgets de pesquisa e inserção de palavra
        self.pesquisar.focus_force()
        self.pesquisar.bind("<KeyRelease>", self.activar_btad)


    def frame_lateral_vista(self):
        """Metodo que trata da visualização das palavras cadastradas"""
        #Criação do frame lateral de visualização de palavras
        self.frame_lateral_palavras = ttk.Frame(self.janela_principal, width = 180, height = 400, style = "cor_frame.TFrame")
        self.frame_lateral_palavras.place(x = 3, y = 90)
        #Criação e empacotamento do treeview
        cabecalho = ['Palavras']
        self.lista_dadostreeviewact = list()
        objecto_gerado = Manipulacao_SQLite()
        objecto_gerado.selecionar_palavras()
        for item in objecto_gerado.lt_palavras:
            self.lista_dadostreeviewact.append(item)
        self.lista_dadostreeviewact.sort()
        #Criação da treeview propriamente dita
        self.treedataview_palavra = ttk.Treeview(columns=cabecalho, show="headings", height = 18)
        self.treedataview_palavra.place(x = 6, y = 97)
        for col in cabecalho:
            self.treedataview_palavra.heading(col, text=col)
            self.treedataview_palavra.column(col, anchor='center', width=170)
        for item in self.lista_dadostreeviewact:
            self.treedataview_palavra.insert('', 'end', values=item)
        ####Eventos
        #Evento chamado quando clicado em alguma palavra do treeview
        self.treedataview_palavra.bind('<ButtonRelease-1>', self.visualizar_palavra)

    def frame_lateral_descricao(self):
        """Metodo que trata da visualização e audição do significado das palavras já existentes"""
        self.fr_descricao = Frame(self.janela_principal, width = 550, height = 390, relief = GROOVE, bg = "#BC8F8F")
        self.fr_descricao.place(x = 250, y = 250)

        self.lb_palavra = ttk.Label(self.fr_descricao, text = "", background =  "#BC8F8F", font = ("Calibri", 20, "bold"))
        self.lb_palavra.place(x = 46, y = 9)

    def imagens(self):
        """Metodo que cuida da apresentação das imagens na janela"""
        self.imagem_referencial = PhotoImage(file = r"Imagens\Icone_referencial.png")
        ttk.Label(self.janela_principal, image = self.imagem_referencial, background = "white").place(x = 550, y = 60)



    def adicionar_item(self):
        self.bt_ad.config(state = desabilidado)
        janela_adicionar = Toplevel()
        palavra = self.pesquisar.get()
        self.pesquisar.delete(0, END)
        self.pesquisar.focus_force()
        objecto_gerado = Janela_Auxiliar(janela_adicionar, palavra)

    def visualizar_palavra(self, e):
        try:
            item = self.treedataview_palavra.selection()[0]
            id = self.treedataview_palavra.item(item)['values'][0]
            objecto_gerado = Manipulacao_SQLite()
            objecto_gerado.selecionar_palavras()
            significado = objecto_gerado.dict_palavrasign[id]
            self.lb_palavra["text"] = id
            self.ouvir = ttk.Button(self.fr_descricao, text = "ouvir")
            self.ouvir.place(x = 5, y = 70)
            self.ouvir["command"] = self.reproduzir_audio
            descricaotxt = Text(self.fr_descricao, width = 65, height = 15, wrap = "word", font = ("Calibri", 11, "bold"), relief = SOLID)
            descricaotxt.place(x = 46, y = 50)

            descricaotxt.insert(1.0, "\n     "+significado)
            descricaotxt.config(state = "disabled")
        except:
            pass

    def activar_btad(self, e):
        if len(self.pesquisar.get()) >= 1 and self.pesquisar.get().isalpha():
            self.bt_ad.config(state = normal)
        else:
            self.bt_ad.config(state = desabilidado)

    def reproduzir_audio(self):
        audio = r"Audio\Amar.wav"
        Reproduzir_audio.reproducao_audio(audio)
        #self.lb_palavra["text"]







            
dicionario_lembrete = Tk()
dicionario_lembrete.title("Dicionário de lembretes")
dicionario_lembrete.geometry("890x700+100+10")
dicionario_lembrete["bg"] = "white"
dicionario_instancia = Dicionario(dicionario_lembrete)
dicionario_lembrete.mainloop()
