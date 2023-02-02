from Settings.settings import *

move = 'x'
count = 0
field = [['\000' for i in range(3)] for i in range(3)]

b1 = types.InlineKeyboardButton(text=f'{field[0][0]}', callback_data=f'00')
b2 =     types.InlineKeyboardButton(text=f'{field[0][1]}', callback_data=f'01')
b3 =    types.InlineKeyboardButton(text=f'{field[0][2]}', callback_data=f'02')


b4 =        types.InlineKeyboardButton(text=f'{field[1][0]}', callback_data=f'10')
b5 =       types.InlineKeyboardButton(text=f'{field[1][1]}', callback_data=f'11')
b6 =       types.InlineKeyboardButton(text=f'{field[1][2]}', callback_data=f'12')



b7 =     types.InlineKeyboardButton(text=f'{field[2][0]}', callback_data=f'20')
b8 =    types.InlineKeyboardButton(text=f'{field[2][1]}', callback_data=f'21')
b9 =   types.InlineKeyboardButton(text=f'{field[2][2]}', callback_data=f'22')


kb = types.InlineKeyboardMarkup(inline_keyboard =[
        [b1, b2, b3],
        [b4, b5, b6],
        [b7, b8, b9],
    ])