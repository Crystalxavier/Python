# Calculate Employee Bonus. Write a Python program to calculate an
# employee's bonus based on their basic salary and years of service:
# ● Less than 2 years: 5% of basic salary
# ● 2 to 5 years: 10% of basic salary
# ● 6 to 10 years: 15% of basic salary
# ● More than 10 years: 20% of basic salary
# Calculate and display: Basic Salary , Bonus , Gross Salary = Basic Salary +
# Bonus

basic_salary = float(input("Enter basic salary: "))
years = int(input("Enter years of service: "))
if years < 2:
    bonus = basic_salary * 5 / 100
elif years <= 5:
    bonus = basic_salary * 10 / 100
elif years <= 10:
    bonus = basic_salary * 15 / 100

else:
    bonus = basic_salary * 20 / 100
gross_salary = basic_salary + bonus
print("Basic Salary =", basic_salary)
print("Bonus =", bonus)
print("Gross Salary =", gross_salary)