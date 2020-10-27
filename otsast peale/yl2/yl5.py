kirja_suurus = float(input("Mis on kirja suurus? (x)MB "))
pealkiri = input("Mis on kirja pealkiri? ")
manus = input("Kas kirjaga on kaasas manus? (Jah/Ei)")

if (kirja_suurus > 1,0) and (pealkiri == "") and ((manus == "Jah") or (manus == "jah")):
    print("Kiri on spämm.")
else:
    print("Kiri ei ole spämm.")
