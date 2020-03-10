[int]$budget = 0
[int]$expenses = 0
[int]$final_budget = 0

[int]$budget = Read-Host("what is your budget")


do{
    [int]$test = Read-Host("Add an expense if done type 0") 
    [int]$expenses = $test + $expenses
       
}while($test -ne 0)


[int]$final_budget = $budget-$expenses

echo "Your remaining budget after expenses is $final_budget dollars"