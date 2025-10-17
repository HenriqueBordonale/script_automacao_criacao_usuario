import testeUsuario
from rich import print
from rich.console import Console
console = Console()

def criaNomeUsuario(nome):
    
    print("Script de criação de nome iniciado...")
    nomeSeparado = nome.strip().split() #Tira espaço em branco e divide o nome em string
    primeiroNome = nomeSeparado[0]
    ultimoNome = nomeSeparado[-1]
    username = primeiroNome[0] + ultimoNome
    i=0
    y=0
    letrasExtra = ""
    letrasAdicionais = "" 
    
    while True: #Estrutura de repetição para recriar usuário
      reescreverUser = testeUsuario.buscaUserAD(username)
      if reescreverUser.returncode == 0:
            if len(nomeSeparado) < 3 and i < len(primeiroNome) - 1:
                i+=1
                letrasExtra += primeiroNome[i]
                username = primeiroNome[0] + letrasExtra + ultimoNome
            elif len(nomeSeparado) >= 3 and y + 1 < len(nomeSeparado) - 1:
                y += 1
                letrasAdicionais += nomeSeparado[y][0]
                username = primeiroNome[0] + letrasAdicionais + ultimoNome    
            else:
                username = input("Não foi possivel criar o usuário, escreva da forma desejada: ").lower()
                console.print(f"Usuário: [bold green]{username}[/]")
                break
      else:     
            console.print(f"Usuário: [bold green]{username}[/]")
            break
    return username