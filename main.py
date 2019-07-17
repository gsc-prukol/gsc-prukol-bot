"""
This is a FAQ bot.
"""
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.executor import start_webhook
from configurations import WebHook as WH, Messages as MSG, Regexp as RE, BotConfig as BC




# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BC.token)
dp = Dispatcher(bot)


@dp.message_handler(regexp=RE.printing)
async def prints(message: types.Message):
    await bot.send_message(message.chat.id, MSG.firstPhrase, reply_to_message_id=message.message_id)
    await bot.send_message(message.chat.id, MSG.printing) # todo підключити бота до бд


@dp.message_handler(regexp=RE.clinic)
async def clinic(message: types.Message):
    await bot.send_message(message.chat.id, "А пошук не працює?", reply_to_message_id=message.message_id)
    await bot.send_message(message.chat.id, MSG.clinic) # todo підключити бота до бд


async def on_startup(dp):
    await bot.set_webhook(WH.url)


async def on_shutdown(dp):
    # insert code here to run it before shutdown
    await bot.delete_webhook()


if __name__ == '__main__':
    start_webhook(dispatcher=dp, webhook_path=WH.path,
                  on_startup=on_startup, on_shutdown=on_shutdown,
                  host=WH.host, port=WH.webapp_port)
