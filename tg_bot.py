import asyncio
import datetime
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from config import token, user_id
from main import check_news_update
import aiohttp

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def news_every_minute():
    async with aiohttp.ClientSession() as session:
        while True:
            fresh_news = check_news_update()

            if len(fresh_news) >= 1:
                for k, v in sorted(fresh_news.items()):
                    news = fresh_news[k]['url']

                    await bot.send_message(user_id, news, disable_notification=True)

            else:
                await bot.send_message(user_id, "Пока нет свежих новостей...", disable_notification=True)

            await asyncio.sleep(10800)

async def main():
    await news_every_minute()

if __name__ == '__main__':
    asyncio.run(main())



