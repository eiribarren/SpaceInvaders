#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 640
HEIGHT = 480

# --------------------------------------------------------------------- 
# Clases
# ---------------------------------------------------------------------
class elemento(pygame.sprite.Sprite):
	def __init__(self,imagen,transp,posx,posy,velx,vely):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image(imagen, transp)
		self.rect = self.image.get_rect()
		self.rect.centerx = posx
		self.rect.centery = posy
		self.speed = [velx, vely]

# ---------------------------------------------------------------------
# Funciones generales
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
		try: image = pygame.image.load(filename)
		except pygame.error, message:
				raise SystemExit, message
		image = image.convert()
		if transparent:
				color = image.get_at((0,0))
				image.set_colorkey(color, RLEACCEL)
		return image
		
def texto(texto, fuente, posx, posy, color):
	salida = pygame.font.Font.render(fuente, texto, 1, color)
	salida_rect = salida.get_rect()
	salida_rect.centerx = posx
	salida_rect.centery = posy
	return salida, salida_rect

# ---------------------------------------------------------------------
# Funciones del juego
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Programa Principal
# --------------------------------------------------------------------- 
def main():
# Inicializaciones pygame
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Space Invaders")
	background_image = load_image('images/fondo_espacio.jpg')
	
# Inicializaciones elementos de juego

	clock = pygame.time.Clock()

	while True:
		time = clock.tick(60)
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
# Procesamos jugador

# Procesamos ia
		
# Actualizamos estado de la partida
		
# Renderizamos
		screen.blit(background_image, (0, 0))
		pygame.display.flip()
	return 0
 
if __name__ == '__main__':
	pygame.init()
	main()
