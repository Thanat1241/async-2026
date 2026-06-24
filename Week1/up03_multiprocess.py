from time import sleep, ctime, time
import multiprocessing

def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1.0)  # จำลองเวลาที่ใช้ในการอัปเดตหมายเลขถ้วยกาแฟ
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")
    pass

def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep (1.0)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"{ctime()} | Coffee Ready for {customer_name}!")
    update_cup_number(customer_name)
    pass

def main():
    print(f"{ctime()} | === Multi-processing Coffee Machine ===")
    start = time()

    processes = []
    for customer_name in ["A", "B", "C"]:
        p = multiprocessing.Process(target=make_coffee, args=(customer_name,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"{ctime()} | Total time: {time() - start:.2f} seconds.")
if __name__ == "__main__":
    main()