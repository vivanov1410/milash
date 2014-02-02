#!/usr/bin/python

import sys, random
import pygame, pygame.mixer
from pygame.locals import *
import euclid

TOTAL_BALLOON_TYPES = 7
TOTAL_OF_BALLOONS = 20
FPS_RATE = 60
INITIAL_VELOCITY = 1

gravity = euclid.Vector2( 0.0, 80.0 )

class Background:
  """Funky background class"""
  def __init__(self, screen):
    self.screen = screen
    self.set_random_color()
    self.target_color = 'red'

  def set_random_color(self):
    self.red = random.randrange( 255 )
    self.green = random.randrange( 255 )
    self.blue = random.randrange( 255 )

  def get_color(self):
    return ( self.red, self.green, self.blue )

  def draw(self):
    self.screen.fill( self.get_color() )

class Balloon():
  """docstring for Baloon"""
  def __init__(self, screen, position):
    self.screen = screen
    self.position = position
    self.velocity = euclid.Vector2( 0, -1 )
    self.image = random.choice( balloon_images )
    self.tick = 0

  def draw(self):
    x, y = self.position.x, self.position.y
    self.screen.blit( self.image, ( x, y ) )

  def update(self, dtime):
    self.position += self.velocity * INITIAL_VELOCITY

  def get_position(self):
    return ( int( self.position.x ), int( self.position.y ) )




pygame.init()

screen_size = width, height = 600, 400
fps_clock = pygame.time.Clock()

# set up music
pygame.mixer.music.load( 'music/main.mp3' )
pygame.mixer.music.play()

# load sounds
pop_sounds = [
  pygame.mixer.Sound( 'sounds/balloon-pop01.wav' ),
  pygame.mixer.Sound( 'sounds/balloon-pop02.wav' ),
  pygame.mixer.Sound( 'sounds/balloon-pop03.wav' )
]

# load images
balloon_images = [
  pygame.image.load( 'images/balloon-yellow.png' ),
  pygame.image.load( 'images/balloon-blue.png' ),
  pygame.image.load( 'images/balloon-green.png' ),
  pygame.image.load( 'images/balloon-orange.png' ),
  pygame.image.load( 'images/balloon-pink.png' ),
  pygame.image.load( 'images/balloon-purple.png' ),
  pygame.image.load( 'images/balloon-red.png' )
]

# set up background
screen = pygame.display.set_mode( screen_size )
background = Background( screen )

balloons = []
for x in range( 0, TOTAL_OF_BALLOONS ):
  balloons.append( Balloon( screen, euclid.Vector2( random.randrange( screen_size[0] ), screen_size[1] ) ) )

# game loop
# pygame.mouse.get_pos()
game_running = True
while game_running:
  # limit framerate
  dtime_ms = fps_clock.tick( FPS_RATE )
  dtime = dtime_ms / 1000  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_running = False
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
      game_running = False
    elif event.type == MOUSEBUTTONDOWN:
      sound = random.choice( pop_sounds )
      sound.play()
  
  background.draw()

  for balloon in balloons:
    balloon.update( dtime )
    balloon.draw()

  pygame.display.flip()

# quit game
pygame.quit()
sys.exit()