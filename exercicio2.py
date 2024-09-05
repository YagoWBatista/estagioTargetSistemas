entrada = input("Escreva uma string a seguir: ")

soma = 0
for char in entrada:
    if char.lower() in "aáàâãäåăą": soma += 1

if soma == 0: print("Não há nenhum \"a\" na string inserida.")
else: print(f"Há {soma} \"a\"(s) na string inserida.")
