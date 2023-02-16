valor = float(input("Valor da casa: "))
salario = float(input("Salário: "))
anos = int(input("Em quantos anos vai pagar: "))

prestacao = valor / (anos*12)
print(f"Prestação {prestacao:.2f}")
if prestacao <= 0.3 * (salario):
    print(f"O empréstimo foi \33[1;42m liberado\33[m")
else:
    print(f"O empréstimo foi \33[1;41m negado\33[m")