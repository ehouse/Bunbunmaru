import sys
import math
import pygame
from pygame import transform
from engine.entity import Entity

class Enemy( Entity ):
	def __init__( self, xpos, ypos, speed, hp, sprite, hitbox ):
		Entity.__init__( self, xpos, ypos, sprite, hitbox )
		# movement vars
		self._speedx = 0
		self._speedy = 0
		self._curAngle = 270
		#self._maxspeed = speed
		self._maxspeed = 2

		# game vars
		self.destroyed = False
		self.hit = False
		self.hp = hp
		self.heat = 0
		self._actcode = 0

		self._hitbox.move_ip( xpos, ypos )

		# sprite vars

	def act( self, player ):
		if self._actcode == 0:
			self._speedy = self._maxspeed
			self._hitbox.move_ip( 0, 1 )
			if self._hitbox.y >= 200:
				self._actcode = 1
		elif self._actcode == 1:
			# fire code goes here
			#angle = math.atan2( self._hitbox.x - player._viewBox.x , self._hitbox.y - player._viewBox.y)
			#angle = math.degrees( angle )
			#if not (self._curAngle  >= angle - 10 and self._curAngle <= angle + 10):
			#	print "rotate", self._curAngle
			#	self._sprite = pygame.transform.rotate( self._sprite, 2 )
			#	self._curAngle += 2
			#	if self._curAngle >= 360:
			#		self._curAngle -= 360
			pass
		if self.hp <= 0:
			self.destroyed = True

		if self.destroyed:
			#TODO place death explosion here
			self.destroy()

	def draw( self, screen ):
		screen.blit(self._sprite, self._hitbox)

	def destroy( self ):
		self.xpos = -99
		self.ypos = -99

		self.hitbox = self._hitbox.move_ip( -999, -999 )
		self.destroyed = True

	def applyHit( self, bullet ):
		self.hp -= bullet.damageValue
		self.heat += 20
