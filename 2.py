string_verify = input("Insira uma string ->")

a_count = 0

for char in string_verify:
    if char == "a" or char == "A":
        a_count += 1

if a_count > 0:
    print(f"A string inserida possui {a_count} caractere(s) 'a' ou 'A'.")
else:
    print("Não há nenhum caractere 'a' ou 'A' na string inserida.")
