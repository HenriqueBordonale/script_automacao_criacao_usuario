param (
    [string]$OrigUser,
    [string]$NewUser,
    [string]$codigo,
    [string]$email,
    [string]$nome,
    [string]$sobrenome
)

Write-Output "Parâmetros recebidos:"
Write-Output "OrigUser: $OrigUser"
Write-Output "NewUser: $NewUser"
Write-Output "Codigo: $codigo"
Write-Output "Email: $email"
Write-Output "Nome completo: $nome"
Write-Output "Sobrenome: $sobrenome"

# Solicita as credenciais administrativas
$Credenciais = Get-Credential

# Caminho do script a ser chamado
$scriptPath = "D:\documents\Script_Criacao_Usuario\CriarUsuario.ps1"

# Argumentos a serem passados para o script destino
$argumentos = "-File `"$scriptPath`" -OrigUser `"$OrigUser`" -NewUser `"$NewUser`" -codigo `"$codigo`" -email `"$email`" -nome `"$nome`" -sobrenome `"$sobrenome`""

# Executa o script com as credenciais fornecidas
Start-Process "powershell.exe" `
    -Credential $Credenciais `
    -ArgumentList $argumentos `
    -NoNewWindow `
    -Wait
