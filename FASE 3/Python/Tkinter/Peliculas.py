import tkinter as tk

def peliculas():
    entrada = entry_peliculas.get()
    
    lista.insert(tk.END, str(entrada))
    entry_peliculas.delete(0, tk.END)
    
ventana = tk.Tk()
ventana.title("Peliculas")
ventana.geometry("450x250")
ventana.resizable(False, False)

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(3, weight=1)


pelicula = tk.Label(ventana, text="Escribe el titulo de la pelicula", font=("Arial", 10))
pelicula.grid(row=0, column=0, padx=10, pady=10)

entry_peliculas = tk.Entry(ventana)
entry_peliculas.grid(row=1, column=0, padx=10, pady=10)

boton_calcular = tk.Button(ventana, text="Añadir", command=peliculas, font=("Arial", 10))
boton_calcular.grid(row=2, column=0, padx=10, pady=10)

lista = tk.Label(ventana, text="Lista de peliculas", font=("Arial", 10))
lista.grid(row=0, column=2, padx=10, pady=10)

lista = tk.Listbox(ventana)
lista.grid(row=1, column=2, rowspan=2, padx=10, pady=10)

ventana.mainloop()
