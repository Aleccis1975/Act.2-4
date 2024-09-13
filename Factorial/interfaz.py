import tkinter as tk
from tkinter import messagebox
from factorial import factorial  # Importar la función factorial desde el archivo factorial.py

# Función para calcular el factorial y mostrarlo en la interfaz
def calcular_factorial():
    try:
        numero = int(entry_numero.get())  # Obtener el número de la entrada de texto
        if numero < 0:
            messagebox.showerror("Error", "El número debe ser mayor o igual a cero.")
            return
        
        resultado = factorial(numero)
        label_resultado.config(text=f"El factorial de {numero} es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Factorial")
ventana.geometry("400x300")

# Etiqueta de instrucción
label_instruccion = tk.Label(ventana, text="Introduce un número para calcular su factorial:")
label_instruccion.pack(pady=10)

# Entrada de texto para el número
entry_numero = tk.Entry(ventana)
entry_numero.pack(pady=5)

# Botón para calcular el factorial
boton_calcular = tk.Button(ventana, text="Calcular Factorial", command=calcular_factorial)
boton_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
