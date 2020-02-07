function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}
Function Date{ 
   (Get-Date)
}
Function Host2{ 
    ($Host).Name   
}
Function Power{ 
    ($Host).Version
}
$IP = getIP
$date = Date
$Host2 = Host2
$User = User
$power = Power
$body = "This Machine's IP is $IP User is $env:USERNAME Powershell version $Power
today's date is $date"
Send-MailMessage -To "tbaronti@gmail.com" -From "t-barton@outlook.com" -Subject "IT3038c windows systeminfo" -Body $body -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (Get-Credential)
#Write-Host($body)