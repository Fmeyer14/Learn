import time
while 54: # infinity loob
    a = time.localtime()
    print (a[3],":", a[4],":",a[5]) 
    time.sleep(0.25) # refresh (0.25s)
