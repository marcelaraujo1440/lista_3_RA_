fora= 0
intervalo= 0
lista=[]
for i in range(1,11):
    num= int(input(f"Digite o seu {i} número inteiro e positivo: "))

    i+=1
    if num  <10 or num >=20:
        fora+=1
    if num >=10 and num<20:
        intervalo+=1
print(f"A quantidade de números dentro do intervalo [10,20] é de {intervalo}")
print(f"A quantidade de números fora do intervalo [10,20] é de {fora}")