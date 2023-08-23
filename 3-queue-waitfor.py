import asyncio
import time
from random import random

# Coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()  
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue  
        await queue.put(value)  
    # send an all done signal
    await queue.put(None)  
    print(f'{time.ctime()} Producer: Done')

# consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waiting...')
            continue
        # Check for stop
        if item is None:
            break
        # report  
        print(f'{time.ctime()} > got {item}')  
    print('Consumer: Done')

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# Start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:52:31 2023 Consumer: Running
# Wed Aug 23 14:52:31 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:32 2023 > got 0.9892718607463163
# Wed Aug 23 14:52:32 2023 > got 0.4517360450757967
# Wed Aug 23 14:52:33 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:33 2023 > got 0.8064267518449686
# Wed Aug 23 14:52:34 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:34 2023 > got 0.7159957190516911
# Wed Aug 23 14:52:34 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:35 2023 > got 0.8701119214394389
# Wed Aug 23 14:52:35 2023 > got 0.01318643148619636
# Wed Aug 23 14:52:35 2023 > got 0.19229481652723857
# Wed Aug 23 14:52:35 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:35 2023 > got 0.6174582638036304
# Wed Aug 23 14:52:36 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:36 2023 > got 0.8230935094627067
# Wed Aug 23 14:52:36 2023 Producer: Done
# Wed Aug 23 14:52:36 2023 > got 0.03312374327931811
# Consumer: Done