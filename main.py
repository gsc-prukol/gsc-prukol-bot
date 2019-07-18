"""
This is a FAQ bot.
"""
import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.executor import start_webhook
from configurations import Messages as MSG, Regexp as RE

TOKEN = os.environ['TOKEN']


WEBHOOK_HOST = 'https://gsc-prukol-bot.herokuapp.com'  # name your app
WEBHOOK_PATH = '/webhook/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.environ.get('PORT')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(regexp=RE.hello)
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, MSG.hello, disable_web_page_preview=True)


@dp.message_handler(regexp=RE.printing)
async def prints(message: types.Message):
    await bot.send_message(message.chat.id, MSG.firstPhrase, reply_to_message_id=message.message_id)
    await bot.send_message(message.chat.id, MSG.printing, disable_web_page_preview=True)


@dp.message_handler(regexp=RE.clinic)
async def clinic(message: types.Message):
    await bot.send_message(message.chat.id, MSG.firstPhrase, reply_to_message_id=message.message_id)
    await bot.send_message(message.chat.id, MSG.clinic)


@dp.message_handler(regexp=RE.numberManager)
async def numberManager(message: types.Message):
    await bot.send_message(message.chat.id, MSG.firstPhrase, reply_to_message_id=message.message_id)


@dp.message_handler(regexp=RE.numberTA)
async def numberTA(message: types.Message):
    await bot.send_message(message.chat.id, MSG.firstPhrase, reply_to_message_id=message.message_id)


@dp.message_handler(regexp=RE.fullNameCastellansha)
async def fullNameCastellansha(message: types.Message):
    await bot.send_message(message.chat.id, MSG.firstPhrase, reply_to_message_id=message.message_id)
    await bot.send_message(message.chat.id, MSG.fullNameCastellansha)


@dp.message_handler(regexp=RE.fullNameManager)
async def fullNameManager(message: types.Message):
    await bot.send_message(message.chat.id, MSG.firstPhrase, reply_to_message_id=message.message_id)
    await bot.send_message(message.chat.id, MSG.fullNameManager)

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    # insert code here to run it before shutdown
    pass



if __name__ == '__main__':
    start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH,
                  on_startup=on_startup, on_shutdown=on_shutdown,
                  host=WEBAPP_HOST, port=WEBAPP_PORT)