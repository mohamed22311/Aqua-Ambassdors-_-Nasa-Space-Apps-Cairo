from settings import vertical_tile_number, tile_size, screen_width
import pygame
from tiles import AnimatedTile, StaticTile
from support import import_folder
from random import choice, randint

class Sky:
	def __init__(self,horizon,style = 'level',level = 0):
		self.level = chr(level + 48)
		img = 'graphics/Backgrounds/'+self.level+'/0.png'
		self.img = pygame.image.load(img).convert()
		self.horizon = horizon
		self.style = style

	def draw(self,surface):
		surface.blit(self.img,(0,0))
		
class Water:
	def __init__(self,top,level_width):
		water_start = -screen_width
		water_tile_width = 192
		tile_x_amount = int((level_width + screen_width * 2) / water_tile_width)
		self.water_sprites = pygame.sprite.Group()

		for tile in range(tile_x_amount):
			x = tile * water_tile_width + water_start
			y = top
			sprite = AnimatedTile(192,x,y,'graphics/decoration/water')
			self.water_sprites.add(sprite)

	def draw(self,surface,shift):
		self.water_sprites.update(shift)
		self.water_sprites.draw(surface)

