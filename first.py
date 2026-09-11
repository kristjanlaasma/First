import datetime # kuupäevade arvutamiseks
# see on kommentaar

"""
mitme realine
kommentaar
"""
# muutujate omistamine

name = "kristjan laasma"
age = 16
height = 1.85

print(name, age, height)
# kasutaja NAME vaunses AGE on pikkusega HEIGHT meetrit
print(f"kasutaja {name.title()} vanusega {age}a. on pikkusega {height} meetrit.")
print("kasutaja "+ name.title() + " vanusega "+ str(age) + "a. on pikkusega " + str(height) + " meetrit.")

# jooksev aasta
birth_year = datetime.date.today().year - age
print(f"sünniaasta {birth_year}")

age = int(input("Sisesta vanus: "))

if age < 1 or age > 122:
    print("Vanus on vales vahemikus (lubatud 1-122 k.a.)")
elif age < 18:
    print("alaealine")
elif age < 64:
    print("tööealine")
elif age < 100:
    print("pensionär")
else:
    print("pikaealine")
    
"""
küsime elukohta ja vastavalt elukoha nime pikkusele väljastame
lühike nimi(2-6 tähte)
pikk nimi(7- tähte)
"""
    
place = input("Sisesta elukoht: ")
place = place.strip() # eemaldab tühikud

if len(place) > 1 and len(place) <= 6 and place.isalpha():
    print(f"lühike nimi {place}")
elif len(place) > 6 and place.isalpha():
    print(f"pikk nimi {place}")
else:
    print("viga")
    
    
    
# substring (alamstringid)
# muutuja name = kristjan laasma
print(name)
print(name[1])		# väljund: r
print(name[1:5])		# väljund: rist
print(name[9:])		# väljund: laasma
print(name[:8])		# väljund: kristjan
print(name[::-1])		 # väljund: amsaal najtsirk


# muutujast name väljastage perekonna nime esimene täht suurelt
print(name[9].title())

# kolm andmetüüpi:
print(type(name))
print(type(age))
print(type(height))
