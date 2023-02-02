import logging
import random as r
from aiogram import Dispatcher, Bot, types, executor
from aiogram.dispatcher.filters import Text

# log = logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)


token = ''
bot = Bot(token)
dp = Dispatcher(bot)
