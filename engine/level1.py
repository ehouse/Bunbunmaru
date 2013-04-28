import sys
import pygame
import engine.Player
import engine.Enemy

class Level1:
	def __init__ ( self )
		self.enemyGroupList = []
		self.currentEnemyGroup = 0
		self.backgroundImage = None #TODO load background image here

	def draw():
		#TODO draw the background

	def getCurrentEnemies()
		"""
		Gets the current group of enemies for the level
		"""
		return enemyGroupList[0]

	def isComplete():
		"""
		Checks to see if all enemy grops have acted yet
		Returns: Boolean->True if all enemies are done, otherwise false
		"""
		for e in enemyGroupList:
			if not e.isDone()
				return False
		return True

