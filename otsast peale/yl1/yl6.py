inimeste_arv = int(input("Sisestage inimeste arv: "))
bussi_kohtade_arv = int(input("Sisestage kohtade arv: "))
busside_arv = round(inimeste_arv / bussi_kohtade_arv)
maha_jaab = inimeste_arv % bussi_kohtade_arv
print("Tellitakse " + str(busside_arv) + " buss(i), ning maha jääb " + str(maha_jaab) + " inimene(st).")