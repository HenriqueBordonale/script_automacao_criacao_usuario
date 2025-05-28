nome = input ("Insira o nome do Colaborador/Docente: ").lower()
codigoFun = input ("Insira o codigo funcional: ")
userACopiar = input("Insira um usuário a copiar: ")

nomeSeparado = nome.strip().split()
primeiroNome = nomeSeparado[0]
ultimoNome = nomeSeparado[-1]
username = primeiroNome[0] + ultimoNome
repetirUsername = "s"
i=0
y=0
letrasExtra = ""
letrasAdicionais = "" 
while repetirUsername != "n":
    print(f"Sugestão de nome de usuário: {username}")
    repetirUsername = input("Deseja recriar o usuário: [S/N]").lower()

    if(repetirUsername == 's'):
        if len(nomeSeparado) < 3:
            i+=1
            letrasExtra += primeiroNome[i]
            username = primeiroNome[0] + letrasExtra + ultimoNome
        else:
            y += 1
            letrasAdicionais += nomeSeparado[y][0]
            username = primeiroNome[0] + letrasAdicionais + ultimoNome
  
    else:
        break

def identificar_sobrenome(nomeInput):
    nome_separado = nomeInput.strip().split()
    for i in range(len(nome_separado)):
        nome_separado[i] = nome_separado[i][0].upper() + nome_separado[i][1:].lower()
    return ' '.join(nome_separado)


confirmarUsuario = input(f"Deseja manter o usuário: {username}? [S/N]")
if(confirmarUsuario == "n"):
    username = input("Insira o usuário desejado: ")

nomeCompleto = identificar_sobrenome(nome)
email = username + "@unaerp.br"
print("-----------------------------")
print(f"Nome Completo: {nomeCompleto}")
print(f"Usuário: {username}")
print(f"Endereço de E-mail: {email}")
print(f"Código Funcional: {codigoFun}")
print(f"Usuário a copiar: {userACopiar}")
input("Deseja confirmar a criação? [S/N]")


