def eelarve(kylalised):
    sook = 10 * kylalised
    rent = 55
    kokku = sook + rent
    return kokku

kylaliste_koguarv = int(input("Mitu inimest on kutsutud "))
kylaliste_kindel_arv = int(input("Mitu inimest tuleb "))


print("Maksimaalne eelarve on " + str(eelarve(kylaliste_koguarv)) + " eurot")
print("Minimaalne eelarve on " + str(eelarve(kylaliste_kindel_arv)) + " eurot")


maksimaalne_eelarve = eelarve(kylaliste_koguarv)
minimaalne_eelarve = eelarve(kylaliste_kindel_arv)

print ("Maksimaalne eelarve on " + str(maksimaalne_eelarve) + " eurot")
print ("Minimaalne eelarve on " + str(minimaalne_eelarve + " eurot"))