# tip calculator

total_bill = input("What was the total bill? £")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

result = ((int(tip_percentage) / 100 * float(total_bill)) + float(total_bill)) / int(people)

rounded_result = round(result, 2)

print(f"Each person should pay: £{rounded_result}")