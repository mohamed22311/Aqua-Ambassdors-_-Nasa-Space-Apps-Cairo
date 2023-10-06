import pygame
from support import import_folder

class ParticleEffect(pygame.sprite.Sprite):
	def __init__(self,pos,type,level):
		super().__init__()
		self.level = chr(level + 48)
		self.frame_index = 0
		self.animation_speed = 0.5
		if type == 'jump':
			self.frames = import_folder('graphics/characters/0/dust_particles/jump')
		if type == 'land':
			self.frames = import_folder('graphics/characters/0/dust_particles/land')
		if type == 'explosion':
			img = 'graphics/enemy/'+self.level+'/explosion/'
			self.frames = import_folder(img)
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center = pos)

	def animate(self):
		self.frame_index += self.animation_speed
		if self.frame_index >= len(self.frames):
			self.kill()
		else:
			self.image = self.frames[int(self.frame_index)]

	def update(self,x_shift):
		self.animate()
		self.rect.x += x_shift
