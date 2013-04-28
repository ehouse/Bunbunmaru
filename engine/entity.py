import sys
import pygame

class Entity:
	def __init__( self, xpos, ypos, sprite, hitbox ):
		self.xpos = xpos
		self.ypos = ypos
		self._sprite = sprite
		self._hitbox = hitbox

	def act( self ):
		"""
		Handles movement for the entity

		Parameters: null
		Returns: null
		"""
		pass

	def draw( self ):
		"""
		Handles drawing for the entity
		"""
		pass

	def destroy( self ):
		"""
		Handles removal from the gameboard for the entity
		"""
		self.xpos = -99
		self.ypos = -99

		self._hitbox = self._hitbox.move( _xSpeed, _ySpeed )
		self.destroyed = True

	def collidesWith( self, other ):
		"""
		Tests if the entity collides with another entity
		"""
		pass
