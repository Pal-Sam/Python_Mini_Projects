import random
print("Welcome to password generator!!")
l=int(input("How many letters would you like in your password : "))
s=int(input("How many symbols would you like in your password : "))
n=int(input("How many numbers would you like in your password : "))
alphabets=list("qwertyuiopasdfghjklzxcvbnm")
numbers=list("1234567890")
symbols=list("!@#$%^&*()<>?/;")
password=[]
for _ in range(l):
    password.append(random.choice(alphabets))
for _ in range(s):
    password.append(random.choice(symbols))
for _ in range(n):
    password.append(random.choice(numbers))
#print(password)
random.shuffle(password)
print("\nPassword generated for you : ","".join(password))



