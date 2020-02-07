function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}
$IP = getIP
Write-Host("This Machine's IP is $IP")
Send-MailMessage -To "tbarton38@yahoo.com" -From "tbarton38@yahoo.com" -Subject "IT3038c windows systeminfo" -Body "body" -SmtpServer smtp.mail.yahoo.com -Port 465 -UseSsl -Credential (Get-Credential)
