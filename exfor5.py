par= 0
impar= 0
lista=[]
for i in range(1,11):
    num= int(input(f"Digite o seu {i} número inteiro e positivo: "))

    i+=1
    if num %2 == 0:
        par+=1
    else:
        impar+=1
print(F"Você digitou um total de {par} números pares")
print(F"Você digitou um total de {impar} números impares")