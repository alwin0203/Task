import threading
import time

def show():
    for i in [1,2,3,4]:
        print(i)
t1=threading.Thread(target=show)
t2=threading.Thread(target=show)
t3=threading.Thread(target=show)

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()
