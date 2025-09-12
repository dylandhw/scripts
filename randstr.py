import random 
import string 
import time 
from termcolor import colored, cprint 

length = 75
for i in range(1000000000):
    chars = string.ascii_letters + string.digits 
    randstr = ''.join(random.choices(chars, k=length))    
    for i in range(len(randstr)):
        time.sleep(0.01)
        x = random.randint(0, 255)
        y = random.randint(0, 255)
        z = random.randint(0, 255)
        cprint(randstr, (x, y, z))