import threading
import time

# Membuat objek kunci
kunci1 = threading.Lock()
kunci2 = threading.Lock()

def thread_A():

    kunci1.acquire() # thread A mengambil kunci 1
    print("Thread A sukses mengambil kunci 1")

    time.sleep(1)

    # thread A mencoba untuk mengambil kunci 2
    print("Mencoba untuk mengambil kunci 2")
    kunci2.acquire()
    print("Thread A sukses mengambil Kunci 2")

    # melepaskan semua kunci
    kunci2.release()
    kunci1.release()


def thread_B():

  
    kunci2.acquire() # thread A mengambil kunci 2  
    print("thread B sukses mengambil kunci 2")

    time.sleep(1) 

    # thread B mencoba untuk mengambil kunci 1
    print("Thread B mencoba mengambil kunci 1")
    kunci1.acquire()
    print("Thread B sukses mengambil kunci 1")

    # melepaskan semua kunci
    kunci1.release()
    kunci2.release()


t1 = threading.Thread(target=thread_A)
t2 = threading.Thread(target=thread_B)

t1.start()
t2.start()

t1.join()
t2.join()

