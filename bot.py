from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.utils.exceptions import Throttled
from aiogram.utils.executor import start_polling
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import os
import sys

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger()
log.addHandler(handler)

if 'LOG_LEVEL' in os.environ:
    LOG_LEVEL_STRING = os.environ['LOG_LEVEL']
else:
    log.warning("LOG_LEVEL not found in env. Set default - WARNING.")
    LOG_LEVEL_STRING = 'WARNING'

if LOG_LEVEL_STRING == 'DEBUG':
    LOG_LEVEL = logging.DEBUG
elif LOG_LEVEL_STRING == 'INFO':
    LOG_LEVEL = logging.INFO
elif LOG_LEVEL_STRING == 'WARNING':
    LOG_LEVEL = logging.WARNING
elif LOG_LEVEL_STRING == 'ERROR':
    LOG_LEVEL = logging.ERROR
else:
    log.warning(f"LOG_LEVEL {LOG_LEVEL_STRING} don't support. Set default - WARNING")
    LOG_LEVEL = logging.WARNING


if 'API_TOKEN' in os.environ:
    API_TOKEN = os.environ['API_TOKEN']
else:
    log.error("API_TOKEN not found in env")
    exit(1)

if 'MESSAGE_TEXT' in os.environ:
    MESSAGE_TEXT = os.environ['MESSAGE_TEXT']
else:
    log.warning("MESSAGE_TEXT not found in env. Set default - 'Plug'.")
    MESSAGE_TEXT = 'Plug'

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler()
@dp.throttled(rate=1)
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    log.info(f"Sending answer message to {user_id} {username}")
    await message.answer(MESSAGE_TEXT)


if __name__ == '__main__':
    log.setLevel(LOG_LEVEL)
    start_polling(dp, skip_updates=True)
