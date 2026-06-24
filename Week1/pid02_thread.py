from time import sleep, ctime, time
import threading
import os

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [Thread ID: {thread_id}] [Thread Name: {thread_name}] Start making coffee for {customer_name}.")
    sleep(5)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"{ctime()} | [PID: {pid}] [Thread ID: {thread_id}] [Thread Name: {thread_name}] Customer {customer_name} ready to be served.")

def main():
    # คิวลูกค้า
    customers = ["Alice", "Bob", "Charlie", "David", "Eve"]
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id
    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] จำลองระบบทำกาแฟแบบมัลติเทรดดิ้ง")
    pass

if __name__ == "__main__":
    main()