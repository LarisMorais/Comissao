
 # Teste comissao

 # abrir os 6 arquivos em excel para cada arquivo:
 # verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000
 # se for maior que 55000 -> envia um SMS com o nome, o mês e as vendas do vendedor
 # caso nao seja maior do que 55000 -> nao fazer nada

 #obs.
 #pandas e openpyxl (excel)
 #twilio - (sms)

import pandas as pd
from twilio.rest import Client

account_sid = 'ACb7c159b02a352a94465b42cd922ba148'
auth_token = 'fc6a5cf29fec4a1d4e0d499069b76bff'
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'] #todos os meses que serão analisados

for mes in lista_meses:  #para cada mês dentro da lista, irá executar o codigo abaixo
  #print(mes)
  tabela_vendas = pd.read_excel(f'/content/drive/MyDrive/Colab Notebooks/DADOS/{mes}.xlsx') #o 'f' significa que o texto será formatado, assim passando o mês em cada arquivo.
  #print(tabela_vendas)
  if (tabela_vendas['Vendas'] > 55000).any():  #se na coluna vendas tiver algum(any:qualquer um) valor acima de 55000
      vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0] #vai pegar o nome do vendedor alocado na linha onde o valor é maior que 55000. o values[0] retorna apenas o valor, e nao a tabela.
      venda = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0] #mesma coisa acima para o valor da venda
      #print(f'No mês de {mes}, o(a) {vendedor} bateu a meta, com uma venda de {venda}!') #pegando os valores acima e alocando no print. necessário o 'f' para formatar o texto.
      message = client.messages.create(
                              body=f'No mês de {mes}, o(a) {vendedor} bateu a meta, com uma venda de {venda}!',
                              from_='+16204136366',
                              to='+(+55 (ddd)+inserir numero a ser enviado sms)')
      print(message.sid)

