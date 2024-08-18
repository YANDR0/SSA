

### Buscar el divisor primo más grande

def max_Factor(n):

    n = n if n > 0 else n * -1
    factor = -1
    change = 0
    i = 2

    while i*i <= n: 
        while(n % i == 0):
            if(i != factor): 
                factor = i
                change += 1
            n /= i
        i += 1
    
    if(n > 1):
        factor = n
        change += 1

    return int(factor) if change > 1 else -1
            

### Obtener y devolver datos

numbers = []
n = int(input())

while(n != 0):
    numbers.append(n)
    n = int(input())

for i in numbers:
    print(max_Factor(i))