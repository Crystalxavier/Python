# Write a program to input the basic salary of an employee and calculate its
# Gross salary according to the following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%

basic_salary = float(input("Enter your basic salary: "))
if basic_salary <= 10000:
    hra = basic_salary * 20/100
    da = basic_salary * 80/100
elif basic_salary <= 20000:
    hra = basic_salary * 25 / 100
    da = basic_salary * 90 / 100
else :
    hra = basic_salary * 30 / 100
    da = basic_salary * 95 / 100
gross_salary = basic_salary + hra + da
print("HRA =", hra)
print("DA =", da)
print("Gross Salary =", gross_salary)
