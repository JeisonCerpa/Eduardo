import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Alineación")
ventana.geometry("600x720")
ventana.resizable(False, False)
ventana.grid_columnconfigure(0, weight=1)  
ventana.grid_columnconfigure(3, weight=1)


imagen = Image.open("FASE 3/Python/Tkinter/Imagenes/Cancha.jpg")
imagen = imagen.resize((600, 720))
img = ImageTk.PhotoImage(imagen)
label = tk.Label(ventana, image=img)
label.place(x=0, y=0)

valdes = Image.open("FASE 3/Python/Tkinter/Imagenes/VictorValdes.png")
valdes = valdes.resize((75, 100))
img_valdes = ImageTk.PhotoImage(valdes)
label_valdes = tk.Label(ventana, image=img_valdes)
label_valdes.grid(row=0, column=0, columnspan=4, pady=10)

danialves = Image.open("FASE 3/Python/Tkinter/Imagenes/DaniAlves.png")
danialves = danialves.resize((75, 100))
img_danialves = ImageTk.PhotoImage(danialves)
label_danialves = tk.Label(ventana, image=img_danialves)
label_danialves.grid(row=1, column=0, pady=10)

pique = Image.open("FASE 3/Python/Tkinter/Imagenes/Pique.png")
pique = pique.resize((75, 100))
img_pique = ImageTk.PhotoImage(pique)
label_pique = tk.Label(ventana, image=img_pique)
label_pique.grid(row=1, column= 1, pady=10)

puyol = Image.open("FASE 3/Python/Tkinter/Imagenes/Puyol.jpg")
puyol = puyol.resize((75, 100))
img_puyol = ImageTk.PhotoImage(puyol)
label_puyol = tk.Label(ventana, image=img_puyol)
label_puyol.grid(row=1, column=2, pady=10)

abidal = Image.open("FASE 3/Python/Tkinter/Imagenes/Abidal.png")
abidal = abidal.resize((75, 100))
img_abidal = ImageTk.PhotoImage(abidal)
label_abidal = tk.Label(ventana, image=img_abidal)
label_abidal.grid(row=1, column=3, pady=10)

busquets = Image.open("FASE 3/Python/Tkinter/Imagenes/Busquets.png")
busquets = busquets.resize((75, 100))
img_busquets = ImageTk.PhotoImage(busquets)
label_busquets = tk.Label(ventana, image=img_busquets)
label_busquets.grid(row=2, column=1, columnspan=2, pady=10)

xavi = Image.open("FASE 3/Python/Tkinter/Imagenes/Xavi.jpg")
xavi = xavi.resize((75, 100))
img_xavi = ImageTk.PhotoImage(xavi)
label_xavi = tk.Label(ventana, image=img_xavi)
label_xavi.grid(row=3, column=0, columnspan=2, pady=10)

iniesta = Image.open("FASE 3/Python/Tkinter/Imagenes/Iniesta.jpg")
iniesta = iniesta.resize((75, 100))
img_iniesta = ImageTk.PhotoImage(iniesta)
label_iniesta = tk.Label(ventana, image=img_iniesta)
label_iniesta.grid(row=3, column=2, columnspan=2, pady=10)

messi = Image.open("FASE 3/Python/Tkinter/Imagenes/Messi.jpg")
messi = messi.resize((75, 100))
img_messi = ImageTk.PhotoImage(messi)
label_messi = tk.Label(ventana, image=img_messi)
label_messi.grid(row=4, column = 0, pady=10)

pedro = Image.open("FASE 3/Python/Tkinter/Imagenes/Pedro.jpg")
pedro = pedro.resize((75, 100))
img_pedro = ImageTk.PhotoImage(pedro)
label_pedro = tk.Label(ventana, image=img_pedro)
label_pedro.grid(row=4, column = 3, pady=10)

villa = Image.open("FASE 3/Python/Tkinter/Imagenes/Villa.jpg")
villa = villa.resize((75, 100))
img_villa = ImageTk.PhotoImage(villa)
label_villa = tk.Label(ventana, image=img_villa)
label_villa.grid(row=5, column=1, columnspan=2, pady=10)















ventana.mainloop()