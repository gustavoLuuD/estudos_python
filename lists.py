list = [123, "James", True] # Podemos criar listas mistas mas isso não é muito bom
numbers  = [78,900,1,4,5]
names = ["Jhon", "Jack", "Jill"]

print(list)                 # O python printa tudo como uma lista só sem precisarmos iterar sobre
print(numbers[0])           # Naturalmente podemos printar apenas um elemento pelo índice
print("Jhon" in names)      # Podemos checar se um valor está na lista

print(min(numbers))
print(max(numbers))

print("Numbers antes da ordenação", numbers)
numbers.sort()
print("Numbers depois da ordenação", numbers)
print(f"Temos {len(names)} nomes na lista")