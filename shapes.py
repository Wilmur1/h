import pygame
import sys
screen = pygame.display.set_mode((1520,780))
pygame.display.set_caption("screen")

'''[rectangle1 =pygame.Rect(100,200,70,90)
pygame.draw.rect(screen,"white",rectangle1)
pygame.draw.circle(screen,"blue",(300,600),30,3)'''

class circle:
    def __init__(self,color,co_ordinates,radius,width):
          self.color = color
          self.co_ordinates = co_ordinates
          self.radius = radius
          self.width = width
    def circ(self):
         pygame.draw.circle(screen,self.color,self.co_ordinates,self.radius,self.width)
    def grow(self):
         self.radius = self.radius + 5
circle_object1 = circle("green",(400,200),50,5)
circle_object2 = circle("red",(600,310),90,7)
         

while True:        
     for event in pygame.event.get():
          circle_object1.circ()
          circle_object2.circ()
          if event.type == pygame.MOUSEBUTTONDOWN:
               circle_object1.grow()
               circle_object2.grow()
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
     pygame.display.update()