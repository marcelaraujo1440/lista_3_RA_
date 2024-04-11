
num= int(input("Digite um numero entre 1 e 10: "))
if num > 10: 
    print('inválido')
    
else:
    for i in range (0,11):
        print(f"{num} x {i} = {num * i}")
   
    