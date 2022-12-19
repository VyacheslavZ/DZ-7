def Insert_Numbers():
    
    print('Тип комплексного числа: a + bi\n')
    user_komplex1 = input('Введите Первое комплексное число: ')
    user_komplex2 = input('Введите Второе комплексное число: ')
    operation = input('Выберите операцию: +, -, *, /:')
    with open('results.txt', 'a') as data:
        data.write(f'({user_komplex1}){operation}({user_komplex2}) = ')
    return [user_komplex1, user_komplex2, operation]

def Take_Rational_Part(user_number):
    
    rational_part = []
    for k in range(0, len(user_number)):
        if user_number[k] != ' ':
            rational_part.append(user_number[k])
        else:
            break
    rational_part = float(''.join(rational_part))
    return rational_part

def Take_Imaginary_Part(user_number):
  
    imaginary_part = []
    for i in range(0, len(user_number)):
        if user_number[i] == 'i':
            while user_number[i] != ' ':
                imaginary_part.insert(0,user_number[i - 1])
                i-= 1
    imaginary_part.pop(0)
    imaginary_part = float(''.join(imaginary_part))
    return imaginary_part

def Take_Symbol(user_number):
    
    symbol = []
    for l in range(0, len(user_number)):
        if user_number[l] == '-' and l !=0 or user_number[l] == '+' and l != 0:
            symbol.append(user_number[l])
    symbol = ''.join(symbol)
    return symbol

def Addition(r1, s1, i1, r2, s2, i2):
    
    result = []
    result.append(r1+r2)
    if s1 == '+' and s2 == '+':
        result.append(i1+i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1-i2)
    elif s1 == '-' and s2 == '+':
        result.append(i2-i1)
    else:
        result.append(-(i1+i2))
    return result

def Deduction(r1, s1, i1, r2, s2, i2):
    
    result = []
    result.append(r1-r2)
    if s1 == '+' and s2 == '+':
        result.append(i1-i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1+i2)
    elif s1 == '-' and s2 == '+':
        result.append(-i2-i1)
    else:
        result.append(i2-i1)
    return result

def Multiply(r1, s1, i1, r2, s2, i2):
    
    result = []
    result.append(r1*r2)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        result.append(-i1*i2)
    else:
        result.append(i1*i2)
    if s1 == "+":
        result.append(r2*i1)
    else:
        result.append(-r2*i1)
    if s2 == "+":
        result.append(r1*i2)
    else:
        result.append(-r1*i2)
    result[0] = result[0] + result[1]
    result[1] = result[2] + result[3]
    result.pop(3)
    result.pop(2)
    return result    
    
def division(r1, s1, i1, r2, s2, i2):
    
    numerator = []
    denominator = []
    result = []
    numerator.append(r1*r2)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        numerator.append(i1*i2)
    else:
        numerator.append(-i1*i2)
    if s1 == "-":
        numerator.append(-r2*i1)
    else:
        numerator.append(r2*i1)
    if s2 == "+":
        numerator.append(-r1*i2)
    else:
        numerator.append(r1*i2)
    numerator[0] = numerator[0] + numerator[1]
    numerator[1] = numerator[2] + numerator[3]
    numerator.pop(3)
    numerator.pop(2)
    denominator.append(r2**2+i2**2)
    result.append(numerator[0]/denominator[0])
    result.append(numerator[1]/denominator[0])
    return result

def record_in_file(result):
    
    with open('results.txt', 'a') as data:
        if result[1] != 0:
            for i in range(0, 2):
                if result[i] > 0 and i == 1:
                    data.write('+ ')
                elif result[i] < 0 and i == 1:
                    result[i] = -result[i]
                    result[i] = str(result[i])
                    data.write('- ')
                    data.write(result[i])
                else:
                    result[i] = str(result[i])
                    data.write(result[i])
                if i != 1:
                    data.write(' ')
            data.write('i\n')
        else:
            result[0] = str(result[0])
            data.write(f'{result[0]}\n')

def Repeat_Or_No():
    '''Продолжить или нет'''
    user_choice = 'Ошибка!'
    while user_choice != 'Y' or user_choice != 'N':
        user_choice = input('Продолжить считать Копмлексные числа? (Y or N)')
        if user_choice == 'N':
            return False
        elif user_choice == 'Y':
            return True
        else:
            print('Ошибка! Продолжить считать Копмлексные числа? Y or N')