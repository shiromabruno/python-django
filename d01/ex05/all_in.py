
import sys

def main(lista_city_state):
    
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
   }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    return
        

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit()

    arg1 = sys.argv[1]
    
    lista_entrada = arg1.split(",")
    lista_final_com_strip=[]

    for nome in lista_entrada:
        if nome.strip() != "":
            lista_final_com_strip.append(nome.strip())

    print(lista_entrada)
    print(lista_final_com_strip)
    if isinstance(arg1, str):
        main(arg1)
