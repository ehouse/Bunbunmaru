import sys
import math
import pygame
import engine.entity
import engine.bullet
import engine.player

class BulletManager:
	def __init__ ( self ):
		self._bulletList = []
		self._playerBulletList = []

	def addPlayerBullet( self, bullet ):
		"""
		Adds a bullet that will effect enemies to the bullet manager
		"""
		self._playerBulletList.append( bullet )

	def addEnemyBullet( bullet ):
		"""
		Adds a bullet that will effect the player to the bullet manager
		"""
		self._bulletList.append( self, bullet )

	def drawall( self, screen):
		for bullet in self._bulletList:
			bullet.draw( screen )

		for bullet in self._playerBulletList:
			bullet.draw( screen )

	def _testEnemyBulletCollision( self ):
		"""
		Tests to see if any of the enemy bullets hit the player. This modifies
		Player.hit to True if there is a hit detected
		"""
		for bullet in self._bulletList:
			if bullet.destroyed:
				self._bulletList.remove( self, bullet )
			elif bullet.collidesWith( self, player ):
				player.hit = True
				bullet.hit = True
				break # if the player is hit once, no point in checking others

	def _testPlayerBulletCollision( self, entity ):
		"""
		Tests if the player's bullets have collided with any enemies. This also
		applys the hits to enemies as needed.

		Parameters: Enemy->entity
		Returns: None
		"""
		for bullet in self._playerBulletList:
			if bullet.destroyed:
				self._playerBulletList.remove( bullet )
			elif bullet.collidesWith( entity ):
				entity.applyHit( bullet )
				distance = math.sqrt( math.pow( entity.xpos + bullet.xpos, 2) - \
								math.pow( entity.ypos + bullet.xpos, 2 ))
				if distance < 100:
					entity.heat += ( 100 - distance ) / 10

	def update( self, enemies ):
		"""
		Updates the posision of each bullet and checks for collisions
		"""
		for bullet in self._bulletList:
			bullet.act()

		for enemy in enemies.enemyList:
			self._testPlayerBulletCollision( enemy )

		for bullet in self._playerBulletList:
			bullet.act()

		self._testEnemyBulletCollision()
