# module
import random
import time
import pickle

# python program to get IP address
import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

# Variables
menu = 0
scoremenu = 0

# game code
def gamecode():
    menu2 = 0
    guess = 0
    score = 100
    menu2 = menu2 - menu2
    num = random.randint(1, 100)
    name = input("Enter your name: ")
    print("Welcome to the game of darkness, ", name)
    time.sleep(2)
    print("If you lose you will be sent to the shadow realm")
    time.sleep(2)
    print("Let's begin")
    time.sleep(2)
    print("A number between 1 to 100 has been chosen")
    time.sleep(2)
    print("Try to guess the random number that has been generated")
    while guess != num:
            guess = int(input("Guess the number: "))
            if score == 0:
                print("Your score is 0, you lose rip bozo")
            elif score == 30:
                print("You only have 3 guesses left before you are sent to the shadow realm")
            elif score == 10:
                print("You better pack your bags")
            if guess < num:
                print("Your number is too low")
                score = score - 10
                print("Your current score is: ", score)
            elif guess > num:
                print("Your number is too high")
                score = score - 10
                print("Your current score is: ", score)
            elif guess == num:
                print("You are correct! the number is ", num)
                print("Congratulations! You win with a score of ", score)
                if score == 100:
                    print("I know where you live", ip)
                elif score < 100 and score >= 90:
                    print("Not bad")
                elif score < 90 and score >= 60:
                    print("You are the average man how does that make you feel?")
                elif score < 60:
                    print("I know where you live ", ip)
                Scorelst = (name, score)
                pickle.dump (Scorelst, open ("score.lst", "wb"))
                break

# score menu
def menu3():
    menu2 = 0
    menu2 = menu2 - menu2
    Scorelst = pickle.load (open("score.lst", "rb"))
    Scorelst2 = list (Scorelst)
    print("SCORE LIST")
    for i in Scorelst2:
            print(i)
    Scorelst = tuple (Scorelst2)
    print(" ")
    print("Enter 1 to go back to the menu")
    print("Enter 3 to exit the game")
    scoremenu = int(input(""))
    if scoremenu == 1:
            scoremenu = scoremenu - scoremenu
            print("Enter 1 to play game")
            print("Enter 2 to see high score")
            print("Enter 3 to exit game")
            menu2 = int(input(""))
            if menu2 == 1:
                gamecode()
            elif menu2 == 2:
                menu3()

# menu prompt
print("Welcome to the 闇のゲーム")
print("Enter 1 to play")
menu = int(input(""))

# game
if menu == 1:
    print("Enter 1 to play game")
    print("Enter 2 to see high score")
    print("Enter 3 to exit game")
    menu2 = int(input(""))
    if menu2 == 1:
        gamecode()

    elif menu2 == 2:
        menu2 = menu2 - menu2
        Scorelst = pickle.load (open("score.lst", "rb"))
        Scorelst2 = list (Scorelst)
        print("SCORE LIST")
        for i in Scorelst2:
                print(i)
        Scorelst = tuple (Scorelst2)
        print(" ")
        print("Enter 1 to go back to the menu")
        print("Enter 3 to exit the game")
        scoremenu = int(input(""))
        if scoremenu == 1:
            scoremenu = scoremenu - scoremenu
            print("Enter 1 to play game")
            print("Enter 2 to see high score")
            print("Enter 3 to exit game")
            menu2 = int(input(""))
            if menu2 == 1:
                gamecode()
            elif menu2 == 2:
                menu3()

        elif scoremenu == 3:
            print("Weak")
            exit
        else:
            print("That is not in the prompt")
            exit

    elif menu2 == 3:
        print("Weak")
        exit
    else:
        print("That is not in the prompt")
        exit
else:
    exit