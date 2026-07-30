validos: tuple[str, ...] = (
    "Celcius",
    "Fahrenheit",
    "Kelvin",
    "Kilometros",
    "Centimetros",
    "Metros",
    "Millas",
    "Pies",
    "Pulgadas")

print("Convertidor de Unidades\n")
outvalue = None
inunit: str = input("""Cuál es la unidad de entrada?
Distancia:
    Metros
    Centimetros
    Kilometros
    Pulgadas
    Pies
    Millas
Temperatura:
    Celcius
    Fahrenheit
    Kelvin\n""").title().strip()

while inunit not in validos:
    inunit: str = input("Ingrese una unidad válida\n").title().strip()

while True:
    try:
        inval = float(input("Y el valor?\n"))
        break
    except ValueError:
        print("Ingrese un valor válido")
        
outvalue = inval

if inunit in validos[0:3]:
    tipo_unit = "Temp"
    outunit: str = input("A que unidad convertir?\n").title().strip()
    while outunit not in validos[0:3]:
        outunit: str = input("Ingrese una unidad de temperatura válida. ").title().strip()
    match outunit:
        case "Celcius":
            if inunit == "Fahrenheit":
                outvalue = (inval-32)*5/9
            elif inunit == "Kelvin":
                outvalue = inval - 273.15
        case "Fahrenheit":
            if inunit == "Celcius":
                outvalue = (inval*9/5)+32
            elif inunit == "Kelvin":
                outvalue = ((inval-273.15)*9/5)+32
        case "Kelvin":
            if inunit == "Celcius":
                outvalue = inval + 273.15
            elif inunit == "Fahrenheit":
                outvalue = (inval -32)*5/9 + 273.15
elif inunit in validos[3:9]:
    tipo_unit = "Dist"
    outunit = input("A que unidad convertir?\n").title().strip()
    while outunit not in validos[3:9]:
        outunit = input("Ingrese una unidad de distancia válida. ").title().strip()
    match outunit: #Dependiendo de la salida elegida.
        case "Kilometros":
            match inunit: #Busca como transformar la entrada.
                case "Metros":
                    outvalue = inval/1000
                case "Centimetros":
                    outvalue = inval/100000
                case "Millas":
                    outvalue = inval*1.609
                case "Pies":
                    outvalue = inval/3280
                case "Pulgadas":
                    outvalue = inval/39370
        case "Centimetros":
            match inunit:
                case "Kilometros":
                    outvalue = inval*100000
                case "Metros":
                    outvalue = inval*100
                case "Millas":
                    outvalue = inval*160934
                case "Pies":
                    outvalue = inval*30.48
                case "Pulgadas":
                    outvalue = inval*2.54
        case "Metros":
            match inunit:
                case "Kilometros":
                    outvalue = inval*1000
                case "Centimetros":
                    outvalue = inval/100
                case "Millas":
                    outvalue = inval*1609
                case "Pies":
                    outvalue = inval/3.28
                case "Pulgadas":
                    outvalue = inval/39.37
        case "Millas":
            match inunit:
                case "Kilometros":
                    outvalue = inval/1.61
                case "Centimetros":
                    outvalue = inval/160900
                case "Metros":
                    outvalue = inval/1609
                case "Pies":
                    outvalue = inval/5280
                case "Pulgadas":
                    outvalue = inval/63360
        case "Pies":
            match inunit:
                case "Kilometros":
                    outvalue = inval*3280.84
                case "Centimetros":
                    outvalue = inval/30.48
                case "Metros":
                    outvalue = inval*3.281
                case "Millas":
                    outvalue = inval*5280
                case "Pulgadas":
                    outvalue = inval/12
        case "Pulgadas":
            match inunit: 
                case "Kilometros":
                    outvalue = inval*39370
                case "Centimetros":
                    outvalue = inval/2.54
                case "Metros":
                    outvalue = inval*39.37
                case "Millas":
                    outvalue = inval*63360
                case "Pies":
                    outvalue = inval*12

print("Resultado:")
if tipo_unit == "Temp":
    print(f"{inval}° {inunit} a {round(outvalue, 2)}° {outunit}")
    #print(str(inval) + "° " + inunit + " a " + str(round(outvalue, 2)) +"° " + outunit)
elif tipo_unit == "Dist":
    print(f"{inval} {inunit} a {outvalue} {outunit}")
    #print(str(inval)+ " " + inunit + " a " + str(round(outvalue, 2))+ " " + outunit)
