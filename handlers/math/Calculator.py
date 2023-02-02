from menus.Menus import *


@dp.message_handler(Text(startswith = 'num_'))
async def parse_number(message: types.Message):
    nums = message.text.split('num_')
    nms = str(nums[1]).split(' ')

    num = nms[0]
    char = nms[1]
    numTwo = nms[2]
    if num != 0 and numTwo != 0:
        ans = calculate(num, char, numTwo)
        await  message.answer(f'Ответ: {complex(ans)}')
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
    with open('db.csv', 'w') as f:
        f.write(answer)




