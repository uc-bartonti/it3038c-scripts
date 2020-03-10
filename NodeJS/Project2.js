
var expenses = [];


while(true){
    process.stdout.write("Add an expense if done type done")
    process.stdout.on('test',function(test)){
        if(test === "done" || test === null){
            break;
        }
    }
    expenses.push(Number(test));
} 

//console.log(budget - expenses);