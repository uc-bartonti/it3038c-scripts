## Upgrade on my powershell version of a buget traking script

print('Enter your budget:')
budget = input()

try:
    expenseList = []
    while True:
        expenseList.append(int(input()))
except:
    print(expenseList)

expenseEntry = len(expenseList)
totalExpense = sum(expenseList)
print ('Your total expenses totals ', totalExpense)