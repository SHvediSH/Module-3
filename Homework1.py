def test():                             #Объявление функции
    a = 10                              #Локальная переменная 1
    b = 20                              #Локальная переменнная 2
    print(a, b)                         #Вывод обоих переменных

test()                                  #Вызов первой функции

def test2(params1, params2, params3):   #Объявление функции с 3 параметрами
    print(params1, params2, params3)    #Вывод значений заданных параметров

test2(1, 2, 3)  #Вызов функции с вводом параметров