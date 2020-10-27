fail = open("C:/Users/Madis/Downloads/rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()

aasta = int(input("Millist aastat soovite teada? "))
if aasta == 2019:
    print(rida)

    # ma ei saa aru kuidas saada mõnda muud rida peale viimase