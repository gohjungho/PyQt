import websockets
import asyncio

async def bithumb_ws_client():
    url = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(url) as websocket:
        greeting = await websocket.recv()
        print(greeting)

async def main():
    await bithumb_ws_client()

asyncio.run(main())