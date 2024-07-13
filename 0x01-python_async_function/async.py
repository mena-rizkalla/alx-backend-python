#!/usr/bin/env python3

import asyncio

async def hello_world1(name):
    await asyncio.sleep(5)  # Simulate some asynchronous work
    print(f"Hello, {name}!")

async def hello_world2(name):
    await asyncio.sleep(1)  # Simulate some asynchronous work
    print(f"Hello, {name}!")

async def main():
    print("start")
    task1 = asyncio.create_task(hello_world1("Alice"))
    task2 = asyncio.create_task(hello_world2("Bob"))
    await task1  # Wait for the first task (optional)
    await task2  # Wait for the second task (optional)
    print("finished")

asyncio.run(main())  # This line manages the event loop and task schedulingi
