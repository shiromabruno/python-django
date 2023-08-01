
def inicio_leitura():

    # daria para usar dessa forma tambem: my_file = open("numbers.txt", "r")
    with open("numbers.txt", "r") as file:

        #The split() method splits a string at the specified separator and returns a list of substrings.
        numbers = file.read().split(",")

        #The strip() method returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).
        for number in numbers:
            print(number.strip())
   
    

if __name__ == '__main__':
    inicio_leitura()