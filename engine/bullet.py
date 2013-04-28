import sys
import pygame
import engine.Entity

class Bullet( Entity ):
	def __init__ ( self, xpos, ypos, speed, damageValue, sprite, hitbox ):
		self.xpos = xpos
		self.ypos = ypos
		self._speed = _speed
		self.damageValue = damageValue
		self._sprite = sprite
		self.hitbox = hitbox

	def act():
		self.ypos -= _speed
		self.hitbox = self.hitbox.move( 0 , __speed )

	def collidesWith( entity ):
		if self.hitbox.colliderect( entity.hitbox ):
			return True
		return False

	def draw():
		#TODO write draw
		pass
