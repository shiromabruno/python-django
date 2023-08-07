import sys
import antigravity

def main(latitude, longitude, dowjones):

    print(f'latitude eh: {latitude}') # latitude eh: -23.5489
    print(f'longitude eh: {longitude}') # longitude eh: -46.6388
    print(f'dow_jones eh: {dowjones}') # dow_jones eh: b'10458.69'

    try:
        coordenada_final = antigravity.geohash(latitude, longitude, dowjones) # aparece -23.308792 -46.803754
        # print(coordenada_final) # None
    except  Exception as ex:
        print(f'Error no antigravity.geohash: {ex}')
    

if __name__ == '__main__':

    # python3 geohashing.py -23.5489 -46.6388 10458.68

    if len(sys.argv) != 4:
        print("Atencao, necessario 4 argumentos NESSA ORDEM: geohashing.py + latitude + longitude + dowopening")
        sys.exit()

    try:
        latitude = float(sys.argv[1]) # precisa ser number, senao: %d format: a number is required, not str
        longitude = float(sys.argv[2])
        dow_jones = (sys.argv[3]).encode('utf-8')  # Precisa do utf-8, senao: Unicode-objects must be encoded before hashing

        main(latitude, longitude, dow_jones)
    except  Exception as ex:
        print(f'Error na captura dos parametros: {ex}')

    
