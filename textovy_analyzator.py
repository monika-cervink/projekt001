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
print("Vítejte v našem textovém analyzátoru. "
      "Prosím zadejte přihlašovací údaje:")
REGISTROVANI = {"bob": "123",
                "ann": "pass123",
                "mike": "password123",
                "liz": "pass123"}
prepinac = True
while prepinac:
    username = input("USERNAME: ")
    heslo = input("HESLO: ")
    if username in REGISTROVANI and heslo == REGISTROVANI[username]:
        prepinac = False
    else:
        print("Neexistující uživatel nebo špatně zadané heslo.")
print(ODDELOVAC)
print(f"Počet textů v nabídce: {len(TEXTS)}")
print(f"Vyberte text pro analýzu (číslo od 1 do {len(TEXTS)}): ", end="")
try:
    VOLBA = int(input())

    while 0 >= VOLBA or VOLBA > len(TEXTS):
        print("Zvolené číslo textu nemáme v nabídce.")
        print(f"Vyberte text (číslo od 1 do {len(TEXTS)}): ", end="")
        VOLBA = int(input())

    print(ODDELOVAC)
    index = VOLBA - 1
    TEXT = TEXTS[index]
    OCISTENY_TEXT = [slovo.strip(".,") for slovo in TEXT.split()]
    print(f"V textu se nachází {len(OCISTENY_TEXT)} slov.")

    slova_velkym = []
    velka_pismena = []
    mala_pismena = []
    pocet_cisel = []
    vyskyt = {}
    for slovo in OCISTENY_TEXT:
        POCET_PISMEN = len(slovo)
        vyskyt[POCET_PISMEN] = vyskyt.get(POCET_PISMEN, 0) + 1
        if slovo.istitle() or slovo.isupper():
            slova_velkym.append(slovo)
        elif slovo.isupper():
            velka_pismena.append(slovo)
        elif slovo.islower():
            mala_pismena.append(slovo)
        elif slovo.isdigit():
            pocet_cisel.append(int(slovo))
    print(f"V textu se nachází {len(slova_velkym)} "
          f"slov začínajících velkým písmenem.")
    print(f"V textu se nachází {len(velka_pismena)} "
          f"slov psaných velkými písmeny.")
    print(f"V textu se nachází {len(mala_pismena)} "
          f"slov psaných malými písmeny.")
    print(f"V textu se nachází {len(pocet_cisel)} "
          f"číselných stringů.")
    print(ODDELOVAC)

    SERAZENY_VYSKYT = sorted(vyskyt.items())
    for pocet_pismen, pocet_slov in SERAZENY_VYSKYT:
        print(pocet_pismen, ("*" * pocet_slov), pocet_slov)
    print(ODDELOVAC)
    print(f"Součet všech čísel v textu je: {sum(pocet_cisel)}.")
    print(ODDELOVAC)
except ValueError:
    print("Zadávej číslice")
