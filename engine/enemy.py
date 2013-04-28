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

		self._hitbox.move_ip( xpos, ypos )

		# sprite vars

	def act( self ):
		#TODO add movement code here
		if self.hp <= 0:
			self.destroyed = True

		if self.destroyed:
			#TODO place death explosion here
			self.destroy()

	def draw( self, screen ):
		screen.blit(self._sprite, self._hitbox)

	def destroy( self ):
		print "destroy"
		self.xpos = -99
		self.ypos = -99

		self.hitbox = self._hitbox.move_ip( -99, -99 )
		self.destroyed = True

	def applyHit( self, bullet ):
		print self.hp
		self.hp -= bullet.damageValue
		self.heat += 20
