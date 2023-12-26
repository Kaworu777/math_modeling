a = int(input("vvedite god"))
if a % 4 == 0 and a % 100 != 0 and a % 400 != 0:
    print("visokosniy")
else:
    print("nevisokosniy")
    