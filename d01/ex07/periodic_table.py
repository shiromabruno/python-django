
import sys

def main():

    d = {
    'Hendrix': '1942',
    'Allman': '1946',
    'King': '1925',
    'Clapton': '1945',
    'Johnson': '1911',
    'Berry': '1926',
    'Vaughan': '1954',
    'Cooder': '1947',
    'Page': '1944',
    'Richards': '1943',
    'Hammett': '1962',
    'Cobain': '1967',
    'Garcia': '1942',
    'Beck': '1944',
    'Santana': '1947',
    'Ramone': '1948',
    'White': '1975',
    'Frusciante': '1970',
    'Thompson': '1949',
    'Burton': '1939',
}

    #sort_dictionary = sorted(d.items()) # faz sort pelo KEY  e volta o DICTIONARY COMPLETO
    #sort_dictionary = sorted(d.values()) # faz sort pelo VALUES apenas e volta o VALUES 

    # o LAMBDA: cada musico sera comparado com outro musico primeiramente pelo ANO [0] e depois pelo NOME [1]
    sort_dictionary = sorted(d.items(), key=lambda musico: (musico[1], musico[0]))
    #print(sort_dictionary)

    for musician in sort_dictionary: # LIST de tupla
        print(musician[0]) #printa primeiro elemento da tupla

    return

if __name__ == '__main__':
    main()