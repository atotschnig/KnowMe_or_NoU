#Title: BostonHacks2019
#Contributers: Agnes Totschnig, Saumyaa Verma

import json
import random
import serial
import time


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


def getLatestStatus():
    status = ser.readline()
    while ser.inWaiting() > 0:
        status = ser.readline()
    string_n = status.decode()
    string = string_n.rstrip()
    return string

def check_answer(buttons):
    #print('checks', buttons)
    for index in range(4):
        if buttons[index] == '1':
            #print('answered', index + 1)
            return True, index+1
    return False, 0

def read_arduino():
    #print('reading')
    correct, guess = 0, 0
    answered1, answered2 = False, False
    while not(answered1 and answered2):
        buttons = getLatestStatus()
        if not answered1:
            answered1, correct = check_answer(buttons[0:4])
        if not answered2:
            answered2, guess = check_answer(buttons[4:8])
    return correct, guess

################################################################################


filename = input("Enter file name: ") + '.json'

# import questions from json file
with open(filename) as json_file:
    questions = json.load(json_file)


# sort all questions by topics and ask for topic choice from user
topics = list_topics(questions)
print("The available topics are:" , topics)
valid = False
while not valid:
    topic_wanted = input("Enter the topic you want: ")
    valid = (topic_wanted in topics)
    if not valid:
        print("OOPS, couldn't find this topic! Re-enter topic name")
shortlisted = shortlist(questions, topic_wanted)


# set up arduino input
ser = serial.Serial('/dev/cu.usbmodem14201',9600)


num_q = len(questions)
num_q_game = 3
score = 0

for index_q in range(num_q_game):
    q = random.choice(shortlisted)
    print(q['question'])
    for index_a in range(4):
        print(str(index_a + 1) + '. ' + q['answer' + str(index_a + 1)])
    correct, guess = read_arduino()
    if guess == correct:
        score += 1
        print("Correct answer! :D")
    else:
        print("Wrong answer! :(")
print("Your score is:",  score)
