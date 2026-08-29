import time
import asyncio


# --------------------
# Synchronous version
# --------------------

def sync_task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")


def run_sync():
    start = time.time()

    sync_task("Task 1")
    sync_task("Task 2")
    sync_task("Task 3")

    end = time.time()

    print(f"\nSync time: {end - start:.2f} seconds")


# --------------------
# Asynchronous version
# --------------------

async def async_task(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} finished")


async def run_async():
    start = time.time()

    await asyncio.gather(
        async_task("Task 1"),
        async_task("Task 2"),
        async_task("Task 3")
    )

    end = time.time()

    print(f"\nAsync time: {end - start:.2f} seconds")


# --------------------
# Run both
# --------------------

run_sync()

asyncio.run(run_async())