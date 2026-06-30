print("Bill Spilt Calculator")
bill_amount = float(input())
tip = float(input())
people = int(input())
tip_amount = (tip / 100) * bill_amount
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / people 
print(total_amount)
print(amount_per_person)