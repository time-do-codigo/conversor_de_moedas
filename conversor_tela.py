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

#Configuração do frame de baixo
resultado = Label(frame_de_baixo,text='',height=2,pady=10,width=26,relief='solid',anchor=CENTER,font=('Montserrat 12 bold'),bg=cor0,fg=cor1)
resultado.place(x=70,y=15)

moedas= ['USD','EUR','BRL']

campo_de =  Label(frame_de_baixo,text='De',relief='flat',anchor=NW,font=('Arial 12 bold'),bg=cor0,fg=cor1)
campo_de.place(x=70,y=110)
combo_de=ttk.Combobox(frame_de_baixo,width=11,justify=CENTER,font=('Montserrat 12 bold'))
combo_de.place(x=74,y=140)
combo_de['values'] = (moedas)

campo_para =  Label(frame_de_baixo,text='Para',relief='flat',anchor=NW,font=('Arial 12 bold'),bg=cor0,fg=cor1)
campo_para.place(x=210,y=110)
combo_para =ttk.Combobox(frame_de_baixo,width=11,justify=CENTER,font=('Montserrat 12 bold'))
combo_para.place(x=214,y=140)
combo_para['values'] = (moedas)

valor= Entry(frame_de_baixo,width=29,relief='solid',justify=CENTER,font=('Montserrat 12 bold'),bg=cor0,fg=cor1)
valor.place(x=70,y=190,height=30)

bnt_converter = Button(frame_de_baixo,command= '',text='Converter',relief='raised',overrelief='raised',width=11,padx=5,height=1,font=('Arial 12 bold'),bg=cor2,fg=cor0,activebackground=cor2,activeforeground=cor0)
bnt_converter.place(x=70,y=250)

bnt_grafico = Button(frame_de_baixo,command= '',text='Gráfico',relief='raised',overrelief='raised',width=11,padx=5,height=1,font=('Arial 12 bold'),bg=cor2,fg=cor0,activebackground=cor2,activeforeground=cor0)
bnt_grafico.place(x=210,y=250)

janela.mainloop()

#temas = style.theme_names()

