import win32com.client as win32

#integração com o outlook
outlook = win32.Dispatch('outlook.application')

#criar um email
email = outlook.CreateItem(0)

faturamento = 1500
qtde_produtos = 10
ticket_medio = faturamento/qtde_produtos

#configurar as informações do email
email.To = 'email1; email2' #destino
email.Subject = 'email automatico do python' #assunto
email.HTMLBody = f"""
<p>Olá Fulano, aqui é o código Python!</p>

<p>O faturamento da loja foi de {faturamento}. Vendemos {qtde_produtos} produtos. 
O ticket médio foi de {ticket_medio}</p>

<p>Att.</p>
<p>Eu</p>
"""" " #corpo do email

#anexar
anexo = 'C://Users/glock/OneDrive/Área de Trabalho/projetosPython/nome_arquivo.xlsx' # Caminho anexo
email.Attachments.Add(anexo)
#enviando email

email.Send()
print('Email enviado')