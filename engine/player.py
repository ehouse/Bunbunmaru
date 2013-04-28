import sys
import pygame

class Player( Entity ):
	def __init__( self, xpos, ypos, sprite, hitbox, item_box )
		self.xpos = xpos
		self.ypos = ypos
		self._sprite = sprite
		self._hitbox = hitbox
		self._item_box = item_box

	def act():
		"""
		Handles movement and other actions for the player
		"""
		# Movement code goes here
	pass

	def draw():
		# Rendering code goes here

	def destroy():
		# Draw explosion
		self.xpos = -99
		self.ypos = -99

	def collidesWith():
		pass
