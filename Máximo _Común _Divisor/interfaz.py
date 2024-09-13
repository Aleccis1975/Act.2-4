import tkinter as tk
from tkinter import messagebox
from mcd import mcd  # Importar la función mcd desde el archivo mcd.py

# Función para calcular el MCD y mostrar el resultado en la interfaz
def calcular_mcd():
    try:
        num1 = int(entry_num1.get())  # Obtener el primer número de la entrada de texto
        num2 = int(entry_num2.get())  # Obtener el segundo número de la entrada de texto
        
        if num1 <= 0 or num2 <= 0:
            messagebox.showerror("Error", "Los números deben ser mayores que cero.")
            return
        
        resultado = mcd(num1, num2)
        label_resultado.config(text=f"El MCD de {num1} y {num2} es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Introduce números válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo del MCD")
ventana.geometry("400x300")

# Etiqueta de instrucción
label_instruccion = tk.Label(ventana, text="Introduce dos números para calcular su MCD:")
label_instruccion.pack(pady=10)

# Entrada de texto para el primer número
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)

# Entrada de texto para el segundo número
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)

# Botón para calcular el MCD
boton_calcular = tk.Button(ventana, text="Calcular MCD", command=calcular_mcd)
boton_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
