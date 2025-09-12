import random 
import string 
import time 

length = 32 
for i in range(1):
    chars = string.ascii_letters + string.digits 
    randstr = ''.join(random.choices(chars, k=length))    
    for i in range(len(randstr)):
        time.sleep(0.1)
        print(randstr[i])