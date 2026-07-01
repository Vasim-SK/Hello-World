import random 
otp = random.randint(1000, 5000)
print(otp)
OTP = int(input("Enter otp: "))
if otp == OTP:
    print("Successful")