
import sys

def main():
    with open("periodic_table.txt", "r") as file:
        for linha in file:
            print(linha)
    return

if __name__ == '__main__':
    main()