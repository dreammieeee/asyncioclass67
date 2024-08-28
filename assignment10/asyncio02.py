from random import random
import asyncio
import time  # Import time module to measure elapsed time
 
# coroutine to generate work
async def producer(queue, start_time):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f'Producer: Done, Total time: {elapsed_time:.2f} seconds')
 
# coroutine to consume work
async def consumer(queue, start_time):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f'Consumer: Done, Total time: {elapsed_time:.2f} seconds')
 
# entry point coroutine
async def main():
    # record the start time
    start_time = time.time()
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue, start_time), consumer(queue, start_time))
  
# start the asyncio program
asyncio.run(main())
