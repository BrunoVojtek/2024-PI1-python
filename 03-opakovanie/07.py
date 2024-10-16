n = int (input ("Zadaj n: "))
for i in range ( n):
    i = i*i
if i % 2 == 0:
    print(i)
else:
    print(i-1)
