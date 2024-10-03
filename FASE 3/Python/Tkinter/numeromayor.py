#Pedir 3 numeros, y decir que numero es mayor con Tkinter
import tkinter as tk

def numeromayor():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get()) 
    num3 = float(entry_num3.get())    
    mayor = max(num1,num2,num3)
    
    resultado.insert(tk.END, str(mayor))
        
        
ventana = tk.Tk()
ventana.geometry("500x300")
ventana.resizable(False, False)
ventana.title("Numero mayor")

# Definir las filas y columnas para centrar el contenido
#ventana.grid_rowconfigure(0, weight=1)  # Espacio superior vacío
#ventana.grid_rowconfigure(3, weight=1)  # Espacio inferior vacío
ventana.grid_columnconfigure(0, weight=1)  # Espacio izquierdo vacío
ventana.grid_columnconfigure(3, weight=1)  # Espacio derecho vacío

titulo = tk.Label(ventana, text="*** NUMERO MAYOR ***", font=("Helvetica", 16, "bold")) 
titulo.grid(row=1, column=1, columnspan=2, padx=10, pady=10)


tk.Label(ventana, text="Ingrese el primer numero: ", font=("Helvatica", 12, "bold")).grid(row=2, column=1, padx=10, pady=10)
entry_num1 = tk.Entry(ventana).grid(row=2, column=2, padx=10, pady=10)



tk.Label(ventana, text="Ingrese el segundo número:", font=("Helvatica", 12, "bold")).grid(row=3, column=1, padx=10, pady=10)
entry_num2 = tk.Entry(ventana).grid(row=3, column=2, padx=10, pady=10)


tk.Label(ventana, text="Ingrese el tercer número:", font=("Helvatica", 12, "bold")).grid(row=4, column=1, padx=10, pady=10)
entry_num3 = tk.Entry(ventana).grid(row=4, column=2, padx=10, pady=10)



boton_calcular = tk.Button(ventana, text="Evaluar", command=numeromayor).grid(row=5, column=0, columnspan=2, padx=10, pady=10)


tk.Label(ventana, text="El resultado es", font=("Helvatica", 12, "bold")).grid(row=6, column=1, padx=10, pady=10)
resultado = tk.Text(ventana, height=1, width=10).grid(row=6, column=2, padx=10, pady=10)



ventana.mainloop()


