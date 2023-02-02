from menus.Menus import *
from fractions import Fraction

@dp.message_handler(Text(startswith = 'num_'))
async def parse_number(message: types.Message):
    nums = message.text.split('num_')
    nms = str(nums[1]).split(' ')

    num = complex(nms[0])
    char = nms[1]
    numTwo = complex(nms[2])
    if complex(num) != 0 and complex(numTwo) != 0:
        ans = calculate(num, char, numTwo)

        await  message.answer(f'Ответ после произведения операции над комплексными числами: {complex(ans)}\n'
                              )
    add_to_csv(str(ans))


def calculate(a, b, c):
    match b:
        case '*':
            return a * c
        case '/':
                return  a / c

        case '+':
            return  a + c
        case '-':
            return  a - c

def add_to_csv(answer):
    with open('db.csv', 'a') as f:
        f.write('\n'+answer)


@dp.message_handler(Text(startswith = 'rac'))
async def calc_rac(message: types.Message):
    msg = message.text.split('rac_')
    num = msg[1].split(' ')[0]
    numTwo =  msg[1].split(' ')[1]
    ans = Fraction(int(num), int(numTwo))
    add_to_csv(str(ans))
    await message.answer(f'Ответ: {ans}')


