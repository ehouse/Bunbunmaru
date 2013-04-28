#!/usr/bin/python
#system imports
import os,sys
import pygame
from pygame.locals import *
#local imports
import engine
import resources

class GameLoop:
    def __init__(self,width=640,height=480):
        self.game = pygame
        self.game.init()
        self.width = width
        self.height = height
        self.screen = self.game.display.set_mode((self.width,self.height))
        self.game.display.set_caption('Bunbunmaru Gamejam 2013')

    def start(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == "__main__":
    bun = GameLoop()
    bun.start()
