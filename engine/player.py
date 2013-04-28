import sys
import pygame
from pygame import Rect
from pygame.locals import *
from engine.entity import Entity

class Player( Entity ):
	def __init__( self, lives, score, maxSpeed, sprite, viewBox ):
		# position vars
		self.SPAWN_X = 300
		self.SPAWN_Y = 600
		self.xpos = self.SPAWN_X
		self.ypos = self.SPAWN_Y
		Entity.__init__( self, 400 , 300, sprite, Rect( self.xpos - 10,
							self.ypos - 10, self.xpos + 54, self.ypos + 54 ) )

		# movement vars
		self._maxSpeed = maxSpeed
		self._focusedSpeed = maxSpeed /  2
		self._xSpeed = 0
		self._ySpeed = 0

		# Game vars
		self.lives = lives
		self.score = score
		self.invincible = False
		self.invincibilityTime = 5000

		# sprite vars
		self._itemBox = Rect( self.xpos, self.ypos, self.xpos + 64,
									self.ypos + 64 )
		self._viewBox = viewBox

	def act( self ):
		"""
		Handles movement and other actions for the player
		"""

		#TODO possibly think of a more elegant way to handle this
		focused = False
		up = False
		down = False
		left = False
		right = False
		focus = False
		fire = False
		bomb = False

		if pygame.key.get_focused():
			keys = pygame.key.get_pressed()
			up = keys[K_UP]
			down = keys[K_DOWN]
			right = keys[K_RIGHT]
			left = keys[K_LEFT]
			focus = keys[K_LSHIFT]
			fire = keys[K_z]
			bomb = keys[K_x]
		# Get if focused here
		if focused == True:
			if up == True:
				self._ySpeed = -1 * self._focusedSpeed
			elif down == True:
				self._ySpeed = self._focusedSpeed
			else:
				self._ySpeed = 0

			if left == True:
				self._xSpeed = -1 * self._focusedSpeed
			elif right == True:
				self._xSpeed = self._focusedSpeed
			else:
				self._xSpeed = 0
		else:
			if up == True:
				self._ySpeed = -1 * self._maxSpeed
			elif down == True:
				self._ySpeed = self._maxSpeed
			else:
				self._ySpeed = 0

			if left == True:
				self._xSpeed = -1 * self._maxSpeed
			elif right == True:
				self._xSpeed = self._maxSpeed
			else:
				self._xSpeed = 0

		#TODO invincibility timer

	def draw( self, screen ):
		screen.blit(self._sprite,(self._viewBox))

	def destroy( self ):
		"""
		Moves the player off screen temporally, then respawns them at the starting position
		"""
		#TODO Draw explosion
		self.xpos = -99
		self.ypos = -99

		self.hitbox = self.hitbox.move( self._xSpeed, self._ySpeed )
		self._itemBox = self._itemBox.move( self._xSpeed, self._ySpeed )

	def collidesWith( self ):
		pass

	def spawn( self ):
		self.xpos = self.SPAWN_X
		self.ypos = self.SPAWN_Y
		self.invincible = True

	def _move( self ):
		"""
		Moves the player based off of the xSpeed and YSpeed
		"""
		self.xpos = self.xpos + self._xSpeed
		self.ypos = self.ypos + self._ySpeed

		self.hitbox = self.hitbox.move( self._xSpeed, self._ySpeed )
		self._itemBox = self._itemBox.move( self._xSpeed, self._ySpeed )
