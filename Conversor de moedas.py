def converter_reais_para_dolares(valor_reais, taxa_cambio=5.0):
    return valor_reais / taxa_cambio

def main():
    print("Bem-vindo ao conversor de moedas! Vamos converter o valor em reais para dólares.")
    valor_reais = float(input("Digite o valor em reais: "))
    valor_dolares = converter_reais_para_dolares(valor_reais)
    print(f"O valor em dólares é: ${valor_dolares:.2f}")

if __name__ == "__main__":
    main()