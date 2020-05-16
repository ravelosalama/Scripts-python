# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:58:05 2020

@author: Ravelo
"""

import tkinter as tk
import pyodbc as bd



#for driver in bd.drivers():
#    print(driver)




conn = bd.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server={CONSULTORIA\SQLDEV2017};"
        "Database={LIBERTYcarsANUALDB};"
        "uid='ADMIN;" " pwd=SOPORTE;")
        
#        "Trusted_Connection=yes;")

'''
estable=bd.Connection()
print (estable)
'''


def read(conn):
  print("lectura")
  cursor=conn.cursor()
  cursor.execute("select * from ssusua")
  for linea in cursor:
      print(f'linea={linea}')

  print()

if cursor == True:
    print("Conexion establecida correctamente")
else:
    print("Parametros errados, conexion falla!")


  
  
   
#read(conn)

#cursor.close()
conn.close()
print ("conexion cerrada")





#ventana=tk.Tk()
#ventana.title("Saint Concesionarios")
#ventana.geometry('640x480')
#etiqueta=tk.Label(ventana,text="menu principal",bg="blue", fg="black")
#etiqueta.pack()
#ventana.mainloop()

