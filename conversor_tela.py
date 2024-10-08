from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from chave_api import API_KEY
# Cores
cor0 = '#ffffff'  # branca
cor1 = '#000000'  # preta
cor2 = '#1251a0'  # azul
cor3 = '#62b468'  # verde

# Criando a janela
janela = Tk()
janela.geometry('400x400')
janela.title('Conversor de moedas')
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

# Divisão da janela
frame_de_cima = Frame(janela, width=400, height=75, bg=cor2, relief='flat')
frame_de_cima.grid(row=0, column=0, columnspan=2)

frame_de_baixo = Frame(janela, width=400, height=325, bg=cor0, relief='flat')
frame_de_baixo.grid(row=1, column=0, sticky=NSEW)

# Configuração do frame de cima
imagem = Image.open('imagens/imagem_dinheiro_branca.png')
imagem = ImageTk.PhotoImage(imagem)
nome_do_app = Label(frame_de_cima, image=imagem, compound=LEFT, text='Conversor de moedas', height=6, pady=31, padx=41,
                    relief='flat', anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
nome_do_app.place(x=0, y=0)

# Configuração do frame de baixo
resultado = Label(frame_de_baixo, text='', height=2, pady=10, width=20, relief='solid', anchor=CENTER,
                  font=('Montserrat 16 bold'), bg=cor0, fg=cor1)
resultado.place(x=70, y=15)

moedas = ['USD', 'EUR', 'BRL']

campo_de = Label(frame_de_baixo, text='De', relief='flat', anchor=NW, font=('Arial 12 bold'), bg=cor0, fg=cor1)
campo_de.place(x=70, y=110)
combo_de = ttk.Combobox(frame_de_baixo, width=11, justify=CENTER, font=('Montserrat 12 bold'))
combo_de.place(x=74, y=140)
combo_de['values'] = moedas

campo_para = Label(frame_de_baixo, text='Para', relief='flat', anchor=NW, font=('Arial 12 bold'), bg=cor0, fg=cor1)
campo_para.place(x=210, y=110)
combo_para = ttk.Combobox(frame_de_baixo, width=11, justify=CENTER, font=('Montserrat 12 bold'))
combo_para.place(x=214, y=140)
combo_para['values'] = moedas

# Função para converter a moeda
def converter():
    try:
        moeda_de = combo_de.get()
        moeda_para = combo_para.get()
        valor_converter = float(valor.get().replace(',', '.'))

        # Faz a requisição com base sempre em USD
        resposta = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={API_KEY}')
        dados = json.loads(resposta.text)

        # Se a moeda_de não for USD, converte de moeda_de para USD
        if moeda_de != 'USD':
            valor_em_usd = valor_converter / dados['rates'][moeda_de]
        else:
            valor_em_usd = valor_converter

        # Converte de USD para a moeda_para
        valor_equivalente = valor_em_usd * dados['rates'][moeda_para]

        # Formatação dos valores convertidos
        if moeda_para == 'USD':
            simbolo = '$'
            valor_equivalente_formatado = simbolo + f'{valor_equivalente:,.2f}'
        elif moeda_para == 'EUR':
            simbolo = '€'
            valor_equivalente_formatado = simbolo + f'{valor_equivalente:,.2f}'
        elif moeda_para == 'BRL':
            simbolo = 'R$'
            # Formatação especial para Real
            valor_equivalente_formatado = simbolo + f'{valor_equivalente:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        else:
            simbolo = ''
            valor_equivalente_formatado = simbolo + f'{valor_equivalente:,.2f}'

        resultado['text'] = valor_equivalente_formatado

    except Exception as e:
        resultado['text'] = "Erro ao converter"
        
# Função para obter dados históricos e plotar o gráfico
def plot_historical_rates():
    try:
        moeda_de = combo_de.get()
        moeda_para = combo_para.get()

        historical_rates = {}
        
        for i in range(7):
            date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')

            # Obtém as taxas com base no USD
            resposta = requests.get(f'https://openexchangerates.org/api/historical/{date}.json?app_id={API_KEY}')
            dados = json.loads(resposta.text)

            # Calcula a taxa de câmbio indireta para moeda_de e moeda_para
            if moeda_de != 'USD' and moeda_para != 'USD':
                if moeda_de in dados['rates'] and moeda_para in dados['rates']:
                    taxa_indireta = dados['rates'][moeda_para] / dados['rates'][moeda_de]
                    historical_rates[date] = taxa_indireta
            elif moeda_de == 'USD':
                # Direto de USD para a moeda_para
                historical_rates[date] = dados['rates'][moeda_para]
            elif moeda_para == 'USD':
                # Direto da moeda_de para USD
                historical_rates[date] = 1 / dados['rates'][moeda_de]

        # Verifica se obteve dados para os últimos 7 dias
        if len(historical_rates) == 0:
            resultado['text'] = "Erro: Sem dados para gerar o gráfico."
            return

        # Gera o gráfico
        dates = sorted(historical_rates.keys())
        rates = [historical_rates[date] for date in dates]

        plt.figure(figsize=(8, 4))
        plt.plot(dates, rates, marker='o')
        plt.title(f'Taxa de Câmbio nos Últimos 7 Dias: {moeda_de} para {moeda_para}')
        plt.xlabel('Data')
        plt.ylabel(f'Taxa {moeda_de} para {moeda_para}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        resultado['text'] = "Erro ao gerar gráfico"


# Campo de entrada do valor
valor = Entry(frame_de_baixo, width=29, relief='solid', justify=CENTER, font=('Montserrat 12 bold'), bg=cor0, fg=cor1)
valor.place(x=70, y=190, height=30)

# Botão para converter
bnt_converter = Button(frame_de_baixo, command=converter, text='Converter', relief='raised', overrelief='raised', width=11,
                       padx=5, height=1, font=('Arial 12 bold'), bg=cor2, fg=cor0, activebackground=cor2, activeforeground=cor0)
bnt_converter.place(x=70, y=250)

# Botão para gerar gráfico
bnt_grafico = Button(frame_de_baixo, command=plot_historical_rates, text='Gráfico', relief='raised', overrelief='raised', width=11,
                     padx=5, height=1, font=('Arial 12 bold'), bg=cor2, fg=cor0, activebackground=cor2, activeforeground=cor0)
bnt_grafico.place(x=210, y=250)

# Inicializando a janela
janela.mainloop()
