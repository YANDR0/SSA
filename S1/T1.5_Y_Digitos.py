
import math 

### Suma de los logaritmos de cada miembro del factorial
def numDigits(n, b):
    sum = 1
    for i in range(1, n+1):
        sum += math.log(i) / math.log(b)
    return int(sum)

### Formula de legendre para para multiplicidad de primos en factoriales
def legendre(n, p):
    count = 0
    while(n > 0):
        n //= p
        count += n
    return int(count)

### Factores primo más grande y sus apariciones 
def bigFactor(n):

    l_factors = []
    i = 1
    while i*i <= n: 
        i += 1
        count = 0
        while(n % i == 0):
            count += 1
            n /= i
        if(count > 0):
            l_factors.append([i, count])
    if(n > 1):
        l_factors.append([n, 1])

    return l_factors

### Entrada de datos
args = input()
inp = []

while(args):
    args = args.split()
    inp.append(args)
    args = input()

for i in inp:
    num = int(i[0])
    base = int(i[1])

    f = bigFactor(base)
    zeros = 0

    for i in f:
        spec = legendre(num, i[0])//i[1] 
        zeros = spec if spec < zeros or zeros <= 0 else zeros

    digits = numDigits(num, base)

    print(str(zeros) + " " + str(digits))
    
