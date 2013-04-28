#!/usr/bin/python
#system imports
import os,sys
import pygame
from pygame.locals import *
#local imports
from engine import *
import resources

class GameLoop:
    def __init__(self,width=640,height=480):
        """
            Game loop Class
            Accepts game window height and width
        """
        # game display vars
        self.game = pygame
        self.game.init()
        self.width = width
        self.height = height
        self.screen = self.game.display.set_mode((self.width,self.height))
        self.game.display.set_caption('Bunbunmaru Gamejam 2013')

        # level management
        self.level = Level1()
        self.bulletMan = BulletManager()

        # entities
        self.enemies = self.level.getCurrentEnemies()
        self.player = player( 3, 0, 5, None )

    def start(self):
        """
            Entry point of the game
        """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # check if current wave is done, if it is, get new enemies
            if level.isComplete():
                enemies = level.getCurrentEnemies()
            actall()
            drawall()
            #TODO add 'tick' stablizer

    def actall():
         player.act()
         self.bulletMan.update( self.enemies )
         for enemy in enemies:
             enemy.act()

    def drawall():
        """
        Draws the player, bullets, and enemies (in that order) to the screen
        """
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.bulletMan.drawall()

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
