from time import time, ctime, sleep
import threading

def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer}...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

def customer_private_workflow(customer):
    # Take Order
    print(f"{ctime()} [Thread]-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()} [Thread]-{customer}] Taking Order ...Done!")

    # Do Cooking
    print(f"{ctime()} [Thread]-{customer}] Cooking Spaghetti...")
    sleep(1)
    print(f"{ctime()} [Thread]-{customer}] Cooking Spaghetti...Done!")

    # Mini Bar
    print(f"{ctime()} [Thread]-{customer}] Manage Bar for Drink ...")
    sleep(1)
    print(f"{ctime()} [Thread]-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()} [Thread]-{customer}] all Served!\n")

if __name__ == "__main__":
    start = time()
    customers = ["A", "B", "C"]
    for customer in customers:
        greet_diners(customer)
    print(f"\n{ctime()} --- All Customer greeted. Spilling into individual threads for private workflow ---\n")

    customer_threads = []
    for customer in customers:
        t = threading.Thread(target=customer_private_workflow, args=(customer,))
        customer_threads.append(t)
        t.start()

    for t in customer_threads:
        t.join()

    duration = time() - start
    print(f"{ctime()} Finish Entire restaurant Operation in {duration:.2f} seconds")
