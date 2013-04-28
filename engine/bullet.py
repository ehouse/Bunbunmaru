import sys
import pygame
from engine.entity import Entity

class Bullet( Entity ):
	def __init__ ( self, xpos, ypos, speed, damageValue, sprite, hitbox ):
		Entity.__init__( self, xpos, ypos, sprite, hitbox )
		self._speed = speed
		self.damageValue = damageValue
		self.destroyed = False

	def act( self ):
		self.ypos -= self._speed
		self._hitbox = self._hitbox.move( 0 , self._speed )

	def collidesWith( self, entity ):
		if self._hitbox.colliderect( entity._hitbox ):
			return True
		return False

	def draw( self, screen):
		screen.blit( self._sprite, self._hitbox )
