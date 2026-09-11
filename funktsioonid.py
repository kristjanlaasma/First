# funktsioonid.py

def welcome():
    print("Tere, kuidas läheb")


def welcome_name(name):
    return f"Tere, {name}! "


def division(number1, number2):
    """teosta kahe arvu jagamist"""
    if number2 != 0:
        return number1 / number2
    return -1


def introduce(name, age=20):
    """ 
    loob lihtsa jutustava lause

    :param name: str isiku nimi
    :param age: int isiku vanus (vaikimisi 20)
    :return: tekstiline tutvustav lause
    :rtype: string
    """
    return f"Tema on {name} ja ta on {age} aastane!"





welcome()
for x in range(3):
    welcome()

print()

print(welcome_name("Joe"))
names = ["Joe", "Joe mama", "Pedro"]
for nimi in names:
    print(welcome_name(nimi))
print(welcome_name(1234))
print(welcome_name(""))
print()


print(division(1, 4))
print(division(10, 0))
print(division(0, 10))

print(introduce("Joe", 60))
print(introduce("monkey"))
print(introduce(""))
print(introduce(1234, 13))
print(introduce(age=99, name="vanamutt"))

print(division(number2= 10, number1= 100))

