#!/usr/bin/python
#system imports
import os,sys
import pygame
from pygame.locals import *
#local imports
from engine.level1 import Level1
from engine.bulletmanager import BulletManager
from engine.player import Player

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
        self.clock = pygame.time.Clock()
        self.game.display.set_caption('Bunbunmaru Gamejam 2013 | TOPGUN')
        self.clock.tick(60)

        # images
        self.f14 = self._load_png("f14.png")
        self.bullet = self._load_png("bullet.png")

        # level management
        self.level = Level1()
        self.bulletMan = BulletManager()

        # entities
        self.enemies = self.level.getCurrentEnemies()
        self.player = Player( 3, 0, self.bulletMan, 1, self.f14,
                              self.f14.get_rect(), self.bullet,
                              self.bullet.get_rect() )

    def _actall( self ):
         self.player.act()
         self.bulletMan.update( self.enemies )
         for enemy in self.enemies.enemyList:
             enemy.act()

    def _drawall( self ):
        """
        Draws the player, bullets, and enemies (in that order) to the screen
        """
        self.screen.fill((135,206,250))
        self.player.draw(self.screen)
        for enemy in self.enemies.enemyList:
            enemy.draw()
        self.bulletMan.drawall()
        pygame.display.flip()

    def _load_png( self, name):
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

    def start(self):
        """
            Entry point of the game
        """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # check if current wave is done, if it is, get new enemies
            if self.level.isComplete():
                self.enemies = self.level.getCurrentEnemies()
            self._actall()
            self._drawall()
            #TODO add 'tick' stablizer

if __name__ == "__main__":
    bun = GameLoop()
    bun.start()
