import threading
import time


def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f'{name} completed')
    
start = time.perf_counter()
t1 = threading.Thread(target=task,args=("Task - 1",))
t2 = threading.Thread(target=task,args=("Task - 2",))
t3 = threading.Thread(target=task,args=("Task - 3",))


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()


end = time.perf_counter()
print(f'Total time:{end - start:.2f} secs')




































import threading
balance = 1000


lock = threading.Lock()
def f1_deposit():
    global balance 
    with lock:
        balance = balance + 500
        
def f2_withdraw():
    global balance
    with lock:
        balance = balance - 200
        
t1 = threading.Thread(target=f1_deposit)
t2 = threading.Thread(target=f2_withdraw)


t1.start()
t2.start()


t1.join()
t2.join()


print(f"Balance : {balance}")