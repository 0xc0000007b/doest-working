from Settings.settings import *

@dp.message_handler(commands = ['book'])
async def send_book(message: types.Message):
    with open('numbers.csv', 'r') as f:
       lines = f.readlines()[1:]
       d = lines
    await message.answer(f'добавишь контакт? введи номера через разделитель, начиная с *p*\nВ твоей книге уже есть контакты{d}', parse_mode = 'Markdown')
@dp.message_handler(Text(startswith = 'p_'))
async def add_phone_to_book(message: types.Message):
    msg = message.text.split('p_')
    nums = msg[1].split(' ')
    name = nums[0]
    sep = nums[1]
    last_name = nums[2]
    number = nums[4]
    save_to_db(name, sep, last_name, number)
    await message.answer('successfully added')




def save_to_db(a, b, c,d):
    with open('../../numbers.csv', 'a') as f:
        f.write('\n' + a + b + c + b + d)

