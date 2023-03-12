from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import json
from get_data import get_data

bot = Bot(token="Здеся типо токен, но я его вам не дам :3", parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(messege: types.Message):
    start_buttons = 'Увидеть новые заказы 👀💰💰'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(start_buttons)

    await messege.answer('Zzz...Zzz...Zzz', reply_markup=keyboard)


@dp.message_handler(Text(equals='Увидеть новые заказы 👀💰💰'))
async def get_list(messege: types.Message):

    get_data()

    with open('works.json', encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        card = f'{hlink(item.get("name"), item.get("url"))}\n' \
            f'{hbold(item.get("price"))}\n🔥🔥🔥' \
            f'{hbold(item.get("date"))}\n' \
            f'{hbold(item.get("tz"))}'

        await messege.answer(card)

#Не работает
# @dp.message_handler()
# async def get_new(messege: types.Message):
#     with open('works.json', encoding="utf-8") as file:
#         data = json.load(file)
#
#     card = f'{hlink(data[0].get("name"), data[0].get("url"))}\n' \
#            f'{hbold(data[0].get("price"))}\n🔥🔥🔥' \
#            f'{hbold(data[0].get("date"))}\n' \
#            f'{hbold(data[0].get("tz"))}'
#
#     await messege.answer('НОВЫЙ ЗАКАЗ!!!🔥🔥🔥')
#     await messege.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()