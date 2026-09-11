from random import randint
names = ["Bob", "james", "joe", "mama"]

# väljasta listis olevad andmed nimed nime kaupa

for name in names:
    print(name) # väljasta nimi

print() # tühi rida

# sama lahendus nage enne, aga lisaks juhuslik vanus

for x in range(len(names)):
    print(x, names[x], randint(1, 122))

print()

for x in range(1, 5): 
    print(x, end=" ")
print("\n")

for x in range(0, 10, 2):
    print(x, end=" | ")
print("\n")

#while-loop
x = 0
while x < len(names):
    print(names[x])
    x += 1 # x = x + 1

# ülesanne: väljasta listi nimed konsooli ja iga nime ette pane järjekorra number koos punktiga. seega 
# 1. mari
# 2. anna

print()
 #lahendus 1
for x in range(len(names)):
    print(f"{x+1}. {names[x]}")
print()
#lahendus 2
#   x = 0

#   while x < len(names):
#    print(str(x+1) + ". " + names{x})
#        x +=1
