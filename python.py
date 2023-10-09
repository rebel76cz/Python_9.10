def cti_a_pridej_jmena():
    with open('names.txt', 'a') as soubor:
        nova_jmena = ["Martin Hruška", "Pepa Uličný", "Erik Kocour"]
        for jmeno in nova_jmena:
            soubor.write(jmeno + '\n')

def pocet_slov_ve_souboru():
    with open('names.txt', 'r') as soubor:
        obsah = soubor.read()
        slova = obsah.split()
        pocet_slov = len(slova)
        return pocet_slov

def vytvor_a_zapis_slovnik(): 
    data = {
        'Jméno': 'Pepa',
        'Věk': 40,
        'Město': 'Kolín'
    }
    
    with open('slovnik.txt', 'w') as soubor:
        soubor.write(str(data))

cti_a_pridej_jmena()
pocet_slov = pocet_slov_ve_souboru()
print(f"Počet slov v 'names.txt' je: {pocet_slov}")
vytvor_a_zapis_slovnik()
