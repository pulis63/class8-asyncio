from random import random
import asyncio 
import time

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
    print (f'{time.ctime()} Producer: Done')

# coroutine to consume work 
async def consumer(queue):
    print (f'{time.ctime()} Consumer: Running') 
    # consume work 
    while True:
        # get a unit of work.
        item = await queue.get()
        # report 
        print (f'{time.ctime()} >got {item}') 
        # block while processing
        if item:
            await asyncio.sleep(item) 
            # mark the task as done 
            queue.task_done()
# entry point coroutine 
async def main():
    # create the shared queue 
    queue =asyncio.Queue()
    #  start the consumer
    _ = asyncio.create_task(consumer(queue)) 
    # start the producer and wait for it to finish 
    await asyncio.create_task(producer(queue)) 
    #wait for all items to be processed 
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:54:28 2023 Consumer: Running
# Wed Aug 23 14:54:28 2023 Producer: Running
# Wed Aug 23 14:54:28 2023 >got 0.5794927947213467
# Wed Aug 23 14:54:29 2023 >got 0.3981331126559924
# Wed Aug 23 14:54:29 2023 >got 0.2326718344588823
# Wed Aug 23 14:54:29 2023 >got 0.29132281961281403
# Wed Aug 23 14:54:30 2023 >got 0.7566510070526415
# Wed Aug 23 14:54:31 2023 >got 0.4546194703436127
# Wed Aug 23 14:54:31 2023 >got 0.733983660994221
# Wed Aug 23 14:54:32 2023 >got 0.1088344307765925
# Wed Aug 23 14:54:32 2023 >got 0.2678210512732794
# Wed Aug 23 14:54:32 2023 Producer: Done
# Wed Aug 23 14:54:32 2023 >got 0.6137064065533165