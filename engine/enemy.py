import sys
import pygame
import engine.Entity

class Enemy( Entity ):
	def __init__( self, xpos, ypos, speed, sprite, hitbox ):
		# position vars
		self.xpos = xpos
		self.ypos = ypos

		# movement vars
		self._speed = speed

		# sprite vars
		self._sprite = sprite
		self._hitbox = hitbox

		def act():
			#TODO add movemebt code here
			pass

		def draw():
			pass

		def destroy():
			self.xpos = -99
			self.ypos = -99

			self._hitbox = self._hitbox.move( _xSpeed, _ySpeed )

		def collidesWith():
			pass
