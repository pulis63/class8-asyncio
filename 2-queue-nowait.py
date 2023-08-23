from random import random 
import time
import asyncio

# coroutine to generate work 
async def producer (queue): 
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
    await queue.put (None) 
    print (f'{time.ctime()} Producer: Done')

# coroutine to consume work 
async def consumer(queue):
    print('Consumer: Running')
    #consume work
    while True:
        # get a unit of work without blocking 
        try:
            item = queue.get_nowait() 
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waiting a while...') 
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print (f'{time.ctime()} >got {item}')
    # all done
    print (f'{time.ctime()} Consumer: Done')

# entry point coroutine 
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers 
    await asyncio.gather (producer(queue), consumer(queue))
# start the asyncio program 
asyncio.run(main())

Producer: Running
Consumer: Running
# Wed Aug 23 14:51:47 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:48 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:48 2023 >got 0.5026435716489273
# Wed Aug 23 14:51:48 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:49 2023 >got 0.8620156812396227
# Wed Aug 23 14:51:49 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:49 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:50 2023 >got 0.7528467995209225
# Wed Aug 23 14:51:50 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:50 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:51 2023 >got 0.9119429882813137
# Wed Aug 23 14:51:51 2023 >got 0.013617680844891455
# Wed Aug 23 14:51:51 2023 >got 0.30104727308704593
# Wed Aug 23 14:51:51 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:51 2023 >got 0.45707196374445747
# Wed Aug 23 14:51:51 2023 >got 0.027730359366579527
# Wed Aug 23 14:51:51 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:52 2023 >got 0.627214924110426
# Wed Aug 23 14:51:52 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:52 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:51:53 2023 Producer: Done
# Wed Aug 23 14:51:53 2023 >got 0.8340330617303351
# Wed Aug 23 14:51:53 2023 Consumer: Done