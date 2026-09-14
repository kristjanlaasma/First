import datetime
"""
Täiendus 1: näita ainult neid isikuid kes on 100 ja rohkem vanad
Täiendus 2: näita nendele isikutele sünniaastat ( kasuta datetime )
"""
filename = "create_file.txt"

with open(filename, "r", encoding="utf-8") as f:
    contents = f.readlines()  #loe kõik faili read listi
    for line in contents:
     line = line.strip() #korrasta rida
     name = line.split(";")[0] # nimi
     age = int(line.split(";")[1]) # teeb vanuse täisarvuks, muidu string
     if age >= 100:
        birth_year = datetime.date.today().year - age
        print(name, age, birth_year)
        
     # print(type(name), type(age)) # näita nime ja vanuse tüüpi