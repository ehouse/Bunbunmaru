import sys
import pygame
import engine.Entity

class Enemy( Entity ):
	def __init__( self, xpos, ypos, speed, hp, sprite, hitbox ):
		# position vars
		self.xpos = xpos
		self.ypos = ypos

		# movement vars
		self._speed = speed

		# game vars
		self.destroyed = False
		self.hit = False
		self.hp = hp

		# sprite vars
		self._sprite = sprite
		self.hitbox = hitbox

		def act():
			#TODO add movement code here
			if self.hp <= 0:
				destroyed = True

			if destroyed:
				#TODO place death explosion here
				destroy()

		def draw():
			pass

		def destroy():
			self.xpos = -99
			self.ypos = -99

			self.hitbox = self.hitbox.move( _xSpeed, _ySpeed )
			self.destroyed = True

		def applyHit( bullet ):
			self.hp -= bullet.damageValue
