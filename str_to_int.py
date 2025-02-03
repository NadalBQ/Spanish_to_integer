
number_set = {"uno", "un", "ún", "dos", "tres", "cuatro", "cinco", "seis", "siete", "sete", "ocho", "nueve", "nove", "diez", "diec", "once", "doce", "trece", "catorce", "quince", "veinte", "veint", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa", "cien", "quinien", "mil"}
sumadores = {"y", "i", "to", "tos", "es"}
unidades = {"uno", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "sete", "ocho", "nueve", "nove"}
decenas = {"diez", "diec", "once", "doce", "trece", "catorce", "quince", "veinte", "veint", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"}
centenas = {"cien", "quinien"}
millares = {"mil", "millón", "millon", "billón", "billon", "trillón", "trillon", "cuatrillón", "cuatrillon", "quintillón", "quintillón", "sextillón", "sextillon", "septillón", "septillon"}

def suma(num1:int, num2:int, millar: str) -> int:
    respuesta = num1 + num2
    if millar == "mil":
        return respuesta * 10**3
    if millar == "millon":
        return respuesta * 10**6
    if millar == "billon":
        return respuesta * 10**12
    if millar == "trillon":
        return respuesta * 10**18
    if millar == "cuatrillon":
        return respuesta * 10**24
    if millar == "quintillon":
        return respuesta * 10**30
    if millar == "sextillon":
        return respuesta * 10**36
    if millar == "septillon":
        return respuesta * 10**42


def string_to_int(string:str) -> int:
    # comprobar sumas como treintaicinco


    
    # comprobar unidades

    # comprobar decenas

    # comprobar centenas

    # comprobar millares

    pass


def find_number_name(string:str = "Dos") -> int:
    string = string.lower()
    numeros = string.split(" ")
    for numero in numeros:
        num = string_to_int(numero)
    
