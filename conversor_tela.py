from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageOps,ImageDraw

cor0 = '#ffffff' #branca
cor1 = '#000000' #preta
cor2 = '#1251a0' #azul
cor3 = '#62b468' #verde

# Criando a janela
janela = Tk()
janela.geometry('400x400')
janela.title('Conversor de moedas')
janela.configure(bg=cor0)
janela.resizable(width=FALSE,height=FALSE)

style = ttk.Style(janela)  #O objeto Style permite personalizar e modificar o estilo visual dos widgets ttk (como ttk.Button, ttk.Label, etc.).
style.theme_use('clam')

#Divisão da janela
frame_de_cima = Frame(janela,width=400,height=75,bg=cor2,relief='flat')
frame_de_cima.grid(row=0,column=0,columnspan=2)

frame_de_baixo = Frame(janela,width=400,height=325,bg=cor0,relief='flat')
frame_de_baixo.grid(row=1,column=0,sticky=NSEW) #o widget vai se alinhar aos quatro lados da célula da grade

#Configuração do frame de cima
imagem= Image.open('imagens/imagem_dinheiro_branca.png')
imagem= ImageTk.PhotoImage(imagem) # Convertendo a imagem para um formato que o Tkinter pode usar
nome_do_app = Label(frame_de_cima,image=imagem,compound=LEFT,text='Conversor de moedas',height=6,pady=31,padx= 41,relief='flat',anchor=CENTER,font=('Arial 16 bold'),bg=cor2,fg=cor0)
nome_do_app.place(x=0,y=0)


janela.mainloop()
#temas = style.theme_names()

