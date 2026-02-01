kitoblar = []
kitob = ""

while kitob != "stop":
    kitob = input("Yangi kitob nomini kiriting (to'xtatish uchun 'stop' deb yozing): ")
    if kitob != "stop":
        kitoblar.append(kitob)
    print("Siz bergan kitob ro'yxat ga qoshildi.")

print("Sizning kitoblaringiz ro'yxati:")
for kitob in kitoblar:
    print(f"siz yaxshi ko'radigan kitob: {kitob}")