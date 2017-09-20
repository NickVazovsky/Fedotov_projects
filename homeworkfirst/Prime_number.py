k = int(input("Введите число:"))
def isprime(n):
    if n==1:#Если n==1
        return False #то фалс
    for x in range(2,n): #фор  х ин рандж
        if n % x == 0:
            return  False
        else:
            return True
def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1
for n in primes():
    if n>k:break
    print(n)
isprime(k)
primes(k)
