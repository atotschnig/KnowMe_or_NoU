import json
import random
#Title: BostonHacks2019
#Contributers: Agnes Totschnig, Saumyaa Verma 


################################################################################

def list_topics(questions):
    ''' takes in the database and returns a list of all the topics
        contained in it
    '''
    topics = []
    for q in questions:
        t = q['topic']
        if t not in topics:
            topics.append(t)
    return topics

def shortlist(questions, topic_wanted):
    shortlisted = []
    for q in questions:
        if topic_wanted == q['topic']:
            shortlisted.append(q)
    return shortlisted

################################################################################


filename = input("Enter file name: ") + '.json'

with open(filename) as json_file:
    questions = json.load(json_file)

topics = list_topics(questions)
print("The available topics are:" , topics)
valid = False
while not valid:
    topic_wanted = input("Enter the topic you want: ")
    valid = (topic_wanted in topics)
    if not valid:
        print("OOPS, couldn't find this topic! Re-enter topic name")
shortlisted = shortlist(questions, topic_wanted)

num_q = len(questions)
num_q_game = 3
score = 0

for index_q in range(num_q_game):
    q = random.choice(shortlisted)
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
 
