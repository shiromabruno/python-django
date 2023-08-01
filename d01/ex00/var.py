
def my_var():

    variavel_int = 42
    print(f"{variavel_int} has a type {type(variavel_int)}")

    variavel_string = "42"
    print(f"{variavel_string} has a type {type(variavel_string)}")

    variavel_quarante = "quarante-deux"
    print(f"{variavel_quarante} has a type {type(variavel_quarante)}")

    variavel_float = 42.0
    print(f"{variavel_float} has a type {type(variavel_float)}")

    variavel_bool = True
    print(f"{variavel_bool} has a type {type(variavel_bool)}")

    variavel_lista = [42]
    print(f"{variavel_lista} has a type {type(variavel_lista)}")

    #thisdict =	{"brand": "Ford", "model": "Mustang", "year": 1964}
    variavel_dict = {42:42}
    print(f"{variavel_dict} has a type {type(variavel_dict)}")

    #mytuple = ("apple", "banana", "cherry")
    variavel_tuple = (42,)
    print(f"{variavel_tuple} has a type {type(variavel_tuple)}")

    variavel_set = set()
    print(f"{variavel_set} has a type {type(variavel_set)}")

if __name__ == '__main__':
    my_var()