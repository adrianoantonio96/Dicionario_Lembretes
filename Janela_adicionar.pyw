#Modulo que faz adição de palavras novas
from tkinter import *
from tkinter import ttk


def info(e):
    global fr_info
    fr_info = Frame(jn_ad, relief = SOLID, width = 30, height = 20, background = "yellow")
    fr_info.place(x = 265, y = 40)
    Label(fr_info, text = "6seg").place(x = 0, y = 0)    
def sair_info(e):
    fr_info.place_forget()

def add():
    arquivo = open ("Arquivos//Palavras.txt", "a")
    arquivo.write(copy_palavra+"\n")
    arquivo.close()


def janela_ad(palavra):
    
    global copy_palavra
    copy_palavra = palavra
    global jn_ad
    
    jn_ad = Tk()

    jn_ad.geometry("340x320")
    jn_ad.title("Adicionar palavra")
    jn_ad["bg"] = "white"

    
    ttk.Label(jn_ad, text = palavra.title(), font = ("Calibre", 14, "bold"), background = "white").place(x = 30, y = 10)


    botaosom = ttk.Button(jn_ad, text = "Som")
    botaosom.place(x = 255, y = 13)
    botaosom.bind("<Enter>", info)
    botaosom.bind("<Leave>", sair_info)

    descricaotxt = Text(jn_ad, width = 45, height = 13, wrap = "word", font = ("Calibri", 11), relief = SOLID)
    descricaotxt.place(x = 10, y = 45)

    botaoadd = ttk.Button(jn_ad, text = "adicionar", command = add).place(x = 255, y = 286)





    jn_ad.mainloop()
