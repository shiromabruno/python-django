
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

    # states_lower = {}
    # for key, value in states.items():
    #     states_lower[key.lower()] = value.lower()

    # print(states_lower)

    for listaitem in lista_city_state:
        estado_sigla = "nenhum" # variavel auxiliar que armazena ESTADO SIGLA, caso a listaitem eh uma CIDADE
        not_found = True #FLAG que nao achou, voltar ERRO
        if listaitem.title() in states: # IF de caso o listaitem eh um ESTADO
            capital_sigla = states[listaitem.title()]
            if capital_sigla in capital_cities:
                print (f'{capital_cities[capital_sigla]} is the capital of {listaitem.title()}')
                not_found = False
        else:
            for key, value in capital_cities.items(): # ELSE de caso o listaitem eh uma CIDADE
                if value == listaitem.title(): 
                    estado_sigla = key
            for key, value in states.items():
                if value == estado_sigla:
                    print(f'{listaitem.title()} is the capital of {key}')
                    estado_sigla = "nenhum"
                    not_found = False
        if not_found: # se entrou aqui, entao nao achou.
                print(f'{listaitem} is neither a capital city nor a state')
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

    #print(lista_entrada)
    #print(lista_final_com_strip)

    #if isinstance(arg1, str):
    main(lista_final_com_strip)
