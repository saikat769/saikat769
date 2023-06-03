num = int(input(" enter the decimal number: "))
bi = ""

if num == 0:
    print("binary: ",0)
while num > 0:
    bi = str(num % 2) + bi
    num = num // 2
print(bi)
