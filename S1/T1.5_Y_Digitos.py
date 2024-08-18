

### Formula de legendre para para multiplicidad de primos en factoriales
def legendre(n, p):
    count = 0
    while(n > 0):
        n //= p
        count += n
    return count


### Cantidad de digitos, casi igual que legendre
### trabaja sobre el resultado, tons no sirve :v 
def digits(n, b):
    count = 0
    while(n > 0):
        n //= b
        count += 1
    return count


### Factores primos de un número
def factors(n):
    f = []
    i = 2
    while i*i <= n: 
        while(n % i == 0):
            f.append(i)
            n /= i
        i += 1
    if(n > 1):
        f.append(i)

    return f



### Entrada de datos

args = input()
inp = []

while(args):
    args = args.split()
    inp.append(args)
    args = input()

for i in inp:
    num = i[0]
    base = i[1]