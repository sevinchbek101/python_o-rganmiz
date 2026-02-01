print("Salom bizning muzeyga xush kelibsiz!")
yosh = ""

while (yosh != "stop" or yosh != "quit"):
    yosh = input("Yoshingizni kiriting (Dasturdan chiqish uchun stop yoki quit deng): ")
    
    yosh = int(yosh)
    if yosh < 7:
        narh = 2000
    elif 7 <= yosh < 18:
        narh = 3000
    elif 18 <= yosh < 65:
        narh = 10000
    else:
        narh = 0

    if narh == 0:
        print("Sizga kirish bepul!")
    else:
        print(f"Sizdan kirish uchun {narh} so'm to'lanadi.")

    
