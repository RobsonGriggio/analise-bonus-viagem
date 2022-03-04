import pandas as pd
from twilio.rest import Client

# Bibliotecas usadas:
# pandas
# twilio

# Your Account SID from twilio.com/console
account_sid = "AC16024604ffd3e2b5a6bf47cff3f5711c"
# Your Auth Token from twilio.com/console
auth_token  = "25327069b9ce112ca7807eb850f2c73b"

client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel

# Para cada arquivo:
# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"inputs/{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        message = client.messages.create(
        to="+5519994350641", 
        from_="+16516152328",
        body=f"No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        print("código da mensagem: ",message.sid)
