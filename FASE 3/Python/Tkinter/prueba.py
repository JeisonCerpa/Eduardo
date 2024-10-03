import tkinter as tk

def close_window():
    root.destroy()  # Cierra la ventana

def minimize_window():
    root.iconify()  # Minimiza la ventana

def draw_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        ratio = i / height
        r = int((1 - ratio) * int(color1[1:3], 16) + ratio * int(color2[1:3], 16))
        g = int((1 - ratio) * int(color1[3:5], 16) + ratio * int(color2[3:5], 16))
        b = int((1 - ratio) * int(color1[5:7], 16) + ratio * int(color2[5:7], 16))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

root = tk.Tk()
root.geometry("500x300")

# Eliminar la barra de título
root.overrideredirect(True)

# Crear un canvas para la barra de título personalizada
title_bar = tk.Canvas(root, height=30, bg='white', highlightthickness=0)
title_bar.pack(fill=tk.X)

# Dibujar un gradiente en el canvas
draw_gradient(title_bar, 500, 30, '#000000', '#434343')  # Gradiente de negro a gris

# Botón de minimizar
minimize_button = tk.Button(title_bar, text="_", command=minimize_window, bg='white', fg="black", borderwidth=0)
minimize_button.place(relx=1.0, rely=0.5, anchor='e')  # Colocar a la derecha

# Botón de cerrar
close_button = tk.Button(title_bar, text="X", command=close_window, bg='white', fg="black", borderwidth=0)
close_button.place(relx=0.95, rely=0.5, anchor='e')  # Colocar a la derecha del botón minimizar

# Crear el contenido principal
content_frame = tk.Frame(root)
content_frame.pack(pady=20)

# Ejemplo de entrada
entrada = tk.Entry(content_frame)
entrada.pack()

root.mainloop()
