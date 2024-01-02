import asyncio
import telegram

async def main():
    token = open('.token', 'r')
    bot = telegram.Bot(token.readline())
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())