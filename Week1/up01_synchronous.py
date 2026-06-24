from time import sleep, ctime, time

def update_cup_number(customer_name):
    print(f"{ctime()}: LCD : processing for Customer {customer_name}.")
    sleep(1)  # จำลองเวลาที่ใช้ในการอัปเดตหมายเลขถ้วยกาแฟ
    print(f"{ctime()}: LCD : Done for Customer {customer_name}.")
    pass

def make_coffee(customer_name):
    print(f"{ctime()}: Start making coffee for {customer_name}.")
    sleep (1)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"{ctime()}: Coffee Ready for Customer {customer_name}.")
    pass

def main():
    print(f"{ctime()}: === Synchronous Coffee Machine ===")
    start = time()

    for customer_name in ["A", "B", "C"]:
        make_coffee(customer_name)
        update_cup_number(customer_name)
    
    print(f"{ctime()}: Total time: {time() - start:.2f} seconds.")

    pass

if __name__ == "__main__":
    main()