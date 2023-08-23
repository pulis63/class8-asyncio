# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

import asyncio
import time
from random import random

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()  
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)  

    await queue.put(None)  
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consum work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal  
        if item is None:
            break
        # report  
        print(f'{time.ctime()} > got {item}')  
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:51:08 2023 Producer: Running
# Wed Aug 23 14:51:08 2023 Consumer: Running
# Wed Aug 23 14:51:08 2023 > got 0.8283834752438526
# Wed Aug 23 14:51:09 2023 > got 0.861623322024916
# Wed Aug 23 14:51:10 2023 > got 0.7040228524720534
# Wed Aug 23 14:51:11 2023 > got 0.9576483160549045
# Wed Aug 23 14:51:12 2023 > got 0.6190601040429354
# Wed Aug 23 14:51:12 2023 > got 0.7636066730720549
# Wed Aug 23 14:51:12 2023 > got 0.005034481215830167
# Wed Aug 23 14:51:13 2023 > got 0.91493232105655
# Wed Aug 23 14:51:13 2023 > got 0.01585242433807743
# Wed Aug 23 14:51:14 2023 Producer: Done
# Wed Aug 23 14:51:14 2023 > got 0.9484275258479972
# Wed Aug 23 14:51:14 2023 Consumer: Done