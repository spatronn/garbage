for ($i=1; $i -le 5; $i++)

{
$chars = [char[]]"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
$DNS = (($chars[0..25]|Get-Random)+(($chars|Get-Random -Count 14) -join ""))

function RandomIPv4 {
return [IPAddress]::Parse([String] (Get-Random) )
}
$IP =  (RandomIPv4).IPAddressToString

Add-DnsServerResourceRecordA -Name $DNS -ZoneName "contoso.com" -IPv4Address $IP
}
