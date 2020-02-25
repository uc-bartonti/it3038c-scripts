
//console.log(`process arg: ${process.argv}`)
function hostnamelookup(hostname){
    dns.lookup(hostname, function(err, addresses, family) {
        console.log(addresses)
    }
}

if(ProcessingInstruction.argv.length <=2) {
    console.log("USAGE: node " + __filename + " hostname.com");
    ProcessingInstruction.exit(-1)
}

var hostname = process.argv[2]; 
console.log(`checking IP of ${hostname}`);
hostnamelookup(hostname)