import asyncio
import json
import aiofiles
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def process_pokemon_file(file_path):
    async with aiofiles.open(file_path, mode='r') as f:
        contents = await f.read()
        pokemon_data = json.loads(contents)
        name = pokemon_data['name']
        moves = [move['move']['name'] for move in pokemon_data['moves']]
        
        moves_file_path = Path(pokemonmove_directory) / f"{name}_moves.txt"
        async with aiofiles.open(moves_file_path, mode='w') as f_out:
            await f_out.write('\n'.join(moves))
        print(f"Wrote moves of {name} to {moves_file_path}")

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')

    tasks = []
    for path in pathlist:
        tasks.append(process_pokemon_file(path))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())