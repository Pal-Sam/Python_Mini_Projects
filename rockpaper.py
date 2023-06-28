import random 

def rock() :
    print("\n\n")
    print(''' "!!!IT' IS A ROCK!!!ROCKKKKKKKKKKKKKK"
              \
 _____         \
| | | |/\       \
|_|_|_|\ \       \
|        /
\_______/            (  ( ) ) ( )  )
 \______\           ( ( ( ( )  )  ) )
 \       \         ( ( )) ) (   ) ( ( )
  \       \        ( (__.-.___.-.__) )
   \       \        /---._.---._.--- \
    \       \       \||   '  \'    ||/
     \       \       |||     _)   |||
      \       \       ||||///\\\||||
       \       \_____/ ||||\__/||||\___
        \             \ |||||||||| /   \
         \             \  ||||||  /     \
          \_____''')
    
def scisorrs():
    print("\n\n")
    print(''' "!!!IT' IS SCISSORS!!! SCISORRSSSSSSSSSSSSS"
              \
 _____         \
| | | |/\       \
|_|_|_|\ \       \
|        /
\_______/            (  ( ) ) ( )  )
 \______\           ( ( ( ( )  )  ) )
 \       \         ( ( )) ) (   ) ( ( )
  \       \        ( (__.-.___.-.__) )
   \       \        /---._.---._.--- \
    \       \       \||   '  \'    ||/
     \       \       |||     _)   |||
      \       \       ||||///\\\||||
       \       \_____/ ||||\__/||||\___
        \             \ |||||||||| /   \
         \             \  ||||||  /     \
          \_____''')


urchoice=int(input("Type 0 for Rock and Type 1 for Scissors.")) 

if urchoice==0:
    rock()
else:
   scisorrs()

compchoice=random.randint(0,2)
print("Computer\'s choice :")

if compchoice==0:
    rock()
else:
   scisorrs()

if (compchoice==0 and urchoice==0) or (compchoice==1 and urchoice==1):
    print("\n\n")
    print("Draw match!!")
elif compchoice==0:
    print("\n\n")
    print("Computer wins!!")
elif urchoice==0:
    print("You win!!")
