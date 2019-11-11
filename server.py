#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    if(name[0:6] == "!echo "):
        await websocket.send(name[6:])
    """elif(name == "!submission"):
        # TO DO : send binary data of the zip file contained source code and readme
    elif: # TO DO : client will send binary data of the submitted file and perform md5 comparison
        await websocket.send(1)
    else:
        await websocket.send(0)"""

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()