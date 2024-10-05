import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación con Pestañas")

# Crear un Notebook (contenedor de pestañas)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Crear los frames para cada pestaña
tab1 = ttk.Frame(notebook, width=400, height=300)
tab2 = ttk.Frame(notebook, width=400, height=300)
tab3 = ttk.Frame(notebook, width=400, height=300)

# Empaquetar los frames (aunque no es necesario con Notebook)
tab1.pack(fill='both', expand=True)
tab2.pack(fill='both', expand=True)
tab3.pack(fill='both', expand=True)

# Agregar las pestañas al Notebook
notebook.add(tab1, text='Pestaña 1')
notebook.add(tab2, text='Pestaña 2')
notebook.add(tab3, text='Pestaña 3')

# Añadir contenido a las pestañas
label1 = tk.Label(tab1, text="Contenido de la Pestaña 1", font=('Arial', 18))
label1.pack(pady=20)

label2 = tk.Label(tab2, text="Contenido de la Pestaña 2", font=('Arial', 18))
label2.pack(pady=20)

label3 = tk.Label(tab3, text="Contenido de la Pestaña 3", font=('Arial', 18))
label3.pack(pady=20)

# Ejecutar el loop principal
root.mainloop()
