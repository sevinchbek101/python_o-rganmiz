savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    
    qiymat = float(qiymat)
    if qiymat < 0:
        continue

    elif qiymat == 'exit':
        break
    
    else:
        ildiz = qiymat ** 0.5
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
