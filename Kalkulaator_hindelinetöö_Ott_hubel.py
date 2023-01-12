import math

# See funktsioon liidab kaks arvu
def add(x, y): # Defineerib liitmist
    return x + y # Väljastab tulemuse

# See funktsioon lahtuab kaks arvu
def subtract(x, y): # Defineerib lahtuamist
    return x - y # Väljastab tulemuse


# See funktsioon korrutab kaks arvu
def multiply(x, y): # Defineerib korrutamist
    return x * y # Väljastab tulemuse


# See funktsioon jagab kaks arvu
def divide(x, y): # Defineerib jagamist
    return x / y  # Väljastab tulemuse



print("Valige arvutusviis.") # Väljastab erinevate kalkulatsioonide võimalused
print("1.Liitmine")
print("2.Lahutamine")
print("3.Korrutamine")
print("4.Jagamine")


while True: # Juhul kui on tõene
    choice = input("Sisestage valik(1/2/3/4): ") # Kasutajalt küsitakse kalkulatsiooni tüübi valikut

    if choice in ('1', '2', '3', '4'): # Juhul kui valik on üks nendest numbritest
        try:
            num1 = float(input("Sisestage esimene number: ")) # Kasutaja sisestab esimese numbri
            num2 = float(input("Sisestage teine number: ")) #  Kasutaja sisestab teise numbri
        except ValueError: # Kood kontrollib kas kasutaja sisestas numbrid
            print("Ebasobilik sisestus. Palun sisestage number.") # Juhul kui kasutaja sisestab midagi muud peale numbri väljastab programm veateate ning küsib uuesti
            continue # Kood jätkub

        if choice == '1': # Juhul kui valikuks on 1
            print(num1, "+", num2, "=", add(num1, num2)) # Kood liidab kasutaja sisestatud arvud

        elif choice == '2': # Juhul kui valikuks on 2
            print(num1, "-", num2, "=", subtract(num1, num2)) # Kood lahutab kasutaja sisestatud arvud

        elif choice == '3': # Juhul kui valikuks on 3
            print(num1, "*", num2, "=", multiply(num1, num2)) # Kood korrutab kasutaja sisestatud arvud

        elif choice == '4': # Juhul kui valikuks on 4
            print(num1, "/", num2, "=", divide(num1, num2)) # Kood jagab kasutaja sisestatud arvud


        next_calculation = input("Kas teeme järgmise kalkulatsiooni? (jah/ei): ") # Kood küsib kasutajalt kas
        if next_calculation == "ei": # Juhul kui vastuseks on ei
            break # Lõpetab tsükkli
    else: # Muul juhul
        print("Ebasobilik sisestus") # Väljastab veateate ning küsib uuesti

def round_off(): # Defineerib funktsiooni ümardamine
    num = float(input("Sisestage arv: ")) # Küsib kasutajalt arvu
    decimals = int(input("Mitme komakohani soovite arvu ümardada?: ")) # Küsib kasutajalt kuhu maani ümardada
    return round(num, decimals) # Kood kalkuleerib

print(round_off()) # Kood väljastab tulemuse

next_calculation = input("Kas teeme järgmise kalkulatsiooni? (jah/ei): ") # Kood küsib kasutajalt kas kasutaja tahab veel kalkulaatorit kasutada

def find_square_root(): # Defineerib funktsiooni ruutjuur
    num = float(input("Sisestage arv: ")) # Kasutaja sisestab arvu
    return math.sqrt(num) # Kood kalkuleerib

print(find_square_root()) # Kood väljastab tulemuse