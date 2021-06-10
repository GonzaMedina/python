multiplo2 = 0
multiplo3 = 0
multiplo4 = 0

for i in range(6,60):
    if(i % 2 == 0):
        multiplo2 += i
    if(i % 3 == 0):
        multiplo2 += i
    if(i % 4 == 0):
        multiplo2 += i

print('2', multiplo2)
print('3', multiplo3)
print('4', multiplo4)

print(multiplo2 + multiplo3 - multiplo4)
