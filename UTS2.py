import random

life = 5
score = 0
while life != 0:
    a = random.randint(-20, 20)
    b = random.randint(-20, 20)
    result = a + b
    print("What is the result of: ", a, "+", b, "?")
    Answer = int(input())
    if Answer == result:
        score += 10
        print("You are correct!")
        print("Your current score is: ", score, "Points")
        print("(Life: ", life, ")")
    elif Answer != result:
        score -= 2
        life -= 1
        print("You are incorrect! The answer is ", result)
        print("Your current score is: ", score, "Points")
        print("(Life: ", life, ")")
print("You have 0 lives game over")
print("Your final score is: ", score)
