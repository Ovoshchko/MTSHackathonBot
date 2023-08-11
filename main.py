import asyncio
#import nest_asyncio

async def runBot():
    from HandleStates import dp
    from aiogram import executor

    #executor.start_polling(dispatcher=dp, skip_updates=False)
    await dp.start_polling()

if __name__ == '__main__':
    #nest_asyncio.apply()
    asyncio.run(runBot())
