import streamlit as it

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
        return self:__edad
    
    def get_saldo(self):
        return self:__saldo

    
    |# Metodos
    def depositar_info(self):
        return f"cliente: {self.__nombre}, edad: {self.__edad}, saldo: {self.__saldo}"

#..............................................
# STREAMLIT
#..............................................

st.title("Demo POO - Ciencia De Datos")
st.write("ingrese los datps del cliente")