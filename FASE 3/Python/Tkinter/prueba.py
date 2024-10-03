import tkinter as tk

def saludar():
    nombre = entrada.get()
    mensaje = f'Hola {nombre}!'
    
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, str(mensaje))
    
def on_entry_click(event):
    if entrada.get() == 'Escribe tu nombre...':
       entrada.delete(0, tk.END)
       entrada.insert(0, '')
       entrada.config(fg = 'red')
       
def on_focusout(event):
    if entrada.get() == '':
        entrada.insert(0, 'Escribe tu nombre...')
        entrada.config(fg = 'red')
    
ventana = tk.Tk()
ventana.geometry("500x250")
ventana.resizable(False, False)
ventana.title("Saludo")

cuadro = tk.LabelFrame(ventana, text="Entrada de Datos", padx=10, pady=10).grid(row=0, column=0, padx=20, pady=20)

entrada = tk.Entry(cuadro, bg="lightgreen", fg="red")
entrada.insert(0, 'Escribe tu nombre...')
entrada.grid(row=0, column=0, padx=10, pady=10)

cuadro2 = tk.LabelFrame(ventana, text="Resultado", padx=10, pady=10).grid(row=0, column=1, padx=20, pady=20)

resultado = tk.Text(cuadro2, height=1, width=20, bg="cyan")
resultado.grid(row=0, column=0)

cuadro3 = tk.LabelFrame(ventana, text="Enviar", padx=10, pady=10).grid(row=1, column=0, padx=20, pady=20)

boton_calcular = tk.Button(cuadro3, text="Enviar", command=saludar, background="cyan", width=20)
boton_calcular.grid(row=0, column=0)

ventana.mainloop()

