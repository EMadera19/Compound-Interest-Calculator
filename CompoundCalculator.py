# Compound Interest Calculator

principle = 0
interest_rate = 0
time = 0

# principle loop
while principle <= 0:
    principle = float(input("Enter the Principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

# Interest Rate loop
while interest_rate <= 0:
    interest_rate = float(input("Enter the interest rate amount: "))
    if interest_rate <= 0:
        print("Interest rate can't be less than or equal to zero")

# Time Loop
while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

# Calculation
total = principle * pow((1 + interest_rate / 100), time)
print(f"Your balance after {time} Year/s is: ${total:.2f}")
