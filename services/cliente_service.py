from models.clientes import Cliente

def crear_cliente(nombre, edad, saldo):
    
    
    #Validación 1:nombre
    if nombre == "":
        raise ValueError("El nombre es obligatorio")
    
    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre debe contener solo letras")

    #Validación 2:edad
    if edad < 18:
        raise ValueError("El cliente debe ser mayor de edad")
    
    #Validación 3:saldo
    if saldo < 0:
        raise ValueError("El saldo no puede ser negativo")
        
    cliente = Cliente(nombre, edad, saldo)

    if saldo == 0: 
        mensaje = "Cliente sin saldo"
    else:
        mensaje = "cliente con saldo"

    return cliente, mensaje