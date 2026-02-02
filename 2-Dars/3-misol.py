toq_sonlar = []

for i in range(101):
    if i >= 10:
        if i % 2 != 0:
            toq_sonlar.append(i)

for i in toq_sonlar:
    print(f"{i ** 3}")
