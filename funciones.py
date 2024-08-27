
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






