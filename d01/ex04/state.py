
import sys

def main(find_city):
    
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

    estado_sigla = "nenhum"
    for key, value in capital_cities.items():
        if value == find_city:
            estado_sigla = key

    for key, value in states.items():
        if value == estado_sigla:
            print(key)
            return
        
    print ("Unknown capital city")
    return
        

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit()
        
    arg1 = sys.argv[1]
    main(arg1)


