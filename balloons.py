#!/usr/bin/env python27

from Tkinter import *
import random
import time

class Baloon:

  def __init__(self, arg):
    super(Baloon, self).__init__()
    self.arg = arg


tk = Tk()
tk.title( 'Pop The Baloons' )
tk.resizable( 0, 0 )
tk.wm_attributes( '-topmost', 1 )
canvas = Canvas( tk, width=500, height=500, bd=0, highlightthickness=0 )
canvas.pack()
tk.update()
tk.mainloop()