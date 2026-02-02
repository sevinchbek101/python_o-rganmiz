yosh = int(input("Iltimos yoshingizni kirting: "))

if (yosh < 4) or (60 < yosh):
    print("Sizga kirish bepul")
elif (18 < yosh) and (4 >= yosh):
    print("Sizga kirish 10.000 som")
else:
    print("Sizga kirish bepul")