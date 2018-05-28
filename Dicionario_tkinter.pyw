#Autor - Adriano António (Desenvolvedor python e artofpro center)
#Desenvolvido - 2018 - Email: adriano.antonio@outook.pt
#Titulo - Dicionário de lembretes, um principio de pymemory
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import Janela_adicionar
#import matplotlib.pyplot as plt
from Dados_SQLite import Manipulacao_SQLite
from Janela_adicionar import Janela_Auxiliar
from Dados_Constantes import *
import Reproduzir_audio
from Funcao_auxiliar import Strings


class Dicionario():
    def __init__(self, janela_principal):
        """Dicionário de lembretes, uma iniciativa da ArtOfProCenter (Adriano António) para projectos universitários em python tkinter"""
        self.janela_principal = janela_principal
        self.design_estilos()
        self.frame_superior()
        self.frame_pesquisa_insercao()
        self.frame_lateral_vista()
        self.imagens()
        self.frame_lateral_descricao()

    def design_estilos(self):
        """Metodo de definição de estilos e variáveis constantes"""
        self.ftpesq = ("Calibri", 13, "bold")
        self.estilo_geral = ttk.Style()
        self.estilo_geral.configure("cor_frame.TFrame", background = castanho)

    def frame_superior(self):
        """Metodo que trata da criação e empacotação do frame superior da janela, que
        contém os principais botões de informação e o botão de impressão"""
        #Criação do frame
        self.fr_superior = ttk.Frame(self.janela_principal, width = 600, height = 30, style = "cor_frame.TFrame")
        self.fr_superior.place(x = 3, y = 5)
        #Imagens
        self.icone_informacao = PhotoImage(file = r"Imagens\Icone_informacao.png")
        self.icone_imprimir = PhotoImage(file = r"Imagens\Icone_imprimir.png")
        #Widgets empacotados no frame no superior, imprimir, sobre o software, sair do programa
        #Imprimir
        self.fr_imprimir = Frame(self.fr_superior, width = 70, height = 20, relief = GROOVE, bg = branco)
        self.fr_imprimir.place(x = 20, y = 5)
        self.lb_imprimiricone = ttk.Label(self.fr_imprimir, image = self.icone_imprimir, background = branco)
        self.lb_imprimiricone.place(x = 25, y = 1)
        #Sobre
        self.fr_sobre = Frame(self.fr_superior, width = 70, height = 20, relief = GROOVE, bg = branco)
        self.fr_sobre.place(x = 110, y = 5)
        self.lb_sobreicone = ttk.Label(self.fr_sobre, image = self.icone_informacao, background = branco)
        self.lb_sobreicone.place(x = 25, y = 0)
        #Gráfico, desabilitado no momento
        self.fr_grafico = Frame(self.fr_superior, width = 70, height = 20, relief = GROOVE, bg = branco)
        #self.fr_grafico.place(x = 200, y = 5)
        #Eventos
        #entrar no frame de imprimir
        self.fr_imprimir.bind("<Enter>", self.entrar_frimprimir)
        #sair do frame de imprimir
        self.fr_imprimir.bind("<Leave>", self.sair_frimprimir)
        #entrar no frame de sobre
        self.fr_sobre.bind("<Enter>", self.entrar_frsobre)
        #sair do frame de sobre
        self.fr_sobre.bind("<Leave>", self.sair_frsobre)
        #clicar no frame de sobre
        self.fr_sobre.bind("<Button-1>", self.informacao)
        self.lb_sobreicone.bind("<Button-1>", self.informacao)
        #Entrar no frame gráfico
        self.fr_grafico.bind("<Enter>", self.entrar_frgrafico)
        #Sair do frame gráfico
        self.fr_grafico.bind("<Leave>", self.sair_frgrafico)
        #Clicar no frame gráfico
        self.fr_grafico.bind("<Button-1>", self.grafico)

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
        #Validar o botão de inserção de palavra
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
        self.treedataview_palavra.bind('<Return>', self.visualizar_palavra)

    def frame_lateral_descricao(self):
        """Metodo que trata da visualização e audição do significado das palavras já existentes"""
        self.fr_descricao = ttk.Frame(self.janela_principal, width = 550, height = 390, relief = GROOVE, style = "cor_frame.TFrame")
        self.fr_descricao.place(x = 250, y = 250)
        #Palavra que surge quando clicamos em alguma palavra do treeview
        self.lb_palavra = ttk.Label(self.fr_descricao, text = "", background =  castanho, font = ("Calibri", 20, "bold"))
        self.lb_palavra.place(x = 46, y = 9)
        #Tamanho da palavra e quantas vogais tem, que aparece por baixo
        self.lb_tamanho = ttk.Label(self.fr_descricao, text = "", background =  castanho)
        self.lb_tamanho.place(x = 380, y = 330)

    def imagens(self):
        """Metodo que cuida da apresentação das imagens na janela"""
        self.imagem_referencial = PhotoImage(file = r"Imagens\Icone_referencial.png")
        ttk.Label(self.janela_principal, image = self.imagem_referencial, background = branco).place(x = 550, y = 60)

    def adicionar_item(self):
        """Metodo que traz a janela auxiliar caso no acto de adição de palavra esteja tudo correcto"""
        try:
            self.bt_ad.config(state = desabilidado)
            janela_adicionar = Toplevel()
            palavra = self.pesquisar.get()
            self.pesquisar.delete(0, END)
            self.pesquisar.focus_force()
            objecto_gerado = Janela_Auxiliar(janela_adicionar, palavra)
        except:
            pass

    def visualizar_palavra(self, e):
        """Metodo de visualização e audição da palavra selecionada"""
        try:
            self.icone_som = PhotoImage(file = r"Imagens\Icone_som.png")
            item = self.treedataview_palavra.selection()[0]
            id = self.treedataview_palavra.item(item)['values'][0]
            objecto_gerado = Manipulacao_SQLite()
            objecto_gerado.selecionar_palavras()
            significado = objecto_gerado.dict_palavrasign[id]
            self.lb_palavra["text"] = id
            self.fr_som = Frame(self.fr_descricao, width = 42, height = 20, relief = GROOVE, bg = branco)
            self.fr_som.place(x = 2, y = 51)
            self.lb_somimage = ttk.Label(self.fr_som, image = self.icone_som, background = branco)
            self.lb_somimage.place(x = 12, y = 2)
            #Descrição, texto que aparece a palavra
            descricaotxt = Text(self.fr_descricao, width = 65, height = 15, wrap = "word", font = ("Calibri", 11, "bold"), relief = SOLID)
            descricaotxt.place(x = 46, y = 50)
            #Adicção e bloqueio de palavra no texto de descrição
            descricaotxt.insert(1.0, "\n     "+significado)
            descricaotxt.config(state = "disabled")
            #Tamanho e vogais
            objecto_string = Strings()
            objecto_string.comprimento_vogais(self.lb_palavra["text"])
            self.lb_tamanho["text"] = objecto_string.descricao
            #Eventos
            #entrar no frame de som
            self.fr_som.bind("<Enter>", self.entrar_frsom)
            #sair do frame de som
            self.fr_som.bind("<Leave>", self.sair_frsom)
            #clicar no frame de som
            self.fr_som.bind("<Button-1>", self.reproduzir_audio)
            self.lb_somimage.bind("<Button-1>", self.reproduzir_audio)
        except:
            pass

    def activar_btad(self, e):
        """Metodo de validação do botão de adicionar da caixa de pesquisa"""
        if len(self.pesquisar.get()) >= 1 and self.pesquisar.get().isalpha():
            self.bt_ad.config(state = normal)
        else:
            self.bt_ad.config(state = desabilidado)

    def reproduzir_audio(self, e):
        """Metodo para reprodução de aúdio"""
        try:
            audio = "Audio\\"+self.lb_palavra["text"]+".wav" #Caminho do aúdio de acordo a palavra
            Reproduzir_audio.reproducao_audio(audio) #Reprodução do aúdio através de arquivo externo
        except:
            pass

    def informacao(self, e):
        """Metodo que mostra a informação sobre o sistema"""
        tkinter.messagebox._show("PyMemory v.1", "Desenvolvedor: Adriano António\n"+r"Email: adriano.antonio@outlook.pt ou facebook.com\adriano5000"+"\nContacto: +244-922-961-983\n"+r"Git: github.com\adrianoantonio96", "info")

    def grafico(self, e):
        pass
        #plt.bar(["Equivalente", "Maria", "João", "António"], [1,2,8,14])
        #plt.title("Gráfico de palavras mais lidas")
        #plt.xlabel("Palavras")
        #plt.ylabel("Número de leitura")
        #plt.show()

    def entrar_frsom(self, e):
        """Metodo que entra no frame de som e coloca a cor marrom"""
        self.fr_som.config(bg = castanho)
        self.lb_somimage.config(background = castanho)

    def sair_frsom(self, e):
        """Metodo que sai do frame de som e coloca a cor branca padrão"""
        self.fr_som.config(bg = branco)
        self.lb_somimage.config(background = branco)

    def entrar_frimprimir(self, e):
        """Metodo que entra no frame de impressão e coloca a cor marrom"""
        self.fr_imprimir.config(bg = castanho)
        self.lb_imprimiricone.config(background = castanho)

    def sair_frimprimir(self, e):
        """Metodo que sai do frame de impressão coloca a cor branca padrão"""
        self.fr_imprimir.config(bg = branco)
        self.lb_imprimiricone.config(background = branco)

    def entrar_frsobre(self, e):
        """Metodo que entra no frame de sobre e coloca a cor marrom"""
        self.fr_sobre.config(bg = castanho)
        self.lb_sobreicone.config(background = castanho)

    def sair_frsobre(self, e):
        """Metodo que sai do frame de sobre coloca a cor branca padrão"""
        self.fr_sobre.config(bg = branco)
        self.lb_sobreicone.config(background = branco)

    def entrar_frgrafico(self, e):
        """Metodo que entra no frame de gráfico e coloca a cor marrom"""
        self.fr_grafico.config(bg = castanho)
        #self.lb_sobreicone.config(background = castanho)

    def sair_frgrafico(self, e):
        """Metodo que sai do frame de gráfico coloca a cor branca padrão"""
        self.fr_grafico.config(bg = branco)
        #self.lb_sobreicone.config(background = branco)

#Instanciação da classe principal
dicionario_lembrete = Tk()
dicionario_lembrete.title("Dicionário de lembretes")
dicionario_lembrete.iconbitmap(r"Imagens/icone_principal.ico")
dicionario_lembrete.geometry("890x700+100+10")
dicionario_lembrete["bg"] = "white"
dicionario_instancia = Dicionario(dicionario_lembrete)
dicionario_lembrete.mainloop()
