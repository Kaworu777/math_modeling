a = int(input("vvedite perviy 4len: "))
b = int(input("vvedite znamenatel: "))
stop = int(input("vvedite koli4estvo: "))
for n in range(0, stop, 1):
    print(a*b**(n-1))
    