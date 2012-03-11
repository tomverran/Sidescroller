
__author__ = 'Tom'
from Sprite import Sprite
from collections import deque
import pygame

class Tile(object):
    def __init__(self):
        self.image = ''
        self.flags = []

class World(object):

    def __init__(self):
        self._group = pygame.sprite.OrderedUpdates()
        self._managers = {}
        self._sprites = {}
        self._tiles = {}
        self._tiles = {}

    def load(self, mappings, level):
        self._loadMappings(mappings)
        self._loadLevel(level)

    def _loadMappings(self, file):
        mappings = open(file,'r')
        for i,line in enumerate(mappings):
            mappingItem = deque(line.split())
            if mappingItem[0].strip() != '#':

                #populate images list
                key = mappingItem.popleft()
                image = mappingItem.popleft()

                tile = Tile()
                tile.image = pygame.image.load(image).convert()
                tile.flags = mappingItem
                self._tiles[key] = tile

    def _loadLevel(self, file):
        rect = pygame.Rect(0,0,32,32)
        level = open(file,'r')
        x, y = 0, 0

        for i,line in enumerate(level):
            for tile in list(line):
                if tile == '\n':
                    break
                elif self._tiles.has_key(tile):

                    #create sprite
                    sprite = Sprite()
                    sprite.rect = rect.move(x,y)
                    sprite.image = self._tiles[tile].image
                    sprite.image.set_colorkey([255,0,255])
                    sprite.flags = self._tiles[tile].flags
                    self._group.add(sprite)

                    #add to managers based on flags
                    for flag in self._tiles[tile].flags:
                        if flag in self._managers.keys():
                            self._managers[flag].add(sprite)
                x+=32
            y += 32
            x = 0

    def addManager(self, name, object):
        self._managers[name] = object

    def update(self, events):
        self._group.update()
        for manager in self._managers.items():
            manager[1].update(events)

    def draw(self, surface):
        self._group.draw(surface)
