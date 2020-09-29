TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

ODDELOVAC = "-" * 40
print(ODDELOVAC)
print("Vítejte v našem textovém analyzátoru. Prosím zadejte přihlašovací údaje:")
REGISTROVANI = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
prepinac = True
while prepinac:
    USERNAME = input("USERNAME: ")
    HESLO = input("HESLO: ")
    if USERNAME in REGISTROVANI:
        kontrola = REGISTROVANI[USERNAME]
        if kontrola == HESLO:
            prepinac = False
        else:
            print("Zadané heslo není správné.")
    else:
        print("Uživatel nenalezen.")
print(ODDELOVAC)
print(f"Počet textů v nabídce: {len(TEXTS)}")
print(f"Vyberte text pro analýzu (číslo od 1 do {len(TEXTS)}): ", end="")
VOLBA = int(input())

while 0 >= VOLBA or VOLBA > len(TEXTS):
    print("Zvolené číslo textu nemáme v nabídce.")
    print(f"Vyberte text (číslo od 1 do {len(TEXTS)}): ", end="")
    VOLBA = int(input())

print(ODDELOVAC)
index = VOLBA - 1
TEXT = TEXTS[index]
OCISTENY_TEXT = TEXT.strip(".,").split()
print(f"V textu se nachází {len(OCISTENY_TEXT)} slov.")

SLOVA_VELKYM = []     # slova začínající velkým písmenem
VELKA_PISMENA = []    # slova psaná velkými písmeny
MALA_PISMENA = []     # slova psaná malými písmeny
POCET_CISEL = []
for slovo in OCISTENY_TEXT:
    if slovo.istitle() or slovo.isupper():
        SLOVA_VELKYM.append(slovo)
    if slovo.isupper():
        VELKA_PISMENA.append(slovo)
    if slovo.islower():
        MALA_PISMENA.append(slovo)
    if slovo.isdigit():
        POCET_CISEL.append(int(slovo))
print(f"V textu se nachází {len(SLOVA_VELKYM)} slov začínajících velkým písmenem.")
print(f"V textu se nachází {len(VELKA_PISMENA)} slov psaných velkými písmeny.")
print(f"V textu se nachází {len(MALA_PISMENA)} slov psaných malými písmeny.")
print(f"V textu se nachází {len(POCET_CISEL)} číselných stringů.")
print(ODDELOVAC)

VYSKYT = {}
for slovo in OCISTENY_TEXT:
    POCET_PISMEN = len(slovo)
    VYSKYT[POCET_PISMEN] = VYSKYT.get(POCET_PISMEN, 0) + 1
SERAZENY_VYSKYT = sorted(VYSKYT.items())

for pocet_pismen, pocet_slov in SERAZENY_VYSKYT:
    print(pocet_pismen, ("*" * pocet_slov), pocet_slov)
print(ODDELOVAC)
print(f"Součet všech čísel v textu je: {sum(POCET_CISEL)}.")
print(ODDELOVAC)
