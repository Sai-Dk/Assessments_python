import math
print("Prime numbers from 2 to 100:")
for n in range(2, 101): 
    is_prime = True
    for i in range(2, int(math.sqrt(n))+1): 
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
