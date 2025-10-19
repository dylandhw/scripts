import pyautogui as pag
import time as t
import random

def clicker():
    clicks = 0
    while True:
        pag.click()
        clicks += 1
        t.sleep(1)

def move():
    while True:
        pag.dragTo(random.randint(0, 1920), random.randint(0, 1080), 100)
        t.sleep(300)


def main():
    clicker()
    move()

if __name__ == "__main__":
    main()
