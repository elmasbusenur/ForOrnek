faktoriyel = 1
while True:

    sayi=int(input("negatif olmayan bir sayi giriniz:"))
    if(sayi<=0):
        print("pozitif bir sayi giriniz!")
    else:

        for i in range(1,sayi+1):
            faktoriyel=faktoriyel*i
        print("faktoriyel",faktoriyel)
        break