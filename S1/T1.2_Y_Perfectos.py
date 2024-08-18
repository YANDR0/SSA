

### Entrada de datos

n = int(input())
numbers = input().split(",")
results = [2,3,5,7,13,17,19]

for i in range(n):
    r = int(numbers[i])
    if(r in results):
        print("Yes")
    else:
        print("No")


