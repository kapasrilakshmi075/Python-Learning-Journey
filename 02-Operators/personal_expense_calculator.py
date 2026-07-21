name="Srii"
monthly_income=40000
rent=5000
food=3000
travel=2000
shopping=10000
other_expenses=2000
expenses={"rent":rent,
          "food":food,
          "travel":travel,
          "shopping":shopping,
          "other_expenses":other_expenses}
expenses_categories=["rent","food","travel","shopping","other_expenses"]
total_expenses=rent+food+travel+shopping+other_expenses
remaining_balance=monthly_income-total_expenses
percentage_spent=(total_expenses/monthly_income)*100
expenses_income=total_expenses<monthly_income
balance=remaining_balance>0
financial_status=expenses_income and balance
expenses_membership=("food" in expenses_categories)
other_expenses+=500
total_expenses=rent+food+travel+shopping+other_expenses
remaining_balance=monthly_income-total_expenses

print("------PERSONAL EXPENSE CALCULATOR------")
print("name:",name)
print("monthly_income:",monthly_income)
print("rent:",rent)
print("food:",food)
print("travel:",travel)
print("shopping:",shopping)
print("other_expenses:",other_expenses)
print("expenses:",expenses)
print("expenses_categories:",expenses_categories)
print("total_expenses:",total_expenses)
print("remaining balance:",remaining_balance)
print("percentage_spent:",percentage_spent)
print("total expenses less than montly expenses?:",expenses_income)
print("is remaining balance greater than o?:",balance)
print("is total expenses are less than income and greater than remaninig balance greater than 0?:",financial_status)
print("is food exist in expenses_categories?:",expenses_membership)
print("updated total expenses:",total_expenses)
print("updated remaining balance:",remaining_balance)


