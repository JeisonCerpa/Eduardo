import tkinter as tk

root = tk.Tk()
root.geometry("500x300")  # Tamaño de la ventana

# Configurar las filas y columnas para que crezcan proporcionalmente
root.grid_rowconfigure(0, weight=1)  # Espacio superior
root.grid_rowconfigure(3, weight=1)  # Espacio inferior
root.grid_columnconfigure(0, weight=1)  # Espacio izquierda
root.grid_columnconfigure(3, weight=1)  # Espacio derecha

# Label centrado
label = tk.Label(root, text="Hola, mundo!")
label.grid(row=1, column=1, columnspan=2, pady=10)  # Centrado con columnspan

# Label "Primer número:" y Entry en la misma fila
label_numero = tk.Label(root, text="Primer número:")
label_numero.grid(row=2, column=1, padx=10, pady=10, sticky="e")  # Alineado a la derecha

entry_numero = tk.Entry(root)
entry_numero.grid(row=2, column=2, padx=10, pady=10, sticky="w")  # Alineado a la izquierda

root.mainloop()
