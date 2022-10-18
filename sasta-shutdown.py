import os
import time
i=5

print('''*******WELCOME TO SASTA SHUTDOWN SYSTEM BY SAURABH*******
\t FOLLOW ME ON instagram - thesupersaurabh''')
while(i>-2):
    if(i==0):
        print("boom.......")
        time.sleep(1)
    elif(i==-1):
        os.system("shutdown /s /t 1")
    else:
        print(i)
        time.sleep(1)
    i-=1