import threading
import asyncio
import time

threadLock = threading.Lock()

global_counter = 0

def increment_counter():
    global global_counter
    with threadLock:
        global_counter += 1

def decrement_counter():
    global global_counter
    with threadLock:
        global_counter -= 1

def get_counter():
    global global_counter
    with threadLock:
        return global_counter

def intensive_processing(value: str):
  cpu_bound()
  # time.sleep(value)
  return value + ' processed'

def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)

def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(11 ** 6))

async def async_executor(sync_func, pool=None):
    eventloop = asyncio.get_event_loop()

    # Create 10 tasks for requests.get synchronous call
    tasks = [
        asyncio.create_task(
            invoke_get_request(eventloop, sync_func, pool)
        ) for _ in range(10)
    ]

    done_tasks, _ = await asyncio.wait(tasks)
    result = [d.result() for d in done_tasks]
    return result[0]

async def invoke_get_request(eventloop: asyncio.AbstractEventLoop, sync_func, pool=None):
    # Wrap requests.get function into a coroutine
    single_result = await eventloop.run_in_executor(
        pool,  # when None we are using the default executor
        sync_func  # each task call invoke_get_request
    )
    return single_result
