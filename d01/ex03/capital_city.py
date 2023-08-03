
import sys

def main(find_state):
    
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

    if find_state in states:
        capital_sigla = states[find_state]
        if capital_sigla in capital_cities:
            print (capital_cities[capital_sigla])
            return
        
    print ("Unknown state")
    return
        

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit()

    arg1 = sys.argv[1]
    main(arg1)


