import pygame

colours = [(255,0,0), (255,255,0), (0,0,255), (0,255,0)]

pygame.init()
screen = pygame.display.set_mode((1200, 750))
screen.fill((255, 255, 255))
done = False

font = pygame.font.SysFont("comicsansms", 72)

# title
text = font.render("Know Me or No U", True, (109, 0, 99))
screen.blit(text, (320, 40))

question = {"question": "What habit annoys you most?","answer1": "Leaving things around the house","answer2": "Chewing loudly","answer3": "Slow walkers","answer4": "Nail bitting","topic": "random"}

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    font = pygame.font.SysFont("comicsansms", 35)
    text = font.render("Q: " + question['question'], True, (0,0,0))
    screen.blit(text, (150,200))
    for i in range(4):
        text = font.render(str(i+1) + '. ' + question['answer'+str(i+1)], True, colours[i])
        screen.blit(text, (200,300 + 75*i))
    pygame.display.flip()
    

pygame.quit()
