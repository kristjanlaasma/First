
# Täiendus: loenda kokku mitu numbrit kokku liidetakse ja näita vastust

filename = "create-MyCSV-v.csv"
total = 0 # kogu veeru summa
count = 0
# loe kokku mitu veergu on failis


f = open(filename, "r") # ava fail lugemiseks
rows = len(f.readline().split(";")) # mitu elementi reas
f.close() # sulge fail

row = int(input(f"Mitmes veerg kokku liita? 1-{rows}: "))

if row >= 1 and row <= rows:
    row -= 1 # row = row -1
    
    with open(filename, "r") as f:
        content = f.readlines()
        for line in content:
            line = line.strip() # korrasta rida
            parts = line.split(";")
            if parts[row].isnumeric():
                total += int(parts[row])
                count += 1 

           
            print(total, count)
          

else:
    print("Vigane veeru number")

 