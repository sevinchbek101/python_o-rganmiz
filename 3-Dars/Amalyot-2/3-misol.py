i1,i2 = map(int,input("Iltimos ikkita son kiriting: ").split(" "))

if i1 == i2:
    print("Bu ikki son teng")
elif i1 < i2:
    print(f'{i1} bu son {i2} bu son dan kichik')
else:
    print(f"{i1} bu son {i2} bundak katta")