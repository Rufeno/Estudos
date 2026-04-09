print("Digite sua idade:")
idade = int(input())
print("Digite se voce é estudante ou não (S/N):")
estudante = input()

# Caso a idade seja igual a 18 ou ele ser estudante ele recebe um desconto de 50 do valor
if idade < 18 or estudante == "S":
    print("O valor do ingresso é R$ 10,00")

# Caso contrario ele paga o valor cheio
else:
    print("O valor do ingresso é R$ 20,00")
