param (
    [string]$OrigUser,
    [string]$NewUser,
    [string]$codigo,
    [string]$email,
    [string]$nome,
    [string]$sobrenome
)
    $CredentialPath = "Caminho das credenciais"


try {
    Write-Host "Tentando importar credenciais..."
    $Credenciais = Import-Clixml -Path $CredentialPath
}
catch {
    Write-Error "Erro ao carregar o arquivo de credenciais. Verifique o caminho e as permissões."
    exit 1 
}
  # Caminho do script a ser chamado
    $scriptPath = ".\CriarUsuario.ps1"
    # Argumentos a serem passados para o script destino
    $argumentos = "-File `"$scriptPath`" -OrigUser `"$OrigUser`" -NewUser `"$NewUser`" -codigo `"$codigo`" -email `"$email`" -nome `"$nome`" -sobrenome `"$sobrenome`""
    

# Executa o script com as credenciais fornecidas
Start-Process "powershell.exe" `
    -Credential $Credenciais `
    -ArgumentList $argumentos `
    -NoNewWindow `
    -Wait
