import os
import time
i=5

print('''*******WELCOME TO SASTA SHUTDOWN SYSTEM BY SAURABH*******
\t FOLLOW ME ON instagram - thesupersaurabh''')
while(i>-1):
    if(i==0):
        print("boom.......")
        break
    print(i)
    i-=1
    time.sleep(1)
os.system("shutdown /s /t 1")