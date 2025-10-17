import subprocess
import os
import sys
from rich import print
from rich.console import Console
from rich.align import Align
from rich.table import Table
import unicodedata
import criacaoUsername
import re

gam_path = r"...\GAM\gam.exe"  # caminho completo do GAM

def reiniciarScript(nome, usuario, email, senha,): #Script para reiniciar o sistema
        reloadScript= None
        console.clear()
        userAd = buscaUserAD(usuario)
        if(userAd.returncode == 0):
            table = Table(show_header=True, header_style="bold yellow")
            table.add_column("Nome Completo: ")
            table.add_column("Usuário: ")
            table.add_column("Endereço de E-mail: ")
            table.add_column("Senha:")
            table.add_row(
            " ".join(nome) if isinstance(nome, list) else str(nome),
            " ".join(usuario) if isinstance(usuario, list) else str(usuario),
            " ".join(email) if isinstance(email, list) else str(email),
            " ".join(senha) if isinstance(senha, list) else str(senha),
        )
            console.print(f"[green]Usuário [bold]{usuario} criado com sucesso![/]")
            console.print(table)
            
        while reloadScript not in ['s', 'n']:
            reloadScript = console.input("Deseja criar outro usuário? [bold yellow][S/N][/] ").lower()
            if reloadScript == "s":
                main()
            elif reloadScript =='n':
                console.input("[bold magenta]Script Encerrado! Pressione qualquer tecla para sair...[/]")
                sys.exit()
            else:
                console.print("[bold red]Digite um valor válido![/]")
                
def buscaUserAD(aluno: str):
    chamadaPowerShell = (
        r"Import-Module ActiveDirectory; "
        + f"if (Get-ADUser -Filter \"(sAMAccountName -eq '{aluno}') -or (UserPrincipalName -eq '{aluno}')\" -ErrorAction SilentlyContinue) "
        + "{ exit 0 } else { exit 1 }"
    )
    processAD = subprocess.run(
        ["powershell", "-NoProfile", "-Command", chamadaPowerShell],
        capture_output=True, 
        text=True)
    return processAD

def remover_acento(texto):
    texto_recebido = unicodedata.normalize('NFKD', texto)
    texto_recebido.encode('ascii', 'ignore').decode('utf-8')
    texto_recebido = re.sub(r'[^a-zA-Z0-9\s]', '', texto_recebido)
    return texto_recebido

def identificar_sobrenome(nomeInput):
    nome_separado = nomeInput.strip().split()
    for i in range(len(nome_separado)):
        nome_separado[i] = nome_separado[i][0].upper() + nome_separado[i][1:].lower()
    return ' '.join(nome_separado)

