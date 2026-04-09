print("Digite sua idade:")
idade = int(input())
print("Digite se voce é estudante ou não (S/N):")
estudante = input()
preco_ingresso = 20

# Caso a idade seja igual a 18 ou ele ser estudante ele recebe um desconto de 50 do valor
if idade < 18 or estudante == "S":
    print(f"O valor do ingresso é R$ {preco_ingresso * 0.5:.2f}")

# Caso contrario ele paga o valor cheio
else:
    print(f"O valor do ingresso é R$ {preco_ingresso:.2f}")
