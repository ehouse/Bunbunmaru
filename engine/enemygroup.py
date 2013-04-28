import sys
import pygame
import engine.Enemy

class EnemyGroup:
	def init__( self, enemylist )
		self.enemyList = enemylist

	def act():
		"""
		Updates each enemy in the enemy list
		"""
		for enemy in enemyList:
			enemy.act()

	def draw():
		"""
		Draws each enemy in the enemy list
		"""
		for enemy in enemyList:
			enemy.draw()

	def isDone():
	"""
	Checks if all enemies in the group are destroyed or have finished their pattern
	Returns: Boolean->True if the pattern is done otherwise False
	"""
		done = True

		for enemy in enemyList:
			if enemy.destroyed == False:
				done = False
				return done
		return done