console = Console()
def main():
        os.system('cls')
        console.clear()
        console.print(Align("-------------Criação de usuário [bold yellow]UNAERP[/]-------------", align="center"))
        nome = console.input ("Insira o [bold yellow]NOME[/] do Colaborador/Docente: ").lower()
        nome = remover_acento(nome)
        codigoFun = console.input ("Insira o [bold yellow]CÓDIGO[/] funcional: ")
        while True:
            userACopiar = console.input("Insira um [bold yellow]USUÁRIO[/] a [bold yellow]COPIAR:[/] ").lower()
            try:
                UserAd = buscaUserAD(userACopiar)
                if UserAd.returncode == 0:
                    break
                elif UserAd.returncode == 1:
                    console.print("[bold red]Usuário cópia não existente, insira um usuário existente![/]")
                    
            except Exception as e:
                print(f"Erro interno de pesquisa: {e}. Tente novamente ou insira outro usuário.")
                    
                
        console.print("-----------------------------", style="bold red")
        
        username = criacaoUsername.criaNomeUsuario(nome) #Chamar função para criar Username
        recriarUser = None
        while recriarUser not in ['s','n']:
            recriarUser = console.input("Deseja recriar o [bold yellow]username[/]? [S/N]").lower()
            try:
                if recriarUser not in ['s', 'n']:
                    console.print("[bold red]Escolha uma alternativa válida![/]")
            except ValueError:
                console.print("[bold red]Escolha uma alternativa válida![/]")
                
        if (recriarUser == 's'):
         username = console.input("Digite o novo [bold yellow]username[/]: ")
         username = remover_acento(username)
            
        nomeCompleto = identificar_sobrenome(nome).split()
        sobrenome = ' '.join(nomeCompleto[1:]) if len(nomeCompleto) > 1 else ''

        confirmaEmail = None
        while confirmaEmail not in ['s','n']:
            confirmaEmail = console.input("Deseja criar E-mail? [bold yellow][S/N][/] ").lower()
            try:
                if confirmaEmail not in ['s','n']:
                    console.print("[bold red]Escolha uma alternativa válida![/]")
            except ValueError:
                 console.print("[bold red]Escolha uma alternativa válida![/]")
                 
        if confirmaEmail == "n":
            email = ""
        else:
            email = username + "@unaerp.br"
        console.clear()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Nome Completo: ")
        table.add_column("Usuário: ")
        table.add_column("Endereço de E-mail: ")
        table.add_column("Código Funcional: ")
        table.add_column("Usuário a copiar: ")
        table.add_row(
        " ".join(nomeCompleto) if isinstance(nomeCompleto, list) else str(nomeCompleto),
        " ".join(username) if isinstance(username, list) else str(username),
        " ".join(email) if isinstance(email, list) else str(email),
        " ".join(codigoFun) if isinstance(codigoFun, list) else str(codigoFun),
        " ".join(userACopiar) if isinstance(userACopiar, list) else str(userACopiar),
    )

        console.print(table)
        confirCriacao = None
        while confirCriacao not in ['s', 'n']:
            confirCriacao = console.input("Deseja confirmar a criação? [bold yellow][S/N][/]").lower()
            try:
                if confirCriacao not in ['s', 'n']:
                    console.print("[bold red]Escolha uma alternativa válida![/]")
            except ValueError:
                console.print("[bold red]Escolha uma alternativa válida![/]")
                
        if (confirCriacao == "s"):
                print("----------------------------------------\n")

                atributosCriacao = [
                    "powershell.exe",
                    "-ExecutionPolicy", "Bypass",
                    "-File", r'...\ChamarCriacao.ps1', 
                    "-OrigUser", userACopiar, 
                    "-NewUser", username,
                    "-codigo", codigoFun, 
                    "-email", email, 
                    "-nome", nomeCompleto[0], 
                    "-sobrenome", sobrenome,
                ]
                
                try:
                    process = subprocess.run(
                        atributosCriacao,
                        capture_output=True,
                        text=True,
                        check=True
                    )

                    print("Criação iniciada com sucesso (Verifique o log do PS):")
                    print(process.stdout) 
                    print(process.stderr)
                    
                except subprocess.CalledProcessError as e:
                    print(f"\nERRO FATAL na execução do PowerShell.")
                    print("Saída de Erro (stderr):")
                    print(e.stderr)
                    
                except FileNotFoundError:
                    print("\nERRO: powershell.exe não encontrado. Verifique sua instalação do PowerShell.")

                    print("Resultado da execução:")
                    print(process.stdout)
                    print(process.stderr)
        else:
            os.system('cls')
            print("Usuário não foi criado!")

        console.clear()

        with open (r'...\senhaGerada.txt', 'r') as arquivoLido: #Senha Gerada pelo Script de crialão de e-mail
            senhaGerada = arquivoLido.read().strip()
            
        if confirmaEmail != 'n':
            console.print("[bold]-------Criação de [yellow]E-mail[/] iniciada-------[/]", justify="center")
            uo_dict = {
                1: "/Administrativo/Ribeirão Preto",
                2: "/Administrativo/Guarujá"
            }
            grupo_dict = {
                1: "campus_ribeirao@unaerp.br",
                2: "campus_guaruja@unaerp.br"
            }

            escolha = None
            
            while escolha not in uo_dict:
                escolha = int(console.input("Escolha a Unidade organizacional do usuário: [bold #2773F5][1]RIB[/] [bold #F2F70A][2]GJA[/] - "))
                try:
                    if escolha not in uo_dict:
                        print("[red]Escolha uma UO Válida![/]")
                except ValueError:
                 print("[red]Digite apenas números válidos![/]")
            unid_organ = uo_dict[escolha]

            grupo = grupo_dict.get(escolha)
             
            cmd = [
                gam_path, "create", "user", username,
                "firstname", nomeCompleto[0],
                "lastname", sobrenome,
                "password", senhaGerada,
                "org", unid_organ
            ]

            cmd_group = [
                gam_path, "update", "group", grupo, "add", "member", email
            ]

            subprocess.run(cmd)
            subprocess.run(cmd_group)
        
            subprocess.run([sys.executable,
            r'...\Automatização_Email.py', username])
                    
        reiniciarScript(nomeCompleto,username,email,senhaGerada)
if __name__ == "__main__":
    main()
