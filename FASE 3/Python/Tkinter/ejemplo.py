import tkinter as tk
from tkinter import messagebox

# Funciones para las operaciones
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        mostrar_resultado(resultado)
    except ValueError:
        mensaje_error()

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        mostrar_resultado(resultado)
    except ValueError:
        mensaje_error()

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        mostrar_resultado(resultado)
    except ValueError:
        mensaje_error()

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            mostrar_resultado(resultado)
    except ValueError:
        mensaje_error()

def mostrar_resultado(resultado):
    messagebox.showinfo("Resultado", f"El resultado es: {resultado}")

def mensaje_error():
    messagebox.showerror("Error", "Por favor, ingresa números válidos.")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora Básica")

# Entradas
tk.Label(ventana, text="Primer número:").grid(row=0, column=0)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1)

tk.Label(ventana, text="Segundo número:").grid(row=1, column=0)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1)

# Botones
tk.Button(ventana, text="Sumar", command=sumar).grid(row=2, column=0)
tk.Button(ventana, text="Restar", command=restar).grid(row=2, column=1)
tk.Button(ventana, text="Multiplicar", command=multiplicar).grid(row=3, column=0)
tk.Button(ventana, text="Dividir", command=dividir).grid(row=3, column=1)

# Ejecutar la ventana
ventana.mainloop()