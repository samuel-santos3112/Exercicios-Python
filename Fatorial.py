numero = int (input("Informe número a ser fatorado: "))
if numero == 1 or numero == 0:
    fatorial = 1
else:
    fatorial=1
    for i in range (1,numero+1):
        fatorial = fatorial* i   
print("Fatorial de",numero,"é: ",fatorial)