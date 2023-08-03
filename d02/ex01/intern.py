class Intern:

    #Name = "" --> nao precisa, ja definido no construtor

    #constructor = __init__
    # o nome_padrao sera um valor DEFAULT. Se nao passar nenhuma string n construtor, ele assumira o valor padrao. Caso contrario, o nome sera o Nome passado no construtor.
    def __init__(self, nome_padrao="My name? I’m nobody, an intern, I have no name."):
        self.Name = nome_padrao

    #The __str__() method returns string representation of an object. This method is called by the built-in print(), str(), and format()
    # quando da o print(objeto), ele executa o STR, se nao tiver, ele volta tipo: <__main__.ClasseX object at 0x000001DBB695FB50>
    def __str__(self):
        return self.Name
    
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return Coffee()


class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."
    

if __name__ == '__main__':
    noname = Intern()
    print(noname)

    mark = Intern("Mark")
    print(mark)
    #print(mark.Name)

    cafe_mark = mark.make_coffee()
    print(cafe_mark) 

    try:
        noname.work()
    except Exception as ex:
        print (ex)
    
