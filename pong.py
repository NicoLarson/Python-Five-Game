# Pong in Python 3

import turtle

wm = turtle.Screen()
wm.title("Pong by @NicoLarson")
wm.bgcolor("black")
wm.setup(width=800, height=600)
wm.tracer(0)
# Main game loop
while True:
    wm.update()
