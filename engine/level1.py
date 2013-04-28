import sys
import pygame
import engine.Player
import engine.Enemy

class Level1:
	def __init__ ( self ):
		# We'll create a bs enemy here
		self.enemyGroupList = [
			EnemyGroup [
				Enemy( 0, 0, 5, 10, None, rect( 0, 0, 64, 64 )),
				Enemy( 100, 0, 5, 100, None, rect( 100, 0, 64, 64 ))
			]
		]
		self.currentEnemyGroup = 0
		self.backgroundImage = None #TODO load background image here

	def draw():
		#TODO draw the background
		pass

	def getCurrentEnemies():
		"""
		Gets the current group of enemies for the level
		Returns: EnemyGroup->The current enemy group
		"""
		return enemyGroupList[0]

	def isComplete():
		"""
		Checks to see if all enemy grops have acted yet
		Returns: Boolean->True if all enemies are done, otherwise false
		"""
		for e in enemyGroupList:
			if not e.isDone():
				return False
		self.currentEnemyGroup+=1
		return True

