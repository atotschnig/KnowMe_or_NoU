import json
import random

filename = input("Enter file name: ") + '.json'

with open(filename) as json_file:
    questions = json.load(json_file)

num_q = len(questions)
num_q_game = 3
score = 0

for index_q in range(num_q_game):
    q = random.choice(questions)
    print(q['question'])
    for index_a in range(4):
        print(str(index_a + 1) + '. ' + q['answer' + str(index_a + 1)])
    correct = int(input("Enter your correct answer: "))
    guess = int(input("Enter your guess: "))
    if guess == correct:
        score += 1
        print("Correct answer! :D")
    else:
        print("Wrong answer! :(")
print("Your score is:",  score)
 
