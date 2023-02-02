from menus.Menus import *
import aiogram.dispatcher.filters as f
from handlers.Authors.PanteraHandlers import *
from handlers.Authors.Metallica import *

@dp.callback_query_handler(f.Text(startswith = 'parse'))
async def langs_menu(callback: types.CallbackQuery):
    await callback.message.answer('Выбери язык', reply_markup = translations)

@dp.callback_query_handler(f.Text(startswith = 'english'))
async def originals_menu(callback: types.CallbackQuery):
    await callback.message.answer('Выбери группу: ', reply_markup = englishBandsMenu)
