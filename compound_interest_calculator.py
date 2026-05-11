def run():
    print("Welcome to the compound interest calculator.")
    principle = float(input("Principle amount?"))
    rate = float(input("Percenteage increase yearly?"))
    time = int(input("How many years?"))
    compound_amount = principle
    for i in range(time):
        compound_amount = compound_amount + compound_amount * (rate/100)
    print(f"Your final amount is ${compound_amount:.2f}")
    percentage_increase = float(compound_amount / principle) * 100 - 100
    print(f"That is a {percentage_increase:.2f}% increase!")