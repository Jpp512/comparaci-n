import subprocess
import sys

# Función para instalar bibliotecas
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Instalar bibliotecas necesarias
required_packages = ["pandas", "openpyxl", "xlsxwriter", "tkinter"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)
####
import xlsxwriter
import pandas as pd
import openpyxl
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para seleccionar el primer archivo
def seleccionar_archivo1():
    archivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    entrada_archivo1.set(archivo)

# Función para seleccionar el segundo archivo
def seleccionar_archivo2():
    archivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    entrada_archivo2.set(archivo)

# Función para ejecutar la comparación
def ejecutar_comparacion():
    archivo1 = entrada_archivo1.get()
    archivo2 = entrada_archivo2.get()
    archivo_salida = "diferencias.xlsx"

    if not archivo1 or not archivo2:
        messagebox.showwarning("Advertencia", "Por favor, selecciona ambos archivos")
        return

    resultado = comparar_archivos(archivo1, archivo2, archivo_salida)
    messagebox.showinfo("Resultado", resultado)

# Función comparar_archivos
def comparar_archivos(archivo1, archivo2, archivo_salida):
    try:
        # Leer los archivos Excel en DataFrames
        df1 = pd.read_excel(archivo1)
        df2 = pd.read_excel(archivo2)

        # Realizar un 'outer join' para obtener todas las filas,
        # incluyendo las que solo están en uno de los archivos
        merged_df = df1.merge(df2, how='outer', indicator=True)

        # Filtrar las filas que tienen diferencias o que solo están en un archivo
        diferencias = merged_df[merged_df['_merge'] != 'both']

        # Eliminar la columna auxiliar '_merge'
        diferencias = diferencias.drop(columns='_merge')

        # Verificar si hay diferencias antes de exportar
        if diferencias.empty:
            return "No se encontraron diferencias entre los archivos."
        else:
            # Exportar las diferencias a un nuevo archivo Excel
            diferencias.to_excel(archivo_salida, index=False)
            return f"Comparación completada. Diferencias guardadas en '{archivo_salida}'"

    except FileNotFoundError:
        return f"Error: Uno o ambos archivos no fueron encontrados."
    except Exception as e:  # Atrapar cualquier otro error inesperado
        return f"Error inesperado: {e}"

# Crear la ventana principal de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Comparador de Archivos")

# Variables para almacenar las rutas de los archivos
entrada_archivo1 = tk.StringVar()
entrada_archivo2 = tk.StringVar()

# Crear los componentes de la interfaz gráfica
label1 = tk.Label(ventana, text="Archivo 1:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(ventana, textvariable=entrada_archivo1, width=50)
entry1.grid(row=0, column=1)
boton1 = tk.Button(ventana, text="Seleccionar", command=seleccionar_archivo1)
boton1.grid(row=0, column=2)

label2 = tk.Label(ventana, text="Archivo 2:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(ventana, textvariable=entrada_archivo2, width=50)
entry2.grid(row=1, column=1)
boton2 = tk.Button(ventana, text="Seleccionar", command=seleccionar_archivo2)
boton2.grid(row=1, column=2)

boton_ejecutar = tk.Button(ventana, text="Comparar", command=ejecutar_comparacion)
boton_ejecutar.grid(row=2, column=0, columnspan=3)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
