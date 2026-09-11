# game.py
"""
ära arvamise mäng. mõeldud numbrid on on 1-100.
loetakse samme. mängul on tagauks (1000)
TÄIENDUS: mängu lõppedes küdi kasutajalt kas soovid veel mängida kui jah(J, j. Y)
siis reseti andmed ja alusta uus mäng
"""
from random import randint

pc_nr = randint(1, 100) # arvuti mõeldud number
steps = 0 # sammude lugeja
game_over = False # kas mäng on läbi?


#print(pc_nr) #TEST

def ask():
    global steps, game_over  # globaalsed muutujad
    user_nr = int(input("Sisesta number: "))
    steps +=1 # sammud kasvavad +1
        
    if user_nr > pc_nr and user_nr != 1000:
        print("Väiksem")

    elif user_nr < pc_nr and user_nr != 1000:
        print("Suurem")

    elif user_nr == pc_nr and user_nr != 1000:
        game_over = True
        print(F"Arvasid numbri ära {steps} sammuga.")


    elif user_nr == 1000:
        print(f"leidsin mu nõrga koha, number on {pc_nr}")
        

def lets_play():
    while not game_over:
        ask()
    play_again()

def play_again():
    global steps, pc_nr, game_over        
    print("Game over")
    user_answer = input("Kas soovid uuesti mängida? [J/E]")
    if user_answer == "J" or user_answer == "j":
        print("Uus mäng")
        steps = 0
        pc_nr = randint(1, 100)
        game_over = False
        lets_play()
    
        
lets_play()

  