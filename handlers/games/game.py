from menus.Menus import *
from handlers.games.bot_games.ThiefGame import *
from handlers.games.bot_games.TicTacToeGame import *

@dp.message_handler(commands = ['game'])
async def send_choice_game(messsage: types.Message):
    await messsage.answer('Выбери игру', reply_markup =  gameChoosingMenu)




