print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip_pct = input ("What percent tip would you like to give? 15, 20, or 25? ")
people = input("How many people to split the bill? ")

tip_amt = float(bill) * (int(tip_pct) / 100)
total_bill = float(bill) + tip_amt

per_person = round(total_bill / int(people), 2)
per_person = "{:.2f}".format(per_person)
print(f"Each person should pay: ${per_person}")