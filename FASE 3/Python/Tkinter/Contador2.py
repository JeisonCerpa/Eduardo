import tkinter as tk

def contar_up():
    try:
        numero = int(entry.get())
        contador = 0
        incrementar_contador(numero, contador)
    except ValueError:
        pass

def incrementar_contador(numero, contador):
    if contador <= numero:
        entry.delete(0, tk.END)
        entry.insert(0, str(contador))
        ventana.after(500, incrementar_contador, numero, contador + 1)

def contar_down():
    try:
        numero = int(entry.get())
        decrementar_contador(numero)
    except ValueError:
        pass

def decrementar_contador(numero):
    if numero >= 0:
        entry.delete(0, tk.END)
        entry.insert(0, str(numero))
        ventana.after(500, decrementar_contador, numero - 1)

def reset():
    entry.delete(0, tk.END)
    entry.insert(0, "0")

ventana = tk.Tk()
ventana.geometry("400x100")

etiqueta = tk.Label(ventana, text="Contador")
etiqueta.grid(row=0, column=0)

entry = tk.Entry(ventana, width=10)
entry.grid(row=0, column=1)
entry.insert(0, "0")

boton_up = tk.Button(ventana, text="Count Up", command=contar_up)
boton_up.grid(row=0, column=2)

boton_down = tk.Button(ventana, text="Count Down", command=contar_down)
boton_down.grid(row=0, column=3)

boton_reset = tk.Button(ventana, text="Reset", command=reset)
boton_reset.grid(row=0, column=4)

ventana.mainloop()
