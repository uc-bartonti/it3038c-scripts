Function Alpha {
Add-Type -AssemblyName System.Speech
$SpeechSynthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer
$Size = Get-WmiObject -Class Win32_logicaldisk -Filter "DriveType ='3'" | ForEach-Object {[math]::Truncate($_.freespace / 1GB)}
$SpeechSynthesizer.SelectVoice('Microsoft Zira Desktop')
$SpeechSynthesizer.Rate = 2
$SpeechSynthesizer.Speak("The date and time is $(Get-Date)")
$SpeechSynthesizer.Speak("C drive free space is $Size gigabytes")
}
Alpha