import compound_interest_calculator
import simple_interest_calculator

print("Welcome to the simple and compount interest calculator.")
print("Press:")
print("1. for simple interest calc")
print("2. for compount interest calc")
option = int(input(""))
if option == 1:
    simple_interest_calculator.run()

elif option == 2:
    compound_interest_calculator.run()

else:
    print("Invalid response, please try again.")
