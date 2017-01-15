import argparse
import random

ap = argparse.ArgumentParser()
ap.add_argument("-X", "--exclude", help="Numero a excluir ", type=int,  default=1)
ap.add_argument("-N", "--N", help="Numeros", type=int, default = 100)

args = vars(ap.parse_args())

exclude = args["exclude"]
lista = range(1, args["N"] + 1)
random.shuffle(lista)

nombre_fichero = "{}_elementos_falta_{}.txt".format(args["N"], exclude)
with open(nombre_fichero, 'w') as f:
    for number in lista:
        if number != exclude:
            f.write(str(number)+'\n')
