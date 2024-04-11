num= int(input("Digite um numero: "))
div=[]
for i in range(1, num+1):#o 1 esta aq para que o numero que o usuario digitar esteja incluso
    if num% i == 0: # o "i" significa os valores que serao divididos pelo num digitado pelo usuario e cada vez que o resto for zero sera acrescentado na lista div
        div.append(i)
print(f'Os divisores desse {num} número: {div}')
        
    