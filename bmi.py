weight=float(input("Enter your weight "))
height=float(input("Enter your height "))

bmi=(weight/(pow(height,2)))

if bmi> 35:
    print("clinically obese")
elif bmi>30 :
    print(" obese")
elif bmi>25 :
    print(" overweight")
elif bmi>18.5 :
    print(" normal weight")
else:
    print("underweight")