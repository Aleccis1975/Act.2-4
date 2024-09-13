import tkinter as tk
from tkinter import messagebox
from fibonacci import fibonacci  # Importar la función desde el archivo fibonacci.py

# Función para mostrar la serie Fibonacci en la interfaz
def mostrar_fibonacci():
    try:
        num_terminos = int(entry_terminos.get())  # Obtener número de términos desde la entrada
        if num_terminos < 0:
            messagebox.showerror("Error", "El número de términos debe ser mayor o igual a cero.")
            return
        
        # Generar la serie Fibonacci y mostrarla en la interfaz
        resultado = [str(fibonacci(i)) for i in range(num_terminos)]
        label_resultado.config(text=" ".join(resultado))  # Mostrar la serie en la etiqueta
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Serie de Fibonacci")
ventana.geometry("400x300")

# Etiqueta de instrucción
label_instruccion = tk.Label(ventana, text="Introduce el número de términos para la serie Fibonacci:")
label_instruccion.pack(pady=10)

# Campo de entrada para el número de términos
entry_terminos = tk.Entry(ventana)
entry_terminos.pack(pady=5)

# Botón para calcular la serie
boton_calcular = tk.Button(ventana, text="Mostrar Serie", command=mostrar_fibonacci)
boton_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
