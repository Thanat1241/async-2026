
from time import time, ctime, sleep

def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer}...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

def take_order(customer):
    print(f"{ctime()} Taking Order for Customer-{customer}...")
    sleep(1)
    print(f"{ctime()} Taking Order for Customer-{customer} ...Done!")

def do_cooking(customer):
    print(f"{ctime()} Cooking for Customer-{customer}...")
    sleep(1)
    print(f"{ctime()} Cooking for Customer-{customer} ...Done!")

def mini_bar(customer):
    print(f"{ctime()} Mini Bar for Customer-{customer}...")
    sleep(1)
    print(f"{ctime()} Mini Bar for Customer-{customer} ...Done!")

if __name__ == "__main__":
    start = time()
    for customer in ["A", "B", "C"]:
        greet_diners(customer)
        take_order(customer)
        do_cooking(customer)
        mini_bar(customer)
    
    duration = time() - start
    print(f"{ctime()} Finish Cooking in {duration:.2f} seconds")
