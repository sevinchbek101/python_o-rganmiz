mahsulotlar = [
    'non',
    'sut',
    'tuxum',
    'shakar',
    'tuz',
    'guruch',
    'makaron',
    'yog‘',
    'olma',
    'choy'
]

savat = []

for i in range(5):
    savat.append(input("kerkli maxsulaotni kiriting: "))

for kalit in savat:
    if kalit in mahsulotlar:
        print(f"{kalit}- bu mahsulaot dokonda bor")
    else:
        print(f"{kalit}- bu mahsulot dokonda yoq")


