import pyautogui as pag
import random
import time

while True:
    x = random.randint(70,3200)
    y = random.randint(450,1850)
    pag.moveTo(x,y,0.15)
    print(x,y)
    time.sleep(5)