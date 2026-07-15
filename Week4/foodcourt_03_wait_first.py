# foodcourt_03_wait_first.py
import asyncio
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6720301003"
    print(f"{ctime()} | --- [Task 3] Practice using wait to queue multiple orders ---")
    
    # 1. Create a list of tasks for ordering different dishes without awaiting them immediately.
    orders = {
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Mixed"))
    }

    # 2. Use asyncio.wait to run all tasks concurrently and wait for their results.
    done, pending = await asyncio.wait(orders, return_when=asyncio.ALL_COMPLETED)

    fastest_dish = list(done)[0].result()
    print(f"{ctime()} |Winner served dish: Shop: {fastest_dish['shop']}, Menu: {fastest_dish['menu']}")

    print(f"{ctime()} | Cleaning up: Canceling {len(pending)} remaining pending orders...")
    for t in pending:
        t.cancel()

if __name__ == "__main__":
    asyncio.run(main())