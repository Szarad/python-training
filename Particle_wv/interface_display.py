#!/usr/bin/python

import sys
import subprocess
import pyglet
import tkinter as tk
from  Particle import Particle
from math import sin,cos,pi,sqrt
from TkinterDisplay import TkinterDisplay
from PygletDisplay import PygletDisplay
if sys.argv[1] == 'tk':
    tk_display = TkinterDisplay()
    tk_display.update(dt)
    tk_display.go()
elif sys.argv[1] == 'pyglet':
    pyglet_display = PygletDisplay()
    pyglet_display.go()
