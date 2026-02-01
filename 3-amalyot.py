savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while savol != 'exit':
    qiymat = input(savol)
    if qiymat < 0:
        print("Iltimos, musbat son kiriting!")
        continue
    elif qiymat == 'Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)

print(f"{qiymat} ning ildizi {ildiz} ga teng")