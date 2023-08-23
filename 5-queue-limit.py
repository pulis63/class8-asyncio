from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue,id):
    print(f'{time.ctime()} Producer {id}: Running')
     # generate work
    for i in range(10):
         # generate a value
        value = random() 
        # block to simulate work
        await asyncio.sleep(id*0.1)
        # add to the queue, may block  
        await queue.put(value)  
    print(f'{time.ctime()} Producer {id}: Done')

# coroutine to 
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
            # mark as completed
            queue.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue,_+1) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for the consumer to process all items
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:56:02 2023 Consumer: Running
# Wed Aug 23 14:56:02 2023 Producer: Running
# Wed Aug 23 14:56:02 2023 Producer: Running
# Wed Aug 23 14:56:02 2023 Producer: Running
# Wed Aug 23 14:56:02 2023 Producer: Running
# Wed Aug 23 14:56:02 2023 Producer: Running
# Wed Aug 23 14:56:02 2023 > got 0.12198023438721384
# Wed Aug 23 14:56:02 2023 > got 0.20666391801132145
# Wed Aug 23 14:56:03 2023 > got 0.1254691917428955
# Wed Aug 23 14:56:03 2023 > got 0.019060728036448316
# Wed Aug 23 14:56:03 2023 > got 0.3437322856431798
# Wed Aug 23 14:56:03 2023 > got 0.6028791404819
# Wed Aug 23 14:56:04 2023 > got 0.1314573949075668
# Wed Aug 23 14:56:04 2023 > got 0.7778583581660734
# Wed Aug 23 14:56:05 2023 > got 0.28957251730114697
# Wed Aug 23 14:56:05 2023 > got 0.3994821043426575
# Wed Aug 23 14:56:05 2023 > got 0.07529340929993
# Wed Aug 23 14:56:06 2023 > got 0.6362083373223365
# Wed Aug 23 14:56:06 2023 > got 0.7762540702637122
# Wed Aug 23 14:56:07 2023 > got 0.3158741021264464
# Wed Aug 23 14:56:07 2023 > got 0.27946179467474763
# Wed Aug 23 14:56:08 2023 > got 0.06018682818995513
# Wed Aug 23 14:56:08 2023 > got 0.3866359300076606
# Wed Aug 23 14:56:08 2023 > got 0.24446970474883756
# Wed Aug 23 14:56:08 2023 > got 0.4288049459388753
# Wed Aug 23 14:56:09 2023 > got 0.026687361660233333
# Wed Aug 23 14:56:09 2023 > got 0.16487913356485429
# Wed Aug 23 14:56:09 2023 > got 0.8646547546866372
# Wed Aug 23 14:56:10 2023 > got 0.7876381426519377
# Wed Aug 23 14:56:11 2023 > got 0.4589150934217664
# Wed Aug 23 14:56:11 2023 > got 0.2413952361524423
# Wed Aug 23 14:56:11 2023 > got 0.0949268784066074
# Wed Aug 23 14:56:11 2023 > got 0.12341927378000739
# Wed Aug 23 14:56:12 2023 > got 0.6025620272128271
# Wed Aug 23 14:56:12 2023 > got 0.5017259792413159
# Wed Aug 23 14:56:13 2023 > got 0.8515108895211161
# Wed Aug 23 14:56:14 2023 > got 0.17331012765956033
# Wed Aug 23 14:56:14 2023 > got 0.6690714103732036
# Wed Aug 23 14:56:14 2023 > got 0.12811207018243798
# Wed Aug 23 14:56:15 2023 > got 0.46677099052794957
# Wed Aug 23 14:56:15 2023 > got 0.5516770499545322
# Wed Aug 23 14:56:16 2023 > got 0.2400753632268765
# Wed Aug 23 14:56:16 2023 > got 0.22516160172021837
# Wed Aug 23 14:56:16 2023 Producer: Done
# Wed Aug 23 14:56:16 2023 > got 0.17641982458608385
# Wed Aug 23 14:56:16 2023 > got 0.7338673542331617
# Wed Aug 23 14:56:17 2023 > got 0.937125099318453
# Wed Aug 23 14:56:17 2023 Producer: Done
# Wed Aug 23 14:56:18 2023 > got 0.9175122570919346
# Wed Aug 23 14:56:19 2023 > got 0.7400293890694467
# Wed Aug 23 14:56:20 2023 > got 0.33980485175815534
# Wed Aug 23 14:56:20 2023 > got 0.0729175945687387
# Wed Aug 23 14:56:20 2023 Producer: Done
# Wed Aug 23 14:56:20 2023 > got 0.8685315538917037
# Wed Aug 23 14:56:21 2023 > got 0.6280644900225559
# Wed Aug 23 14:56:22 2023 > got 0.6317138080153393
# Wed Aug 23 14:56:22 2023 Producer: Done
# Wed Aug 23 14:56:22 2023 > got 0.36356088743498705
# Wed Aug 23 14:56:22 2023 Producer: Done
# Wed Aug 23 14:56:23 2023 > got 0.9641456758213433
# Wed Aug 23 14:56:24 2023 > got 0.6062516664167128
