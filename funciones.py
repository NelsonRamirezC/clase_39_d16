
'''
def saludar(): #no recibe params
    print("Hola mundo") # no retorna
'''

'''
def saludar(saludo):
    print(saludo)
    

saludar(input("Ingresa el saludo: "))
saludar(input("Ingresa el saludo: "))
saludar(input("Ingresa el saludo: "))
'''

def saludar(saludo):
    return f"¡{saludo}!"

saludo = saludar("hola mundo!")
print(saludo)


# una función puede recibir n cantidad de params / args

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)

print(resultado)

################
def sumar(*valores):
    resultado = 0
    for valor in valores:
        resultado += valor
        
    return resultado


resultado = sumar(3, 5, 6, 8, 10)
print(resultado)


def operaciones(op, *valores):
    resultado = 0
    if op == "sumar":
        for valor in valores:
            resultado += valor
    elif op == "restar":
        for valor in valores:
            resultado -= valor
    else: 
        return None
    
    return resultado

resultado = operaciones("restar", 4,5,6,7,7)
print(resultado)


# funciones anotaciones

def sumar(a, b):
    print(a)
    print(b)
    return a+b

resultado = sumar(b=5, a=3)

print(resultado)


# indicar tipo de dato que recibe la función 
def sumar(a: int = 0, b: int = 0) -> int:
    return a + b
    

resultado = sumar(5, 4)

print(resultado)


###

numeros = [1,2,3,4,5,6]

def sumar(valores):
    print(valores)

sumar(numeros)


## spread en python

numeros = (1,2,3,4,5,6)

def sumar(*valores):
    print(valores)

sumar(*numeros, 5, 6, 7, 8, 8, 9)


    
    




