import asyncio
import random

async def cook_rice():
    cooking_time = 1 + random.random()
    print(f'cooking rice... (will take {cooking_time:.10f} seconds)')
    await asyncio.sleep(cooking_time)
    print('rice is finish')
    return 'rice ' , cooking_time

async def cook_noodle():
    cooking_time = 1 + random.random()
    print(f'cooking noodle... (will take {cooking_time:.10f} seconds)')
    await asyncio.sleep(cooking_time)
    print('noodle is finish')
    return 'noodle ' , cooking_time

async def cook_curry():
    cooking_time = 1 + random.random()
    print(f'cooking curry... (will take {cooking_time:.10f} seconds)')
    await asyncio.sleep(cooking_time)
    print('curry is finish')
    return 'curry ' , cooking_time

 
async def main():
    print('cooking lunch...')
    
    # Create the tasks
    rice_task = asyncio.create_task(cook_rice())
    noodle_task = asyncio.create_task(cook_noodle())
    curry_task = asyncio.create_task(cook_curry())
    
    # Wait for the first dish to complete
    done, pending = await asyncio.wait(
        [rice_task, noodle_task, curry_task], 
        return_when=asyncio.FIRST_COMPLETED
    )
    
    for task in done:
        dish_name, cook_time = await task  # Await to get the result and cooking time
        print(f'student A eat {dish_name} (cooking time: {cook_time:.10f} seconds)')
    


# Run the asyncio program
asyncio.run(main())