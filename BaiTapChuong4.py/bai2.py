from random import randrange
somay =randrange(1,101)
solandoan = 0
Win = False
while solandoan < 7:
    solandoan += 1
    songuoi = int(input("MAY DOAN [1 ..100]. Moi ban doan: "))
    print("Lan doan thu",solandoan)
    if songuoi == somay:
        print("Chuc mung ban da doan dung so!")
        Win = True
    elif songuoi < somay:
        print("So ban doan nho hon so may")
    elif songuoi > somay:
        print("So ban doan lon hon so may")
    if Win == False:
        print("Game Over. So may la:", somay)
    hoi = input("Ban co muon choi tiep khong (c/k)? ")
    if hoi == 'k':
        break
    print("Cam on ban da choi!Ket Thuc tro choi")