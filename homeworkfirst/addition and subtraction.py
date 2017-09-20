print('Введите первое число:')
first = float(input(""))
print('Введите второе число')
second = float(input(""))
print('Введите знак + или -')
calculation = str(input(""))
if(calculation == "+" ):
    addition = first + second
    print("Сложив два числа мы получили:")
    print(addition)
elif(calculation == "-"):
    subtraction = first - second
    print("Выполнив вычитание мы получили:")
    print (subtraction)
else:
    print("Допустимые знаки только + и -")

