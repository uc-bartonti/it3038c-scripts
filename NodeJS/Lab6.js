var http = require("http")
var fs = require("fs")
var os = require("os")
var ip = require("ip")

name = os.hostname;


uptime = os.uptime
uptimeDays = Math.floor (uptime / 86400)
uptime = uptime - (uptimeDays * 86400);
upHours = Math.floor (uptime / 3600);
uptime = uptime - (upHours * 3600);
upMins = Math.floor (uptime / 60);
uptime = uptime - (upMins *60)
upSecs = Math.floor (uptime);

cpus = os.cpus(),
cpuNumber = cpus.length;
Memory = os.totalmem;
FreeMemory = os.freemem;
TotalMemory = Memory / 1000000;
FreeMemory = FreeMemory / 1000000;

var server = http.createServer(function(req,res){
    res.writeHead(200, {"Content-Type":"text/html"});
    res.end(
        
        
        `
        <!DOCTYPE html>
        <html>
         <head>
         <title> Node JS Baby</title>
         </head>
         <body>
         <p>Hostname: ${name} </p>
         <p>Server Uptime: Days:${uptimeDays},Hours:${upHours},Minutes:${upMins},Seconds:${upSecs}</p>
         <p>Total Memory: ${TotalMemory} MB </p>
         <p>Free Memory: ${FreeMemory} MB </p>
         <p>CPUs: ${cpuNumber} </p>
         </body>
        </html> 
    
        `
    )

});

server.listen(3000)
console.log("Server listening on port 3000");