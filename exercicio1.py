entrada = int(input("Por favor, insira o número que deseja encontrar na sequência de Fibonacci: "))

aNum = 0
bNum = 1

while(entrada >= aNum):
    if aNum == entrada:
        print("Esse número pertence à sequência de Fibonacci.")
        break
    else:
        abSum = aNum + bNum
        aNum = bNum
        bNum = abSum
    
if(entrada < aNum):
    print("Esse número não pertence à sequência de Fibonacci.")
