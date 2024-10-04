def buscar_fibonacci(num):
  if (num == 0 or num == 1): 
    return True
  
  penultimo = 0
  ultimo = 1
  atual = 0

  while (num > atual):
    atual = ultimo + penultimo
    penultimo = ultimo
    ultimo = atual

    print(f"{atual}")

  if (num == ultimo or num == atual):
    return True
  else:
    return False

num = int(input("Digite um valor para ser buscado na sequência de Fibonacci: "))

if (buscar_fibonacci(num)):
  print(f"O número {num} existe na sequência de Fibonacci.")
else:
  print(f"O número {num} não existe na sequência de Fibonacci.")