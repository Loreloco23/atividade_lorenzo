def desconto(A):
    return A * 0.10   # 10% = 0.10, ou 0.01 se for 1%

A = int(input("Escreva número 1: "))

b = A - desconto(A)

print(f"O desconto de {A} é = {desconto(A)}")
print(f"O valor com desconto de {A} é = {b}")