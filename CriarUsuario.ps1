param (
    [string]$OrigUser,
    [string]$NewUser,
    [string]$codigo,
    [string]$email,
    [string]$nome,
    [string]$sobrenome
)

$senha = -join ((0..9) | Get-Random -Count 8)

# Obter as propriedades do usuário modelo
$User = Get-ADUser -Identity $OrigUser -Properties MemberOf, Title, Department, Company, HomeDirectory, HomeDrive
# Extrair a OU do usuário modelo
$UserOU = $User.DistinguishedName -replace "^CN=[^,]+,", ""

$Campus = ($User.Company).trim().ToLower()


if ($Campus -like "*preto*") {
    $Servidor = "servidor-ribeirao"
}
elseif ($Campus -like "*guaruj*") {
    $Servidor = "servidor-guaruja"
}

$homePath = "\\$Servidor\home\$NewUser"

# Criar novo usuário na mesma OU
try {
  $params = @{
        Name              = "$nome $sobrenome"
        SamAccountName    = $NewUser
        UserPrincipalName = "$NewUser@dominio.br"
        Path              = $UserOU
        Enabled           = $true
        GivenName         = $nome
        Surname           = $sobrenome
        DisplayName       = "$nome $sobrenome"
        AccountPassword   = (ConvertTo-SecureString "$senha" -AsPlainText -Force)
    }

    if ($User.Title)      { $params.Title          = $User.Title }
    if ($User.Department) { $params.Department     = $User.Department }
    if ($codigo)          { $params.Description    = $codigo }
    if ($email)           { $params.OtherAttributes = @{ mail = $email } }
    if ($User.Company)    { $params.Company        = $User.Company }
    if ($User.HomeDirectory) { $params.HomeDirectory = $homePath
         New-Item -Path $homePath -ItemType Directory}
    if ($User.HomeDrive) {$params.HomeDrive = "P:"}
    
    New-ADUser @params
           
}
catch {
    Write-Error "Erro ao criar usuario: $_"
    exit 1
}
Set-Content -Path ".\senhaGerada.txt" -Value $senha
# Adicionar o novo usuário aos mesmos grupos do usuário modelo
foreach ($Group in $User.MemberOf) {
    Add-ADGroupMember -Identity $Group -Members $NewUser
}

$validacaoUser = Get-ADUser -Identity $NewUser -ErrorAction SilentlyContinue
if ($null -ne $validacaoUser){
    Write-Host "---------------------------------------" -ForegroundColor DarkYellow
    Write-Host "Usuário Criado conforme solicitado." -ForegroundColor Green
    Write-Host "Usuário: '$NewUser'" -ForegroundColor White
    Write-Host "Senha: $senha" -ForegroundColor White
}
else{
    Write-Error "Erro ao criar ou encontrar o usuário '$NewUser'!"
}
