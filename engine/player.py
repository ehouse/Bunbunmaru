import sys
import pygame
from pygame import Rect
from pygame.locals import *
from engine.entity import Entity
from engine.bullet import Bullet

class Player( Entity ):
	def __init__( self, lives, score, bulletMan, maxSpeed, sprite, viewBox, bulletSprite, bulletBox ):
		# position vars
		self.SPAWN_X = 300
		self.SPAWN_Y = 600
		self.xpos = self.SPAWN_X
		self.ypos = self.SPAWN_Y
		Entity.__init__( self, 400 , 300, sprite, Rect( self.xpos - 10,
							self.ypos - 10, self.xpos + 54, self.ypos + 54 ) )

		# movement vars
		self._maxSpeed = maxSpeed
		self._focusedSpeed = maxSpeed /  2.0
		self._xSpeed = 0
		self._ySpeed = 0

		# Game vars
		self.lives = lives
		self.score = score
		self.invincible = False
		self._invincibilityTime = 5000
		self._bulletMan = bulletMan

		# sprite vars
		self._itemBox = Rect( self.xpos, self.ypos, self.xpos + 64,
									self.ypos + 64 )
		self._viewBox = viewBox
		self._bulletSprite = bulletSprite
		self._bulletBox = bulletBox

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

		if fire:
			self._fire()

		self._move()

		#TODO invincibility timer

	def _fire( self ):
		bullet = Bullet( self.xpos, self.ypos, -5, 5, self._bulletSprite,
						self._bulletSprite.get_rect())
		xpos = self._viewBox.x
		ypos = self._viewBox.y
		bullet._hitbox.move_ip(xpos, ypos)
		self._bulletMan.addPlayerBullet( bullet )
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

		self._viewBox = self._viewBox.move( self._xSpeed, self._ySpeed)

		self._hitbox = self._hitbox.move( self._xSpeed, self._ySpeed )
		self._itemBox = self._itemBox.move( self._xSpeed, self._ySpeed )
