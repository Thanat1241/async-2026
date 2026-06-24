from time import sleep, ctime, time
import os
import threading

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คนแบบซิงโครนัส
def make_coffee(customer_name):
    pass

def main():
    queue = ["Alice", "Bob", "Charlie", "David", "Eve"]
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print (f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] จำลองระบบทำกาแฟแบบซิงโครนัส")    

if __name__ == "__main__":
    main()
    