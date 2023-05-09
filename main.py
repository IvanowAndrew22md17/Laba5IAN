x = int(input("Номер задачи: "))
a = 0
b = 0
c = 0
d = 0
i = 0

# 5.1
def f1():
    c = ["13", "15", "16", "19", "22"]
    a = input("Введите число: ")
    if a in c:
        print("Вы угадали число!)")
    else:
        print("Вы не угадали число(")
if x == 1:
    f1()

# 5.2
def f2():
    from random import randint
    c = [randint(1, 10) for i in range(5)]
    print(c)
    d = [i for i in set(c) if c.count(i) > 1]
    if len(d) == 0:
        print("Повторяющихся элементов нет")
    else:
        print(d)
if x == 2:
    f2()

# 5.3
def f3():
    d = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье",)
    a = int(input("Сколько выходных в неделю вы хотите?"))
    print('Вы отдыхаете в:', d[:-a - 1:-1])
    print('Вы работаете в:', d[:-a])
if x == 3:
    f3()

# 5.4
def f4():

if x == 4:
    f4()
if x < 0 or x > 4:
    print("Такой задачи нет(")