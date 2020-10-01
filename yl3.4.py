import random
pöialpoisid = int(input("Mitu pöialpoissi tahab õunu? "))
õunad = 14
while pöialpoisid > 0:
    arv = random.randint(1, 2)
    print(arv)
    õunad -= arv
    pöialpoisid -= 1

print("Lumivalgekesel jäi " + str(õunad))