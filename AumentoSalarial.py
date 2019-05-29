salario = float(input("Informe salário: "))

if salario <= 280:
    salarioAtualizado = salario *1.2
    percentual = 20
    aumento = salarioAtualizado - salario
    if salario > 280 and salario <=700:
        salarioAtualizado=salario *1.15
        percentual = 15
        aumento = salarioAtualizado - salario
        if salario > 700 and salario <=1500:
            salarioAtualizado= salario*1.1
            percentual = 10
            aumento = salarioAtualizado - salario
            if salario > 1500:
                salarioAtualizado=salario*1.05
                percentual = 5
                aumento = salarioAtualizado - salario

print("Salario: R$",round(salario,2),"\nPercentual aumento:",percentual,"%\nValor aumento: R$",round(aumento,2),
    "\nSalario Atualizado",round(salarioAtualizado,2))
