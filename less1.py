# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
word ='p'
print(word)
number = '493'
print(number)
# №2
#
second = int(input("Введите количество секунд:"))
hours =(second//3600) #перевод в часы
minutes =(second%3600//60) #перевод в минуты
seconds = (second%3600%60) #перевод в секунды
print(f'H{hours}:M{minutes}:S{seconds}')
# №3
n = int(input("Введите число :"))
a = int(str(n)*2)
b = int(str(n)*3)
print(f'n+nn+nnn={a}+{b}+{n}={n+b+a}')
#4
n = int(input("Введите число :"))
num = n % 10
while n > 0 :
    n = n // 10
    if n % 10 > num:
        num = n%10
print(num)
#5
ebitda = float(input("Введите общую прибыль до вычета расходов:"))
costs = float(input("Введите расходы :"))
proceeds=ebitda-costs
print("Показатель прибыли:", proceeds)
if proceeds >= 0:
    rent = ebitda / proceeds # Расчет рентабельности
    print('Компания прибыльная, рентабельность:', rent)
    per = int(input("Введите кол-во персонала:"))
    ppp = ebitda / per #Прибыль на сотрудника
    print("Прибыль на сотрудника:", ppp)
else:
    print('Компания убыточная')
# №6
a = float(input("Введите цель на первый день :"))
b = float(input("Введите цель для окончания :"))
d=a #результат в каждый последующий день
day = 1
while d < b:
        d = d + d * 0.1 #Увеличение на 10%
        day = day+1 #условие цикла для дня
print(day)
print(d)










