import streamlit as st
import pandas as pd
from models.clientes import Cliente
from services.cliente_service import crear_cliente

#..............................................
# STREAMLIT
#..............................................
st.title("Demo POO - Ciencia De Datos")
st.write("ingrese los datos del cliente")


# Imputs
nombre = st.text_input("nombre")
edad = st.number_input("edad", min_value=0)
saldo = st.number_input("saldo", min_value=0.0)

# Boton
if st.button("crear cliente"):

    try:
        #crea cliente + mensajes
        cliente, mensaje = crear_cliente(nombre, edad, saldo)

        st.success("cliente creado exitosamente")

        st.info(mensaje)

        st.write("### Información del cliente: ")
        st.write(cliente.mostrar_info())

        data = {
            "nombre": cliente.get_nombre(),
            "edad": cliente.get_edad(),
            "saldo": cliente.get_saldo()
        }

        df = pd.DataFrame(data)

        st.write("### Tabla de clientes:")
        st.dataframe(df)

    except Exception as e:
        st.error(str(e))
