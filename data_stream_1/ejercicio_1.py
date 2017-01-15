import argparse
import time
import resource

ap = argparse.ArgumentParser()
ap.add_argument("-F", "--file", help="Archivo a tratar ", required=True)
args = vars(ap.parse_args())

start_time = time.time()
N = 0
suma = 0
with open(args["file"], 'r') as f:
        for line in f:
            data = line.strip()
            N += 1
            suma += int(data)

N += 1
gauss = ((N + 1)*N)/2
memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000

print "El numero faltante es {} en un total de {}".format((gauss-suma), N)
print "El tiempo empleado es {} segundos y un consumo de memoria de {}MB".format(time.time()- start_time, memory)
