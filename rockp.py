from random import randint as r

choice = ["rock", "paper", "scissors"]# Lower case only!

computerChoice = choice[r(0,2)]

yourChoice = input("")# Type Trump, China or Mexico too see fun stuff!
print("You choose:")
print(yourChoice)
print("Computer choose:")
print(computerChoice)
print("Result:")


if yourChoice == "rock" and computerChoice == "paper" or\
yourChoice == "paper" and computerChoice == "scissors" or\
yourChoice == "scissors" and computerChoice == "rock":
    print("You lost!")
    print("Did you really think that you would win?")
elif yourChoice == computerChoice:
    print("It's a draw!")
    print("You just got lucky, I will beat you next time")
elif yourChoice == "paper" and computerChoice == "rock" or\
yourChoice == "rock" and computerChoice == "scissors" or\
yourChoice == "scissors" and computerChoice == "paper":
    print("You won!")
    print("You are hacking that is why you won!")
    print("I will build a wall next time so you cannot cheat!")
elif yourChoice == "Trump":
  print("I will build a wall, and I am gonna make the mexicans pay for it. I'm gonna use my helicopter and take a part of the chinese Great Wall and the mexicans will pay for it.")
elif yourChoice == "China":
    print("I love China, China is great. China China China China China. We can't let China rape our country and that's what they are doing.")
elif yourChoice == "Mexico":
    print("All mexicans are rapists and I am gonna build a wall so that they can rape on their own side. A wall a day keeps the mexicans away!")
else:
    print("Please type rock, scissors or paper.")
    print("Or you can just give up!")
