#!/usr/bin/python

import sys
import subprocess
import tkinter as tk
from  Particle import Particle
from math import sin,cos,pi,sqrt
from TkDisplay import TkDisplay
from PygletDisplay import PygletDisplay
from Colour import Colour
if sys.argv[1] == 'tk':
    tk_display = TkDisplay()
    tk_display.add(Particle(32, (100,100), (150, 140), Colour(1,1,0)))

    tk_display.go()
elif sys.argv[1] == 'pyglet':
    pyglet_display = PygletDisplay()
    pyglet_display.add(Particle(32, (100,100), (150, 140), Colour(1,1,0)))
    pyglet_display.go()
