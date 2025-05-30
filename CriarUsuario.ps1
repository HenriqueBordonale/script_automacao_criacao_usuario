param (
    [string]$OrigUser,
    [string]$NewUser,
    [string]$codigo,
    [string]$email,
    [string]$nome,
    [string]$sobrenome
)

$senha = -join ((0..9) | Get-Random -Count 8)

Write-Output "Credenciais que pegou: $OrigUser"
Write-Output "Credenciais que pegou: $NewUser"
# Obter as propriedades do usuário modelo
$User = Get-ADUser -Identity $OrigUser -Properties MemberOf, Title, Department

# Extrair a OU do usuário modelo
$UserOU = $User.DistinguishedName -replace "^CN=[^,]+,", ""
Write-Output "Usuario modelo esta na OU: $UserOU"
# Criar novo usuário na mesma OU
New-ADUser -Name "$nome $sobrenome" `
           -SamAccountName $NewUser `
           -UserPrincipalName "$NewUser@unaerpnet.br" `
           -Path $UserOU `
           -Title $User.Title `
           -Department $User.Department `
           -Enabled $true `
           -Description $codigo `
           -OtherAttributes @{mail = $email} `
           -GivenName $nome `
           -Surname $sobrenome `
           -DisplayName "$nome $sobrenome" `
           -AccountPassword (ConvertTo-SecureString "$senha" -AsPlainText -Force)
           
Write-Output "Usuario '$NewUser' criado na mesma OU de '$OrigUser'"

Set-Content -Path "D:\documents\Script_Criacao_Usuario\senhaGerada.txt" -Value $senha
# Adicionar o novo usuário aos mesmos grupos do usuário modelo
foreach ($Group in $User.MemberOf) {
    Add-ADGroupMember -Identity $Group -Members $NewUser
    Write-Output "Usuario '$NewUser' adicionado ao grupo '$Group'"
}

Write-Output "Processo concluido! Usuario '$NewUser' copiado com sucesso."
Write-Output "Usuário $NewUser com a senha $senha criados com sucesso!"