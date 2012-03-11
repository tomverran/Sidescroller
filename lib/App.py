from Managers import ScrollManager, FrictionManager, MovementManager
from World import World
__author__ = 'Tom'
import pygame
import sys

class Application:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption('SideScroller')
        pygame.display.set_mode([1024,600])

        self.world = World()
        self.world.addManager('player',MovementManager())
        self.world.addManager('scrollable',ScrollManager())
        self.world.addManager('friction',FrictionManager())
        self.world.load('lvl/maps.txt','lvl/1.txt')
        self.clock = pygame.time.Clock()
        self.go = True

    def loop(self):

        while self.go:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(60)
            self.world.update( events )
            self.world.draw(pygame.display.get_surface())
            pygame.display.flip()