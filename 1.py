num_verify = input("Insira um número para verificar se pertence à sequência de Fibonacci ->")
num_verify = int(num_verify)

def fibonacci(num_verify):
    if num_verify == 0:
        return True
    a, b = 0, 1
    while a < num_verify:
        a, b = b, a + b
        if a == num_verify:
            return True
    return False

if fibonacci(num_verify):
    print(f"O número {num_verify} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num_verify} não pertence à sequência de Fibonacci.")
