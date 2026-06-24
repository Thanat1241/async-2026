from time import ctime, time
import asyncio
import os
import threading


async def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: processing for customer {customer_name}...")
    await asyncio.sleep(1.0)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")
    pass

async def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1.0)
    print(f"{ctime()} | Coffee Ready for {customer_name}!")
    await update_cup_number(customer_name)


async def main():
    print(f"{ctime()} | === Asyncio Coffee Machine ===")
    start = time()

    tasks = [make_coffee(customer_name) for customer_name in ["A", "B", "C"]]
    await asyncio.gather(*tasks)

    print(f"{ctime()} | Total time: {time() - start:.2f} seconds.")
    pass

if __name__ == "__main__":
    asyncio.run(main())