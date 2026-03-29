import streamlit as st
from models.clientes import Cliente
from services.cliente.ervice import crear_cliente

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
        cliente = crear_cliente(nombre, edad, saldo)

        st.success("cliente creado exitosamente")

        st.write("### Información del cliente: ")
        st.write(cliente. mostrar_info())

    except Exception as e:
        st.error(str(e))
