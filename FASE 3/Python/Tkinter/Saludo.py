import tkinter as tk

def saludar():
    nombre = entrada.get()
    mensaje = f'Hola {nombre}!'
    
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, str(mensaje))
    
ventana = tk.Tk()
tk.Label(ventana, text="Entrada de datos").grid(row=1, column=0)
entrada = tk.Entry(ventana)
entrada.grid(row=1, column=1)

tk.Label(ventana, text="Resultado").grid(row=1, column=5, padx=5, pady=10)
resultado = tk.Text(ventana, height=1, width=15)
resultado.grid(row=1, column=6, pady=10)

tk.Label(ventana, text="Enviar").grid(row=2, column=0)
boton_calcular = tk.Button(ventana, text="Enviar", command=saludar)
boton_calcular.grid(row=2, column=1)

ventana.mainloop()

    
    
    
    