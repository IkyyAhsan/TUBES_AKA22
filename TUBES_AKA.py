import time
MAX = 1000000
def duapangkat(n):
    i = 1
    p = 0
    while (n>p) :
        n = n-1
        i = i * 2
    return i    

def dua_pangkat(n):
    if (n == 0) :
        return 1
    else:
        return ((dua_pangkat(n-1))*2)

j = 1
while j <= 10:
    start = time.time()
    print(duapangkat(j))
    end = time.time()
    print("Iteratif 2 pangkat :",(end-start) * 10 ** 3, "ms")
    print(" ")
    
    start2 = time.time()
    print (dua_pangkat(j))
    end2 = time.time()
    print("Rekursif 2 pangkat :",(end2-start2) * 10 ** 3, "ms")
    print(" ")
    j += 1