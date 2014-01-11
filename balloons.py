#!/usr/bin/env python27

from Tkinter import *
import random
import time

SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 500

BALOON_RADIUS = 25
BALOON_DIAMETER = 50

class Bal

class Baloon:
  '''Our funky baloon'''
  def __init__(self, canvas, type=0):
    self.canvas = canvas
    self.id = canvas.create_oval( 0, 0, BALOON_DIAMETER, BALOON_DIAMETER, fill='yellow' )
    self.canvas.move( self.id, random.randrange( SCREEN_WIDTH ), SCREEN_HEIGHT )

  def draw(self):
    self.canvas.move( self.id, 0, -1 )

tk = Tk()
tk.title( 'Pop The Baloons' )
tk.resizable( 0, 0 )
tk.wm_attributes( '-topmost', 1 )
canvas = Canvas( tk, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bd=0, highlightthickness=0 )
canvas.pack()
tk.update()

balloons = []
for x in range(1, 10):
  balloons.append( Baloon( canvas ) )

while 1:
  for baloon in balloons:
    baloon.draw()

  tk.update_idletasks()
  tk.update()
  time.sleep( 0.01 )