import tkinter as tk

def numeromayor():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    num3 = int(entry_num3.get())
    mayor = max(num1, num2, num3)
    resultado_text.delete("1.0", tk.END)  # Limpiar el contenido anterior
    resultado_text.insert(tk.END, str(mayor))  # Insertar el nuevo resultado

ventana = tk.Tk()

tk.Label(ventana, text="Ingrese el primer número:").grid(row=0, column=0)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1)

tk.Label(ventana, text="Ingrese el segundo número:").grid(row=1, column=0)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1)

tk.Label(ventana, text="Ingrese el tercer número:").grid(row=2, column=0)
entry_num3 = tk.Entry(ventana)
entry_num3.grid(row=2, column=1)

boton_calcular = tk.Button(ventana, text="Calcular Mayor", command=numeromayor)
boton_calcular.grid(row=3, column=0)

tk.Label(ventana, text="El resultado es").grid(row=4, column=0)
resultado_text = tk.Text(ventana, height=1, width=10)
resultado_text.grid(row=4, column=1)

ventana.mainloop()