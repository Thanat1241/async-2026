# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio

async def calculate_bill(customer, base_price):
    print(f"Calculating receipt for {customer}...")
    await asyncio.sleep(1)  # Simulate calculation time
    final_price = base_price * 1.07  # Adding tax
    return final_price

async def main():
    # Create tasks for each customer
    task_a = asyncio.create_task(calculate_bill("A", 100))
    task_b = asyncio.create_task(calculate_bill("B", 200))

    # Wait for both tasks to complete and get their results
    result_a = await task_a
    result_b = await task_b

    print(f"Final bill A: ${result_a:.2f}")
    print(f"Final bill B: ${result_b:.2f}")
    print(f"Combined Total Revenue: ${result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine