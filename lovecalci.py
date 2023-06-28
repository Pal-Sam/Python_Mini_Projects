yname=input("Enter your name :")
hname=input("Enter HIS or HER name :")

lower_name=yname.lower()+hname.lower()

no_of_true=0
no_of_love=0

for i in "true":
    no_of_true+=lower_name.count(i)
for i in "love":
    no_of_love+=lower_name.count(i)
        

print(f"THE LOVE SCORE IS {no_of_true}{no_of_love} %")

