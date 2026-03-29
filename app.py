import streamlit as st

#..............................................
# CLASS (POO)
#..............................................

class Cliente:
    def __init__(self, nombre, edad, saldo):
        self.__nombre = nombre
        self.__edad = edad
        self.__saldo = saldo

    # Getters (encapsulamiento)
    def get_nombre(self):
        return self,__nombre

    def get_edad(self):
        return self,__edad
    
    def get_saldo(self):
        return self,__saldo

    
    # Metodos
    def mostrar_info(self):
        return f"cliente: {self.__nombre}, edad: {self.__edad}, saldo: {self.__saldo}"

#..............................................
# STREAMLIT
#..............................................
st.title("Demo POO - Ciencia De Datos")
st.write("ingrese los datos del cliente")

nombre = st.text_input("nombre")
edad = st.number_input("edad", min_value=0)
saldo = st.number_input("saldo", min_value=0.0)

if st.button("crear cliente"):

    #Secuencia
    cliente = Cliente(nombre, edad, saldo)

    st.success("cliente creado exitosamente")

    st.write("### Información del cliente: ")
    st.write(cliente. mostrar_info())
