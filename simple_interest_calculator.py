def run():
    print("Welcome to the simple interest calculator.")
    principle = float(input("What is your principle amount (Starting money)?"))
    rate = float(input("What is the rate of increase per year in %?"))
    time = int(input("How many years of investment?"))
    simple_interest = principle * (rate/100) * time
    total_amount = float(principle + simple_interest)
    interest_earned = float(total_amount - principle)
    percentage = (interest_earned / principle) * 100
    print(f"Your total amount comes to: ${total_amount:.2f}")
    print(f"You interest earned is ${interest_earned:.2f}, which is a {percentage:.0f}% increase!")