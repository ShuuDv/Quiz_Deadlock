import threading
import time

#Membuat objek kunci
kunci1 = threading.Lock()
kunci2 = threading.Lock()

def thread_a():
    kunci1.acquire()
    print("Kunci 1 sudah diambil")
