print("How many years will you be saving?")
years = int(input("Enter years: "))

print('************************************************')

print("How much money is in your account?")
main_income = float(input("Enter current amount in your account: "))

print('************************************************')

print("How much money do you plan on investing monthly?")
monthly_invest = float(input("Enter amount you plan to invest: "))

print('************************************************')

print("What do you think will be your yearly interest of this investment?")
interest = float(input("Enter interest in decimals (10% = 0.1): "))

print('************************************************')

print(' ')

monthly_invest = monthly_invest * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = main_income
    
    #Calculating the compound interest over designated years
    final_amount = (final_amount + monthly_invest) * (1 + interest)
    
print("The amount of money you would have in your account after {} years: ".format(years) + str(final_amount))    

