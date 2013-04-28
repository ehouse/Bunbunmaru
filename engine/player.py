import sys
import pygame
import engine.Entity

class Player( Entity ):
	def __init__( self, xpos, ypos, maxSpeed, sprite, hitbox, item_box ):
		# position vars
		self.xpos = xpos
		self.ypos = ypos

		# movement vars
		self._maxSpeed = maxSpeed
		self._focusedSpeed = maxSpeed /  2
		self._xSpeed = 0
		self._ySpeed = 0

		# sprite vars
		self._sprite = sprite
		self._hitbox = hitbox
		self._item_box = item_box

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
				_ySpeed = -1 * _focusedSpeed
			elif down == True:
				_ySpeed = _focusedSpeed
			else:
				_ySpeed = 0

			if left == True:
				_xSpeed = -1 * _focusedSpeed
			elif right == True:
				_xSpeed = _focusedSpeed
			else:
				_xSpeed = 0
		else:
			if up == True:
				_ySpeed = -1 * _maxSpeed
			elif down == True:
				_ySpeed = _maxSpeed
			else:
				_ySpeed = 0

			if left == True:
				_xSpeed = -1 * _maxSpeed
			elif right == True:
				_xSpeed = _maxSpeed
			else:
				_xSpeed = 0
	pass

	def draw():
		# Rendering code goes here
		pass

	def destroy():
		# Draw explosion
		self.xpos = -99
		self.ypos = -99

	def collidesWith():
		pass

	def _move():
		xpos = xpos + _xSpeed
		ypos = ypos + _ySpeed
