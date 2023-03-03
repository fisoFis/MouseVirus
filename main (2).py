from pynput.mouse import Controller
import random

mouse = Controller()

while True:
    r1 = random.randint(-1, 5)
    r2 = random.randint(-1, 5)
    mouse.move(r1, r2)