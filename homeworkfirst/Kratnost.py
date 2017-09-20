first  = int(input("Введите первое число "))
second = int(input("Введите второе число "))

for j in range(first,second+1):
    if j%5==0:
        print(j)
