import asyncio
import random

async def wait_random(max_delay = 10):
    rand_val = random.uniform(0, max_delay)
    await asyncio.sleep(rand_val)
    return rand_val
