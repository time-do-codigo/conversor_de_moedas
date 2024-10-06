from chave_api import API_KEY
import requests
import json

# função converter -----------------------

def converter():
	moeda_de = combo_de.get()
	moeda_para = combo_para.get()
	valor_converter = valor.get()

	resposta =  requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{moeda_de}/{moeda_para}')
	dados = json.loads(resposta.text)
	cambio = dados['conversion_rate']
	resultado = float(valor_converter) * float(cambio)

	if moeda_de == 'USD':
		simbolo = '$'
	elif moeda_para == 'EUR':
		simbolo = '€'
	else:
		simbolo = 'R$'
	
	valor_equivalente = simbolo + f'{resultado:,.2f}'
 
	resultado['text'] = valor_equivalente

	