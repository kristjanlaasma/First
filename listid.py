# list ehk massiiv
# list [nimekiri, loend], tuple (järjend), dictionary {sõnastik}

places = []
places.append("Kehtna") # lisa uus koht listi lõppu
places.append("Rapla")
places[1:1] = ["Tallinn", "Pärnu"] # lisa kehtna ja rapla vahele
places.extend(["Viljandi", "Tartu", "Rapla"]) # lisa lõppu
places.insert(2, "Are")



numbers = [1, 2, 3, 4, 5]

print(places) # näita kohanimede listi
print(numbers) # näita numbrite listi
print(type(places)) # näita kohanimede muutuja tüüpi

# kustutamine
places.remove("Rapla") # kustutab esimese leitud nime
places.pop(6) # kustutab viimase rapla
del places[2] # kustutab Are

print(places)

# Ülesanne: lisa rapla, pärnu ja viljandi vahele ning listi lõppu

places.insert(3, "Rapla")
places.append("Rapla")
print(places)

# leiame elemendi indeksi ja mitu korda esineb(Rapla)
place = places[-1] # nimekirja viimane rapla
index = places.index(place) # mis indeks on esimene rapla
count = places.count(place) # mitu korda leiti
print(place, index, count)

if place in places:
    print(f"{place} on nimekirjas olemas.")
    
if "Kohila" in places:
    print(f"Kohila on nimekirjas olemas.")
    
print(len(places)) # listi suurus
print(places[len(places)-1]) # viimane element listist (Rapla)

# koopia listist
list_copy = places.copy()
list_list = list(places)
# sorteerimine
list_copy.sort() #a>z
new_list_list = sorted(places, reverse=True) #z>a

print(list_copy) # sorteeritud
print(places) # originaal
print(new_list_list)


print()

# tühjenda list
new_list_list.clear()
print(new_list_list)

"""
ülesanne: kasuta originaal listi ja eemalda listist viimane Rapla
ilma [-1] kasutamata ning väljasta kolmanda elemendi keskmine täht suurtähena
"""


places.pop(len(places)-1)
print(places)
print(places[2][2].upper())


