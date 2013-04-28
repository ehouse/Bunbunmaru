import sys
import pygame

class Entity:
	def __init__( self, xpos, ypos, sprite, hitbox ):
		self.xpos = xpos
		self.ypos = ypos
		self._sprite = sprite
		self._hitbox = hitbox

	def act():
		"""
		Handles movement for the entity

		Parameters: null
		Returns: null
		"""
		pass

	def draw():
		"""
		Handles drawing for the entity
		"""
		pass

	def destroy():
		"""
		Handles removal from the gameboard for the entity
		"""
		pass

	def collidesWith( other ):
		"""
		Tests if the entity collides with another entity
		"""
		pass
