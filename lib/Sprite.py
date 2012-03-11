__author__ = 'Tom'
import pygame

class Sprite(pygame.sprite.Sprite):

    def __init__(self):
        super(Sprite,self).__init__()
        self.flags = []
        self.forcex = 0
        self.forcey = 0

    def setForce(self,force):
        self.forcex, self.forcey = force

    def update(self, *args):
        self.rect.move_ip(self.forcex,self.forcey)