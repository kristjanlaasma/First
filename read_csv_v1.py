

filename = "create-MyCSV-v.csv"
row = 9 # mitmes veerg kokku liita
total = 0 # kogu veeru summa

f = open(filename, "r") # ava fail lugemiseks
content = f.readlines()
f.close() # sulge fail

for line in content:
    line = line.strip() # korrasta rida
    parts = line.split(";")
    if parts[row].isnumeric():
        total += int(parts[row])
        #print(line)

   #print(parts) # väljasta rea elemendid (list)
    print(total)
 