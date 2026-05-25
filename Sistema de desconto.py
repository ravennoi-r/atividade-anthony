valor = float(input("Digite o valor da compra: R$ "))

if valor < 100:
    desconto_percentual = 0
elif valor < 500:
    desconto_percentual = 10
else:
    desconto_percentual = 15

desconto = valor * (desconto_percentual / 100)
valor_final = valor - desconto

print("\n===== RESULTADO =====")
print(f"Valor original: R$ {valor:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")