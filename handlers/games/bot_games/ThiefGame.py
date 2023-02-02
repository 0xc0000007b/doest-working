import aiogram.dispatcher.filters as f
import random
global schekels
from menus.Menus import *

schekels = 0
@dp.callback_query_handler(f.Text(startswith = 'thief'))
async def PlayThiefGameGame(callback: types.CallbackQuery):
    await callback.message.answer('Сколько денег в казне будет снчала?', reply_markup = schekelsgameKeyBoard)

@dp.callback_query_handler(f.Text(startswith = 'set_'))
async def AddSchekels(callback: types.CallbackQuery):
    global schekels
    query = callback.data.split('_')
    schekels = int(query[1])

    await callback.message.answer(f'В казне теперь {schekels} шекелей, сколько своруешь?', reply_markup = theftMenu)

@dp.callback_query_handler(f.Text(startswith = 'theft_'))
async def ThuefSchekels(callback: types.CallbackQuery):
    global schekels
    query = callback.data.split('_')
    if schekels <= 0:
        await callback.message.answer('Ты хочешь занять в долг у народа? и так денег нет, тебя посадят')
    else:
        schekels -= int(query[1])
        await callback.message.answer(f'Ты своровал  {query[1]} шекелей,осталось {schekels} шкеклей в казне')
        r = random.randint(0, 50)
        schekels -= r
        await callback.message.answer(f'бот своровал {r} шекелей. Сколько возьмешь?\nВ казне осталось {schekels}', reply_markup = theftMenu)
