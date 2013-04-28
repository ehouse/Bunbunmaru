import sys
import pygame
from engine.entity import Entity

class Bullet( Entity ):
	def __init__ ( self, xpos, ypos, speed, damageValue, sprite, hitbox ):
		Entity.__init__self( xpos, ypos, sprite, hitbox )
		self._speed = _speed
		self.damageValue = damageValue

	def act( self ):
		self.ypos -= _speed
		self.hitbox = self.hitbox.move( 0 , __speed )

	def collidesWith( slef, entity ):
		if self.hitbox.colliderect( entity.hitbox ):
			return True
		return False

	def draw():
		#TODO write draw
		pass
