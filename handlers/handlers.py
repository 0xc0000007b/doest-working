from Settings.bot_commandes import *
from Settings.settings import *
from handlers.games.game import *
from handlers.other.parseHandlers import *
from handlers.other.phonebook import *
from handlers.math.Calculator import *


@dp.message_handler(commands = ['start'])
async def SendInfo(message: types.Message):
    await message.answer(info)
    await log(message)
async def log(message):
    with open('../log.txt', 'a', encoding = 'utf-8') as f:
        log = "\nСообщение от {0} {1} (id = {2}) \n {3}\n".format(message.from_user.first_name,
                                                                message.from_user.last_name,
                                                                str(message.from_user.id), message.text)
        f.write(log)




@dp.message_handler(commands = ['parse'])
async def ParseText(message: types.Message):
    await  message.answer('Клацни на кнопку', reply_markup = parseMenu)

















