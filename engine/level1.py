import sys
from pygame import Rect
from engine.enemygroup import EnemyGroup
from engine.player import Player
from engine.enemy import Enemy

class Level1:
	def __init__( self, enemySprite ):
		self.enemyGroupList = [
			EnemyGroup (
				[ Enemy(100, 100, 1, 100, enemySprite, Rect(0, 0, 64, 64 )) ], enemySprite
			)
		]
		self.currentEnemyGroup = 0
		self.backgroundImage = None #TODO load background image here

	def draw():
		#TODO draw the background
		pass

	def getCurrentEnemies( self ):
		"""
		Gets the current group of enemies for the level
		Returns: EnemyGroup->The current enemy group
		"""
		print self.currentEnemyGroup
		if self.currentEnemyGroup > 0:
			return None
		else:
			return self.enemyGroupList[self.currentEnemyGroup]

	def isComplete( self ):
		"""
		Checks to see if all enemy grops have acted yet
		Returns: Boolean->True if all enemies are done, otherwise false
		"""
		for e in self.enemyGroupList:
			if not e.isDone():
				return False
		self.currentEnemyGroup+=1
		return True

