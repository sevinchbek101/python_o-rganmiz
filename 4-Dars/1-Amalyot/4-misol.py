Python_Lugt = {
    "print" : "chiqarish",
    "if" : "agar",
    "elif" : "agar va aks holda ",
    "else" : "aks holda",
    "for" : "sikill",
    "while" : "skil faqa bunda ikki ta qiymat bor True va Fals",
    "True" : "Rosat",
    "False" : "Yolg'on"
}

tarjima = input('Iltimos tajima qilishni hohlagan sozingizni kirting: ')

for i,s in Python_Lugt.items():
    if tarjima in Python_Lugt:
        print(f'{s}')
    else:
        print("Bunda so'z mavjud emas")