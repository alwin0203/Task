import threading
import time

def show():
    for i in [1,2,3,4]:
        print(i)
t1=threading.Thread(target=show)
t2=threading.Thread(target=show)
t3=threading.Thread(target=show)

t1.start()
t2.start()
t3.start()
