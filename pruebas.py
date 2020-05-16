# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:58:05 2020

@author: Ravelo
"""

import tkinter as tk
import pyodbc as bd

for driver in bd.drivers():
    print(driver)

while True:
    try:
        conn = bd.connect("Driver={SQL Server Native Client 11.0};"
        "Server={CONSULTORIA\SQLDEV2017};"
        "Database={LIBERTYcarsANUALDB};"
        "uid=ADMIN;" " pwd=SOPORTE;")
        
#        "Trusted_Connection=yes;")
        print("Conexion establacida satisfactoriamente")
        break
    except:
        print("Parametros errados, conexion NO ESTABLECIDA")
        break

try:
    a=int(input("introduzca a:" ))
    b=int(input("introduzca b:" ))
    DIV=a/b
    print(DIV)
        
except: 
    print("no puede dividir entre o")

uno=bd.Error
print("respuesta:", uno)

'''
def read(conn):
    print("lectura")
    cursor=conn.cursor()
    cursor.execute("select * from saoper")
    for linea in cursor:
        print(f'linea={linea}')
    print()


read(conn)

if conn == True: 
    print("Conexion establecida correctamente")
else:
    print("Parametros errados, conexion falla!")
'''

#cursor.close()
abierto=conn.close()
if abierto==True:
    conn.close()
    
print ("conexion cerrada")

#ventana=tk.Tk()
#ventana.title("Saint Concesionarios")
#ventana.geometry('640x480')
#etiqueta=tk.Label(ventana,text="menu principal",bg="blue", fg="black")
#etiqueta.pack()
#ventana.mainloop()

