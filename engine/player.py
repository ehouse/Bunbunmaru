import sys
import pygame
import engine.entity

class Player( Entity ):
	def __init__( self, lives, score, maxSpeed, sprite ):
		# position vars
		self.SPAWN_X = 400
		self.SPAWN_Y = 300
		self.xpos = self.SPAWN_X
		self.ypos = self.SPAWN_Y

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
		self._sprite = sprite
		self.hitbox = rect( self.xpos - 10, self.ypos - 10, self.xpos + 54,
								self.ypos + 54 )
		self._itemBox = rect( self.xpos, self.ypos, self.xpos + 64,
									self.ypos + 64 )

	def act():
		"""
		Handles movement and other actions for the player
		"""

		#TODO possibly think of a more elegant way to handle this
		focused = False
		up = False
		down = False
		left = False
		right = False

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

	def draw():
		#TODO Rendering code goes here
		pass

	def destroy():
		"""
		Moves the player off screen temporally, then respawns them at the starting position
		"""
		#TODO Draw explosion
		self.xpos = -99
		self.ypos = -99

		self.hitbox = self.hitbox.move( self._xSpeed, self._ySpeed )
		self._itemBox = self._itemBox.move( self._xSpeed, self._ySpeed )

	def collidesWith():
		pass

	def spawn():
		self.xpos = self.SPAWN_X
		self.ypos = self.SPAWN_Y
		self.invincible = True

	def _move():
		"""
		Moves the player based off of the xSpeed and YSpeed
		"""
		self.xpos = self.xpos + self._xSpeed
		self.ypos = self.ypos + self._ySpeed

		self.hitbox = self.hitbox.move( self._xSpeed, self._ySpeed )
		self._itemBox = self._itemBox.move( self._xSpeed, self._ySpeed )
