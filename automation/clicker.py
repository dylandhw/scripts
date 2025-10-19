import pyautogui as pag
import time as t
import keyboard

clicks = 0
while True:
    if keyboard.is_pressed == 'esc':
        print(">> exit <<")
        break
    pag.click()
    clicks += 1
    t.sleep(10)
