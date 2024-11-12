import random

val=[random.randint(-10, 10) for _ in range(20)]
print("Список значений: ", val)

pairs=[]
for i in range(len(val)):
    for j in range(i+1, len(val)):
        pairs.append((val[i], val[j]))

print("\nВсе уникальные пары: ", pairs)

num=int(input("Введите целое число: "))

count=0
for pair in pairs:
    if sum(pair)<num:
        count+=1

print(f"\nКол-во пар, чья сумма меньше {num}: {count}")