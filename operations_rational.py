import operations_rational as op
import sys

def x():
    firstnum = float(input('Введите первое число через запятую: ').replace(',', '.'))
    return firstnum

def y():
    secondnum = float(input('Введите второе число через запятую: ').replace(',', '.'))
    return secondnum

def selectoperation():
    global operation
    operation = (input(f'Выберите операцию: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Неверный синтаксис!')

def res(firstnum, secondnum):
    if  operation == '+':
        res = firstnum + secondnum
        result = round(res, 2)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 2)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 2)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 2)
        return result
    else:
        print('Неверный синтаксис!')

def mainterminal():
    global file
    x = op.x()
    while True:
        y = op.y()
        oper = op.selectoperation()
        res = op.res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'rational: {x} {oper} {y} = {res}\n')
        print(f'Результат: {x} {oper} {y} = {res}\n(Результат операций записан в "txt" файл)' )
        again = input('Хотите еще посчитать? Y/N: ').lower()
        if again == 'y':
            useresult = input('Вы хотите использовать результат последней операции? (Y/N): ').lower()
            if useresult == 'y':
                x = res
                continue
            elif useresult == 'n':
                break
            else:
                sys.exit()      
        else:   
            sys.exit()