import random
a = random.randint(0,2)
b = random.randint(0,2)

if b > a:
    print(f"{b} > {a}")
elif a > b:
    print(f"{b} < {a}")
elif a == b:
    print(f"{b} == {a}")