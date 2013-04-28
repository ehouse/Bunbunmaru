import sys
import pygame
from engine.enemy import Enemy

class EnemyGroup:
	def __init__( self , enemyList, sprite ):
		self.enemyList = enemyList
		self.sprite = sprite

	def act( self ):
		"""
		Updates each enemy in the enemy list
		"""
		for enemy in enemyList:
			enemy.act()

	def draw( self ):
		"""
		Draws each enemy in the enemy list
		"""
		for enemy in enemyList:
			enemy.draw()

	def isDone( self ):
		"""
		Checks if all enemies in the group are destroyed or have finished their pattern
		Returns: Boolean->True if the pattern is done otherwise False
		"""
		done = True

		for enemy in self.enemyList:
			if enemy.destroyed == False:
				done = False
				return done
		return done

