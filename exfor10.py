lista= [2,4,7,2,3,3,1,0,2,6]
num_rep= 0
num_freqq=0
for num in lista:
    if lista.count(num)> num_freqq:
        num_freqq+=1
        num_rep=num
print(f"O número que mais se repete é o {num_rep}")