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
        """
            Game loop Class
            Accepts game window height and width
        """
        self.game = pygame
        self.game.init()
        self.width = width
        self.height = height
        self.screen = self.game.display.set_mode((self.width,self.height))
        self.game.display.set_caption('Bunbunmaru Gamejam 2013')

    def start(self):
        """
            Entry point of the game
        """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _load_png(name):
        """
            Private Load_png method
            accept: name - file name
            return: pygame image obj
        """
        fullname = os.path.join('resources',name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error:
            print "Cannot load image: ",fullname
        return image


if __name__ == "__main__":
    bun = GameLoop()
    bun.start()
