
import random

print("WELCOME TO THE NUMBER GUESSNNG GAME")
print("Choose two number between which you want to play")

a=int(input("Enter the first number\n"))
b=int(input("Enter the last number\n"))

c=random.randint(a,b)
x=input("press Y to start game\n")
while(x=="Y"):
    u=int(input("Enter your guessing\n"))
    if(c==u):
        input("congratulation! You success to guess my number..." )
        break
    elif(c>u):
        print("your nnumber is smaller than my number\n")
    elif(c<u):
        print("your number is graeter than my number\n")
        continue
x=input("do you want play again then press Y\n")
