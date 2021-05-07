import asyncio

async def make_americano():
    print("Americano Start")
    await asyncio.sleep(10)
    print("Americano End")

async def make_latte():
    print("Latte Start")
    await asyncio.sleep(15)
    print("Latte End")

async def main():
    coro1 = make_americano()
    coro2 = make_latte()
    await asyncio.gather(
        coro1,
        coro2
    )

print("Main Start")
asyncio.run(main())
print("Main End")