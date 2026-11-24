    # Password generator

import secrets

print("Welcome to MyPassword Generator! ")

scret_password=[]

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_+{}|;:,.<>?/~"


Total_letters=int(input("How many letters would you like in your password? "))

Total_symbols=int(input("How many symbols would you like? "))

Total_numbers=int(input("How many numbers would you like? "))

length=Total_symbols+Total_numbers+Total_letters



for l in range(Total_letters):
    scret_password.append(secrets.choice(letters))
for n in range(Total_numbers):
    scret_password.append(secrets.choice(numbers))
    
for s in range(Total_symbols):
    scret_password.append(secrets.choice(symbols))
    
    
    
secrets.SystemRandom().shuffle(scret_password)

final_password="".join(scret_password)

print(f"\n Your {length} digit Secure Password is:  {final_password}\n   Save it now , You will never find this again.")


