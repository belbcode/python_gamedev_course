from dataclasses import replace
from numpy import character
import pygame
from sys import exit

pygame.init()

width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Textris v1')
clock = pygame.time.Clock()


def tuplePosition(obj):
    arr = []
    for key in obj:
        arr.append(obj[key])
    return arr



class Background:
    def __init__(self, size, position) -> None:
        self.reference = pygame.Surface(size)
        self.position = position
    
    def changeColor(self, color):
        self.reference.fill(color)

class AmongUs:
    def __init__(self, imagePaths) -> None:
        self.imagePath = 'redCrewmate/redcrew1big.png'
        self.surface = pygame.image.load(self.imagePath)
        self.position = {'x': 0, 'y': 0}
    
    def reposition(self, x, y):
        self.position = {'x': x, 'y': y}
    

    def walk(self, distance, coordinate):
        if self.imagePath == 'redCrewmate/redcrew1big.png':
            self.imagePath = 'redCrewmate/redcrew2big.png'
        else:
            self.imagePath = 'redCrewmate/redcrew1big.png'

        self.position[coordinate] += distance
        self.surface = pygame.image.load(self.imagePath)
        
                # self.position[0] -= 9
                # self.surface = pygame.image.load(self.imagePath)

imagePath = ['redCrewmate/redcrew1big.png', 'redCrewmate/redcrew2big.png']

crewmate = AmongUs(imagePath)
crewmate.reposition(400,200)


sceneA = Background((width, height), (0,0))
sceneA.changeColor("Blue")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            # for key in directions:
            if event.key == pygame.K_UP:
                crewmate.walk(-10, 'y')
            if(event.key == pygame.K_DOWN):
                crewmate.walk(10, 'y')
            if event.key == pygame.K_LEFT:
                crewmate.walk(-10, 'x')
            if(event.key == pygame.K_RIGHT):
                crewmate.walk(10, 'x')
                
        
    screen.blit(sceneA.reference,sceneA.position)
    screen.blit(crewmate.surface, tuplePosition(crewmate.position))

    keys = pygame.key.get_pressed()


    pygame.display.update()
    clock.tick(60)