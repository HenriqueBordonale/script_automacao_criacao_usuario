# Esse é o wrapper que você pode chamar para iniciar o script com as credenciais administrativas
param (
    [string]$OrigUser,
    [string]$NewUser
)

Write-Output "Credenciais que pegou no script1: $OrigUser"
Write-Output "Credenciais que pegou no script1: $NewUser"
# Cria o objeto de credenciais
$Credenciais = Get-Credential

$scriptPath = "D:\documents\Script_Criacao_Usuario\CriarUsuario.ps1"

# Monta a linha de argumentos corretamente
$argumentos = "-File `"$scriptPath`" -OrigUser `"$OrigUser`" -NewUser `"$NewUser`""

# Executa com as credenciais
Start-Process "powershell.exe" `
    -Credential $Credenciais `
    -ArgumentList $argumentos `
    -NoNewWindow `
    -Wait