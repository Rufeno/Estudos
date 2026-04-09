print("Bem-vindo ao nosso servico de delivery! Vamos calcular o valor do seu pedido.")
print("Quantos KM serao percorridos para a entrega?")
km = float(input())
print("Esta chovendo? (S/N)")
chovendo = input()

if km <= 5:
    valor_entrega = 5
elif km > 5 and km <= 10:
    valor_entrega = 8
elif km > 10 and km <= 20:
    valor_entrega = 10

if chovendo == "S":
    valor_entrega += 2

print(f"O valor da entrega é R$ {valor_entrega:.2f}")
