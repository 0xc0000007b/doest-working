from TicTacMenu import *


@dp.callback_query_handler(Text('tic'))
async def SendField(callback: types.CallbackQuery):
    await callback.message.answer('Попробуй мою бета функцию', reply_markup = kb)
    for i in kb.row():
        for j in kb.row():
            if kb.row(b1.callback_data)[0][i] == '00':
                await callback.message.edit_reply_markup(kb.row(b1.text == '\124'))