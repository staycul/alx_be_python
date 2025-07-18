# Prompt user for monthly income and expenses
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate projected annual savings with 5% interest
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = int(annual_savings + interest)

# Print results
print(f"Your monthly savings are ${monthly_savings: }.")
print(f"Projected savings after one year, with interest, is: ${projected_savings: }.")

