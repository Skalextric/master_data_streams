import numpy as np

test = np.array([1,1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,8,9,9,9,9,9,9,9,9,9,10,10,10,10])


print np.var([3,4,3,3,3,3,4,])
#print sum(np.histogram(test)[0])/4


lista = 'abceebdabaeedbdbabdcecdeabdbacedddacbbeabbcdacbeab'
counting = lista
print counting
print len(counting)
print counting.count('a')
print counting.count('b')
print counting.count('c')
print counting.count('d')
print counting.count('e')