# Loo skript mis küsib kasutajalt ringi raadiust. Kontrolli kas kasutaja sisestus jääks 1-10 (k.a.) piiridesse.
# Arvuta ringi pindala, ja ümbermõõt. Näita vastust raadius, pindala ja ümbermõõt.
from math import pi, pow

raadius = float(input("Sisesta Raadius: ")) 
if raadius >1 and raadius <10: 
    pindala = pow(raadius, 2) * pi 
    ümbermõõt = raadius * 2 * pi
    print(f"Raadius: {raadius}")
    print(f"Pindala: {pindala}")
    print(f"Ümbermõõt: {ümbermõõt}")
else: print("Viga! number peab olema 1-10 piiris.")

