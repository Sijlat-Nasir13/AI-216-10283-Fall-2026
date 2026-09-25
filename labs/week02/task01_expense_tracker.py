# Input:
# Processing:
# Output:

food_expense = 450
transport_expense = 200
other_expense = 150
daily_budget = 1000

total_expense = food_expense + transport_expense + other_expense
remaining_budget = daily_budget - total_expense

if total_expense < daily_budget:
    status = "Within budget"
elif total_expense == daily_budget:
    status = "Exactly at budget"
else:
    status = "Over budget"

print("Total expense:", total_expense)
print("Remaining budget:", remaining_budget)
print("Status:", status)