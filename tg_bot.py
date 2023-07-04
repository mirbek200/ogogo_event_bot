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


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
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


if __name__ == '__main__':
    executor.start_polling(dp)

# Работет по кнопке 
# import asyncio
# import datetime
# import json
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
# from aiogram.dispatcher.filters import Text
# from config import token, user_id
# from main import check_news_update
# import aiohttp

# bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
# dp = Dispatcher(bot)

# button1 = types.KeyboardButton('News')
# keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1)


# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     fresh_news = check_news_update()
#     for k, v in sorted(fresh_news.items()):
#         news = fresh_news[k]['url']

#         await bot.send_message(user_id, news, disable_notification=True, reply_markup=keyboard1)


# @dp.message_handler()
# async def kb_answer(message: types.Message):
#     if message.text == 'News':
#         fresh_news = check_news_update()
#         if len(fresh_news) >= 1:
#             for k, v in sorted(fresh_news.items()):
#                 news = fresh_news[k]['url']

#                 await bot.send_message(user_id, news, disable_notification=True)
#         else:
#             await bot.send_message(user_id, "Пока нет свежих новостей...", disable_notification=True)


# if __name__ == '__main__':
#     executor.start_polling(dp)


# Без кнопки работает 
# import asyncio
# import datetime
# import json
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
# from aiogram.dispatcher.filters import Text
# from config import token, user_id
# from main import check_news_update
# import aiohttp

# bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
# dp = Dispatcher(bot)


# async def news_every_minute():
#     async with aiohttp.ClientSession() as session:
#         while True:
#             fresh_news = check_news_update()

#             if len(fresh_news) >= 1:
#                 for k, v in sorted(fresh_news.items()):
#                     news = fresh_news[k]['url']

#                     await bot.send_message(user_id, news, disable_notification=True)

#             else:
#                 await bot.send_message(user_id, "Пока нет свежих новостей...", disable_notification=True)

#             await asyncio.sleep(10800)

# async def main():
#     await news_every_minute()

# if __name__ == '__main__':
#     asyncio.run(main())



