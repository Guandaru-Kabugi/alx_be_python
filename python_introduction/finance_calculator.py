monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income-monthly_expenses
projected_interest = (monthly_savings * 12) * 0.05
projected_yearly_savings = round((monthly_savings*12) + projected_interest)
print(f"Projected savings after one year, with interest, is: {projected_yearly_savings}")