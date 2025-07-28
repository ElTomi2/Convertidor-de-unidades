#Falta implementar unidades de distancia
print("Convertidor de Unidades\n")
outvalue = None
inunit = input("Cuál es la unidad de entrada? (Celcius o Fahrenheit, Kelvin; Metros, Pies o Millas)\n").title()
while inunit != "Celcius" and inunit != "Fahrenheit" and inunit != "Kelvin":
    inunit = input("Ingrese una unidad válida\n")
while True:
    try:
        inval = float(input("Y el valor?\n"))
        break
    except ValueError:
        print("Ingrese un valor válido")
if inunit == "Celcius" or inunit == "Fahrenheit" or inunit == "Kelvin":
    tipo_unit = "Temp"
    outunit = input("A que unidad convertir?\n").title()
    while outunit != "Celcius" and outunit != "Fahrenheit" and outunit != "Kelvin":
        outunit = input("Ingrese una unidad de temperatura válida. ")
    match outunit:
        case "Celcius":
            if inunit == "Fahrenheit":
                outvalue = (inval-32)*5/9
            elif inunit == "Kelvin":
                outvalue = inval - 273.15
            else:
                outvalue = inval
        case "Fahrenheit":
            if inunit == "Celcius":
                outvalue = (inval*9/5)+32
            elif inunit == "Kelvin":
                outvalue = ((inval-273.15)*9/5)+32
            else:
                outvalue = inval
        case "Kelvin":
            if inunit == "Celcius":
                outvalue = inval + 273.15
            elif inunit == "Fahrenheit":
                outvalue = (inval -32)*5/9 + 273.15
            else:
                outvalue = inval

print("Resultado:")
if tipo_unit == "Temp":
    print(str(inval) + "° " + inunit + " a " + str(round(outvalue, 2)) +"° " + outunit)