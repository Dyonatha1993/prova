altura = float(input("digite altura"))
peso = float(input("digite o peso"))

imc = round(peso/altura**2)
if imc < 18.50:
    print("Abaixo do Peso", imc)
elif imc < 25:
    print("Peso Normal", imc)
elif imc > 25 and imc < 30:
    print("Sobrepeso", imc)
else:
    print("obeso", imc)
