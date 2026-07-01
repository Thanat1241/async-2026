from time import time, ctime, sleep
import multiprocessing

def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer}...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

def customer_private_workflow(customer):
    # Take Order
    print(f"{ctime()} [Process]-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()} [Process]-{customer}] Taking Order ...Done!")

    # Do Cooking
    print(f"{ctime()} [Process]-{customer}] Cooking Spaghetti...")
    sleep(1)
    print(f"{ctime()} [Process]-{customer}] Cooking Spaghetti...Done!")

    # Mini Bar
    print(f"{ctime()} [Process]-{customer}] Manage Bar for Drink ...")
    sleep(1)
    print(f"{ctime()} [Process]-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()} [Process]-{customer}] all Served!\n")

if __name__ == "__main__":
    start = time()
    customers = ["A", "B", "C"]
    for customer in customers:
        greet_diners(customer)
    print(f"\n{ctime()} --- All Customer greeted. Spilling into individual processes for private workflow ---\n")

    customer_processes = []
    for customer in customers:
        p = multiprocessing.Process(target=customer_private_workflow, args=(customer,))
        customer_processes.append(p)
        p.start()

    duration = time() - start
    print(f"{ctime()} Finish Entire restaurant Operation in {duration:.2f} seconds")