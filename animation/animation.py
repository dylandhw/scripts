import os
import time 
import random
from termcolor import colored, cprint 
import frames 

red_color = (
    (136, 8, 8),
    (170,74, 68),
    (165, 42, 42),
    (128, 0, 32),
    (139, 0, 0),
    (165, 42, 42)
)

def animate(delay=0.5, loop=True):
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            cprint(random.choice(frames.hal9000), random.choice(red_color))
            time.sleep(delay)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("animation interrupted")

animate()