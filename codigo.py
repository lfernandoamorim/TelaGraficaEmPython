#importa o requests
import requests

#importa o pacote tkinter com tudo que tem nele
from tkinter import *

#cria funcção
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}    
    '''

    print(texto)

pegar_cotacoes()

#INICIAL - Criando a janela
janela = Tk()

#Configura a janela
janela.title("Cotação Atual das Moedas")


#FINAL - Não deixa fechar a janela
janela.mainloop()