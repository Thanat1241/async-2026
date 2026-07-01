# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def greet():
    print("Hello from the event loop!")


if __name__ == "__main__":
    coro_object = greet()  # Create a coroutine object
    asyncio.run(coro_object)  # Run the event loop to execute the coroutine