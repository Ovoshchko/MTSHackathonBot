import asyncio

async def runBot():
    from HandleStates import dp

    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(runBot())
