import streamlit as st
from models.clientes import Cliente
from services.cliente_service import crear_cliente

#..............................................
# STREAMLIT
#..............................................
st.title("Demo POO - Ciencia De Datos")
st.write("ingrese los datos del cliente")

nombre = st.text_input("nombre")
edad = st.number_input("edad", min_value=0)
saldo = st.number_input("saldo", min_value=0.0)

if st.button("crear cliente"):

    try:
        #Secuencia
        cliente, mensaje = crear_cliente(nombre, edad, saldo)

        st.success("cliente creado exitosamente")

        st.info(mensaje)

        st.write("### Información del cliente: ")
        st.write(cliente.mostrar_info())

        if hasattr(cliente, "clasificar_cliente"):
            st.write("### Clasificación: ")
            st.write(cliente.clasificar_cliente())
    
        if hasattr(cliente, "es_mayor_edad"):
            if cliente.es_mayor_edad():
                st.success("El cliente es mayor de edad")
            else:
                st.warning("El cliente es menor de edad")


    except Exception as e:
        st.error(str(e))
