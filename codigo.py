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

    conteudo["text"] = texto


#INICIAL - Criando a janela
janela = Tk()

#Configura a janela
#Define o título da janela
janela.title("Cotação Atual das Moedas")
#define o tanho da janela
janela.geometry("400x400")

#texto a ser exibido
texto = Label(janela, text="Clique no botão para ver as cotações")
texto.grid(column=0, row=0, padx=10, pady=10)
#Botão a ser exibido
btn = Button(janela, text="Buscar cotações de Dóllar/Euro/BTC", command=pegar_cotacoes)
btn.grid(column=0,row=1,padx=10, pady=10)
#conteúdo dinamico 
conteudo = Label(janela,text="")
conteudo.grid(column=0, row=2,padx=10, pady=10)

#FINAL - Não deixa fechar a janela
janela.mainloop()