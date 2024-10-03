import tkinter as tk

def peliculas():
    entrada = entry_peliculas.get()
    
    lista.insert(tk.END, str(entrada))
    entry_peliculas.delete(0, tk.END)
    
ventana = tk.Tk()
ventana.title("Peliculas")

tk.Label(ventana, text="Ingrese el nombre de la pelicula: ").grid(row=0, column=0)
entry_peliculas = tk.Entry(ventana)
entry_peliculas.grid(row=0, column=1)

boton_calcular = tk.Button(ventana, text="Agregar", command=peliculas)
boton_calcular.grid(row=1, column=0)

tk.Label(ventana, text="Lista de peliculas").grid(row=2, column=0)
lista = tk.Listbox(ventana)
lista.grid(row=2, column=1)

ventana.mainloop()
