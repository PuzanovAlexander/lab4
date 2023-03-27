def lab4_1():
    n = int(input('Введите число'))
    delit = n % 3
    if delit == 0:
        print ('Число делится на 3')
    else:
        print ('Число не делится на 3')
    
def lab4_2():
    try:
        n = int(input('Введите чиcло'))
        r=100/n
        print ("Результат деления: " + str(r))
    except ValueError:
        print ("Введено не число!")
    except ZeroDivisionError:
        print ("Простите, делить на ноль я не могу...")
        
def lab4_3():
    date = str(input('Введите дату'))
    date = date.split('.')
    a = int(date[0]) * int(date[1])
    b = int(date[2][2:4])
    if a == b:
        print ('Дата является магической')
    else:
        print ('К сожалению дата не является магической')
     
def lab4_4():
    tiсket = str(input('Введите номер билета'))
    if len(tiсket) % 2 == 0:
        sum1 = sum([int(i) for i in tiсket[:int(len(tiсket) / 2)]])
        sum2 = sum([int(i) for i in tiсket[int(len(tiсket) / 2):]])
        if sum1 == sum2:
            print ('Счастливый')
        else:
            print ('Не счасливый')
    else:
        print ('Введите чётное число')