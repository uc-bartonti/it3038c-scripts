## Upgrade on my powershell version of a buget traking script

##Start off asking for the starting budget to do calculations down the road with
##try used to avoid user typing letters
try:
    budget = int(input('Enter your budget:'))
except:
    print('That value is not a number.')

    
## Loop to get the expenses
##once the user types stop or trys to enter a nonstring the loop will end
try:
    expenseList = []
    while True:
        print('Enter an expense once done type stop')
        expenseList.append(int(input()))
except:
    print(expenseList)

## adding the expenses together and get the number of expenses entered
expenseEntry = len(expenseList)
totalExpense = int(sum(expenseList))
##print the aount of expenses and total
print ('You have a total of', expenseEntry, 'expenses')
print ('Your total expenses totals ', totalExpense, 'dollars')
##Display total
print('Your remaining buget is', budget - totalExpense, 'dollars')