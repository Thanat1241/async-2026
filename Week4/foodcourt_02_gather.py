# foodcourt_02_gather.py
import asyncio
from time import ctime
from unittest import result
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6720301003"
    print(f"{ctime()} | --- [Task 2] Practice using gather to queue multiple orders ---")
    start_time = ctime()
    
    # 1. Create a list of tasks for ordering different dishes without awaiting them immediately.
    t1 = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Mixed"))
    t2 = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles"))
    t3 = asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak"))

    # 2. Use asyncio.gather to run all tasks concurrently and wait for their results.
    results = await asyncio.gather(t1, t2, t3)
    
    # 3. Print the results of all orders once they are completed.
    for dish in results:
        print(f"{ctime()} | System Response: {dish}")

if __name__ == "__main__":
    asyncio.run(main())