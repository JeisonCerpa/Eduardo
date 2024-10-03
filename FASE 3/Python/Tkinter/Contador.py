import tkinter as tk

def countup():
    global count
    count += 1
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, str(count))

def countdown():
    global count
    count -= 1
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, str(count))
    
def reset():
    global count
    count = 0
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, str(count))
    
ventana = tk.Tk()
ventana.title("Contador")

count = 0

tk.Label(ventana, text="Contador").grid(row=0, column=0)
resultado = tk.Text(ventana, height=1, width=10)
resultado.grid(row=0, column=1, padx=5, pady=30)

boton_countup = tk.Button(ventana, text="CountUp", command=countup)
boton_countup.grid(row=0, column=2, padx=5)

boton_countdown = tk.Button(ventana, text="CountDown", command=countdown)
boton_countdown.grid(row=0, column=3, padx=5)

boton_reset = tk.Button(ventana, text="Reset", command=reset)
boton_reset.grid(row=0, column=4, padx=5)

ventana.mainloop()