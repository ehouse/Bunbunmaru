import sys
import pygame
import engine.Entity
import engine.Bullet
import engine.Player

class BulletManager:
	def __init__ ( self ):
		self._bulletList = []
		self._playerBulletList = []

	def testEnemyBulletCollision():
		"""
		Tests to see if any of the enemy bullets hit the player. This modifies Player.hit to True if there is a hit detected
		"""
		for bullet in self._bulletList:
			if bullet.collidesWith( player ):
				player.hit = True
				bullet.hit = True

	def testPlayerBulletCollision( entity ):
		"""
		Tests if the player's bullets have collided with any enemies. This also applys the hits to enemies as needed.

		Parameters: Enemy->entity
		Returns: None
		"""
		for bullet in self._playerBulletList:
			if bullet.collidesWith( entity ):
				entity.applyHit( bullet )
