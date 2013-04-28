import sys
import pygame
from engine.entity import Entity

class Enemy( Entity ):
	def __init__( self, xpos, ypos, speed, hp, sprite, hitbox ):
		Entity.__init__( self, xpos, ypos, sprite, hitbox )
		# movement vars
		self._speed = speed

		# game vars
		self.destroyed = False
		self.hit = False
		self.hp = hp
		self.heat = 0

		# sprite vars

	def act( self ):
		#TODO add movement code here
		if self.hp <= 0:
			destroyed = True

		if self.destroyed:
			#TODO place death explosion here
			destroy()

	def draw( self ):
		pass

	def destroy():
		self.xpos = -99
		self.ypos = -99

		self.hitbox = self.hitbox.move( _xSpeed, _ySpeed )
		self.destroyed = True

	def applyHit( self, bullet ):
		self.hp -= bullet.damageValue
		self.heat += 20
