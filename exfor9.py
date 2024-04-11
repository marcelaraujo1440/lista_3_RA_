lista=[]

for i in range (0,10):
    lista.append(int(input("Digite um valor inteiro e positivo: ")))
print(f"Lista: {lista}")

lista.sort()
print(f'Lista em ordem crescente: {lista}')