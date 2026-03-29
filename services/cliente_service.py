from models.clientes import Cliente

def crear_cliente(nombre, edad, saldo):
    
    
    #Validación 1:nombre
    if nombre == "":
        raise ValueError("El nombre es obligatorio")
    
    #Validación 2:edad
    if edad < 18:
        raise ValueError("El cliente debe ser mayor de edad")
    
    #Validación 3:saldo
    if saldo < 0:
        raise ValueError("El saldo no puede ser negativo")
    
    #Condicion Adicional
    if saldo == 0:
        print("Cliente sin saldo inicial")
    
    return Cliente(nombre, edad, saldo)
 
    