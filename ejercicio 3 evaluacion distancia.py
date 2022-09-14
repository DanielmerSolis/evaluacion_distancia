igual, aux = 0, 0

palabra = input("Ingrese la palabra que quiera determinar si es o no un palindromo: ")

for ind in reversed(range(0, len(palabra))):
  if palabra[ind].lower() == palabra[aux].lower():
    igual += 1
  aux += 1

if len(palabra) == igual:
  print("La palabra es palindromo!")
else:
  print("La palabra no es palindromo!")