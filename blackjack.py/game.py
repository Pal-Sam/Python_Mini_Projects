import random
from logo import logo

print(logo)
cards=['A',2,3,4,5,6,7,8,9,'K','J','Q']
my_card=[]
comp_card=[]
def get_cards():
    return random.choice(cards)


for i in range(2):
    my_card.append(get_cards())
    comp_card.append(get_cards())


def find_winner():
    sum1=0
    sum2=0
    print(f"Your final cards : {my_card}")
    print(f"Computer's final cards : {comp_card}")
    for i in my_card:
        if i in ['K','Q','J']:
            sum1+=10
        elif i=='A':
            sum1=sum1+int(input("Its an Ace!! Choose the value for Ace ,either 1 or 11 :"))
        else:
            sum1=sum1+i
    for i in comp_card:
        if i in ['K','Q','J']:
            sum2+=10
        elif i=='A':
            sum2=sum2+random.choice([1,11])
        else:
            sum2=sum2+i
    if sum1>sum2:
        if sum1<=21:
            print("You Win")
        else:
            print("Computer Wins")
    elif sum1==sum2:
        print("Draw match")
    else:
        print("Computer Wins")



print(f"Your cards : {my_card}")
print(f"Computer's first card : {comp_card[0]}")
option=input("Type 'y to get another card, type 'n' to pass: ")
if option=='y':
    my_card.append(get_cards())
    
find_winner()
    
