s = int(input('Bugun nechta odambilan uchrashdigiz(suhbatlashdingiz):'))

odamlar = []

for i in range(s):
    i += 1
    odamlar.append(input(f'siz bugnun korishgan(suhbatlashgan) \n {i}-chi odamni ismi:'))

for i in odamlar:
    print(f'siz bugun gaplshgan odamning ismi: {i}')