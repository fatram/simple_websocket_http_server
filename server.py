import asyncio
import websockets
import hashlib

bindat = open('tes.zip', 'rb').read()

def checkmd5(bindat):
    m = hashlib.md5()
    if(isinstance(bindat, str)):
        m.update(bindat.encode())
    else:
        m.update(bindat)
    return m.hexdigest()

async def hello(websocket, path):
    name = await websocket.recv()
    if(name[0:6] == "!echo "):
        await websocket.send(name[6:])
    elif(name == "!submission"):
        await websocket.send(bindat)
    else:
        if(checkmd5(bindat).lower() == checkmd5(name).lower()):
            await websocket.send("1")
        else:
            await websocket.send("0")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()