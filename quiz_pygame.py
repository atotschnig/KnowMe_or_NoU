#Title: BostonHacks2019
#Contributers: Julia Fowler, Aria Rens, Sarah Santoso, Agnes Totschnig and Saumyaa Verma

import json
import random
import serial
import pygame

colours = [(255,0,0), (255,255,0), (0,0,255), (0,255,0)]


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


# set up pygame screen
pygame.init()
screen = pygame.display.set_mode((1200, 750))
screen.fill((255, 255, 255))
done = False
    
def clear_with_title():
    screen.fill((255,255,255))
    font = pygame.font.SysFont("comicsansms", 72)
    text = font.render("Know Me or No U", True, (109, 0, 99))
    screen.blit(text, (320, 40))

clear_with_title()


num_q = len(questions)
num_q_game = 3
score = 0
new = True
counter = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if new:
        clear_with_title()
        
        q = random.choice(shortlisted)
        print(q['question'])
        for index_a in range(4):
            print(str(index_a + 1) + '. ' + q['answer' + str(index_a + 1)])
                
        font = pygame.font.SysFont("comicsansms", 35)
        text = font.render("Q: " + q['question'], True, (0,0,0))
        screen.blit(text, (150,200))
        for i in range(4):
            text = font.render(str(i+1) + '. ' + q['answer'+str(i+1)], True, colours[i])
            screen.blit(text, (200,300 + 75*i))

        correct, guess = 0, 0
        answered1, answered2 = False, False

    
    buttons = getLatestStatus()
    if not answered1:
        answered1, correct = check_answer(buttons[0:4])
    if not answered2:
        answered2, guess = check_answer(buttons[4:8])
    new = (answered1 and answered2)

    if new:
        counter += 1
        if counter == num_q_game:
            done = True
        
        if guess == correct:
            score += 1
            print("Correct answer! :D")
        else:
            print("Wrong answer! :(")
        print("Your score is:",  score)
    
    pygame.display.flip()

    
pygame.quit()



