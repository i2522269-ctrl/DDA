from models.clientes import Cliente

def crear_cliente(nombre, edad, saldo):
    if edad < 18:
        raise ValueErro ("El cliente debe ser mayor de edad")

    return Cliente(nombre, edad, saldo)

