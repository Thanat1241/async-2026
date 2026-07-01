# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for Customer {customer}...")
    await asyncio.sleep(1)  # Simulate a delay in cooking
    print(f"{ctime()} -> Finished cooking for Customer {customer}!")

async def main():
    start = time()
    # Create tasks for each customer
    task_a = asyncio.create_task(cook_spaghetti("A"))
    task_b = asyncio.create_task(cook_spaghetti("B"))

    print(f"{ctime()} -> Main program can do other work while Tasks A and B run in the background.")
    # Wait for both tasks to complete
    await task_a
    await task_b

    print(f"Total Operation time: {time() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine