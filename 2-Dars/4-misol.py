print(f"Salom Iltimos 5 ta sevli kino ingizni kiriing")

kino = []

for i in range(5):
    i += 1
    kino.append(input(f'{i}-chi sevimli kinoni kiriting: '))

for i in kino:
    print(f'sizning sevimli kinoingiz nomi: {i}')
