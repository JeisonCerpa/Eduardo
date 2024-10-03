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

titulo = tk.Label(ventana, text="*** NUMERO MAYOR ***", font=("Helvetica", 16, "bold")) 
titulo.grid(row=0, column=0, columnspan=2, pady=10)


tk.Label(ventana, text="Ingrese el primer numero: ").grid(row=1, column=0, padx=100)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=1, column=1, pady=25)  



tk.Label(ventana, text="Ingrese el segundo número:")
entry_num2 = tk.Entry(ventana)


tk.Label(ventana, text="Ingrese el tercer número:")
entry_num3 = tk.Entry(ventana)



boton_calcular = tk.Button(ventana, text="Calcular Mayor", command=numeromayor)


tk.Label(ventana, text="El resultado es")
resultado = tk.Text(ventana, height=1, width=10)



ventana.mainloop()


