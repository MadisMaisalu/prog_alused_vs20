import random  # suvalise numbri generaator
kilomeetrite_arv = 0  # Muutuja tekitamine



sammu_pikkus=float(input("Sisestage sammu pikkus meetrites: ")) #input kasutaja jaoks

def kilomeetrid(sammude_arv_paevas, sammu_pikkus):  # funktsiooni defineerimine
    kilomeetrite_arv=((sammude_arv_paevas*sammu_pikkus)/1000)
    return kilomeetrite_arv


random.seed()
sammude_arv_paevas=[]  # list kuhu tulevad sammude päevased arvud

for x in range(7):  # 7 korda genereerib - 7 nädalapäeva
    sammude_arv_paevas.append(random.randrange(5000, 15000)) #lisab need listi sammude_arv_paevas
    print(sammude_arv_paevas)

nadal=0
uks_paev=0  # tekitan muutujad
for y in range(len(sammude_arv_paevas)):  # leian päeva ja nädalaga läbitud kilomeetrite arvu
    uks_paev=kilomeetrid(sammude_arv_paevas[y], sammu_pikkus)
    print(str(uks_paev) + "km")
    nadal+=uks_paev

print("Kõndisite nädalaga " + str(nadal) + "km, ning tegite keskmiselt " + str(sum(sammude_arv_paevas)/7))
  #  väljastan väärtused
if sum(sammude_arv_paevas)/7 < 10000:
    print("Peate järgmine nädal rohkem kõndima!")
