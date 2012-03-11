__author__ = 'Tom'
import pygame

class Manager(object):

    def __init__(self):
        self._sprites = []
        self._callbacks = {}
        self.group = None

    def add(self, sprite):
        self._sprites.append(sprite)

    def _addCallback(self, type, callback):
        self._callbacks[type] = callback

    def update(self, events):
        for event in events:
            if event.type in self._callbacks.keys():
                self._callbacks[event.type](event)

class ScrollManager(Manager):

    def __init__(self):
        super(ScrollManager,self).__init__()
        self._player = None

    def add(self, sprite):
        super(ScrollManager,self).add(sprite)
        if 'player' in sprite.flags:
            self._player = sprite

    def update(self, events):
        super(ScrollManager,self).update(events)
        if self._player.rect.topleft[0] > 500:
            for sprite in self._sprites:
                sprite.forcex = -2


class MovementManager(Manager):

    def __init__(self):
        super(MovementManager,self).__init__()
        self._addCallback(pygame.KEYDOWN,self._movestart)
        self._addCallback(pygame.KEYUP,self._movestop)
        self._moving = 0

    def update(self, events):
        super(MovementManager,self).update(events)
        for sprite in self._sprites:
            sprite.forcex = self._moving

    def _movestart(self, event):
        if event.key == pygame.K_RIGHT:
            self._moving = 2
        elif event.key == pygame.K_LEFT:
            self._moving = -2
        elif event.key == pygame.K_UP:
            for sprite in self._sprites:
                sprite.forcey = -10

    def _movestop(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self._moving = 0


class FrictionManager(Manager):

    def update(self, events):
        for sprite in self._sprites:
            if sprite.forcex > 0:
                sprite.forcex -= 1
            elif sprite.forcex < 0:
                sprite.forcex += 1
            if sprite.forcey > 0:
                sprite.forcey -= 1
            elif sprite.forcey < 0:
                sprite.forcey += 1
