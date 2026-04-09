# Valor dos itens
Valor_Hamburguer = 12
Valor_Coca = 5
Valor_Batata = 7

# quantidade de itens
Hamburguer = 0
Coca = 0
Batata = 0

print("Quantos hamburgueres deseja?")
Hamburguer = int(input())
print("Quantas cocas deseja?")
Coca = int(input())
print("Quantas batatas deseja?")
Batata = int(input())

# calculo do valor total
Valor_Total = (Valor_Hamburguer * Hamburguer) + (Valor_Coca * Coca) + (Valor_Batata * Batata)
print("O valor total do seu pedido é: " + str(Valor_Total))

print("Obrigado por comprar conosco!")
