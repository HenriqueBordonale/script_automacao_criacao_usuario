import subprocess

nome = input ("Insira o nome do Colaborador/Docente: ").lower()
codigoFun = input ("Insira o codigo funcional: ")
userACopiar = input("Insira um usuário a copiar: ").lower()

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


confirmarUsuario = input(f"Deseja manter o usuário: {username}? [S/N]").lower()
if(confirmarUsuario == "n"):
    username = input("Insira o usuário desejado: ").lower()
    print(f"Usuário: {username}")

nomeCompleto = identificar_sobrenome(nome).split()
sobrenome = ' '.join(nomeCompleto[1:]) if len(nomeCompleto) > 1 else ''
email = username + "@unaerp.br"
print("-----------------------------")
print(f"Nome Completo: {nomeCompleto}")
print(f"Usuário: {username}")
print(f"Endereço de E-mail: {email}")
print(f"Código Funcional: {codigoFun}")
print(f"Usuário a copiar: {userACopiar}")
confirEmail = input("Deseja confirmar a criação? [S/N]").lower()


if (confirEmail == "s"):
    process = subprocess.run(
    ["powershell", "-File", "ChamarCriacao.ps1", "-OrigUser", userACopiar, "-NewUser", username,"-codigo", codigoFun, "-email", email, "-nome", nomeCompleto[0], "-sobrenome", sobrenome],
    capture_output=True,
    text=True
)

print("Resultado da execução:")
print(process.stdout)
print(process.stderr)

processPy = subprocess.run(["python",
        "D:\documents\Automacao_Email\Automatização_Email.py", username])