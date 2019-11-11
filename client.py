#!/usr/bin/env python

# WS client example

import asyncio
import websockets

bindat = open('tes.zip', 'rb').read()

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        if(name == 'tes'):
            await websocket.send(bindat)
        else:
            await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())