import tkinter as tk
from main1 import *

def procesesar_entrada():
    numero_a_convertir = entrada1.get()
    base_entrada = entrada2.get()
    base_destino = entrada3.get()

    mensaje_de_salida = ""

    # se verifica que en los cuadros haya input que tenga sentido y se le haces las modificaciones a este
    # para poder utilizarlo en la funcion de conversion
    try:
        base_entrada = int(base_entrada)
    
    except ValueError:
        mensaje_de_salida = ("ERROR: Ingrese un numero entero")
  
    try:
        base_destino = int(base_destino)
    
    except ValueError:
        mensaje_de_salida = ("ERROR: Ingrese un numero entero")


    numero_a_convertir = str(numero_a_convertir).strip().upper()

    # se obtiene la salida llamando a la funcion para convertir a menos de que anteriormente ya se haya tenido error
    if len(mensaje_de_salida) == 0:
        mensaje_de_salida = conversor(numero_a_convertir, base_entrada, base_destino)
    
    # se imprime el resultado en el cuadro de salida
    # se configura este cuadro para que pueda actualizarse, para que empiece vacio, para que no se pueda escribir sobre este
    # y para que se actualice con el numero convertido despues de picar en el boton de procesar
    output.config(state="normal")  
    output.delete(1.0, tk.END)    
    output.insert(tk.END, mensaje_de_salida) 
    output.config(state="disabled")  

# Tamano y titulo de la ventana
menu = tk.Tk()
menu.title("Conversor de Bases")
menu.geometry("500x300")

#configuraciones de columna y renglones para poder poner los cuadros de entrada y salida
menu.grid_rowconfigure(0, weight=1)
menu.grid_rowconfigure(1, weight=1)
menu.grid_rowconfigure(2, weight=1)
menu.grid_rowconfigure(3, weight=1)
menu.grid_rowconfigure(4, weight=1)
menu.grid_columnconfigure(0, weight=1)
menu.grid_columnconfigure(1, weight=1)

# cuadro de input en donde se escribe el numero de entrada
etiqueta1 = tk.Label(menu, text="Numero entrada:")
etiqueta1.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
entrada1 = tk.Entry(menu)
entrada1.grid(row=0, column=1, padx=10, pady=5)

# cuadro de output que es actualizado con numero ya convertido cuando se pica el boton
etiqueta_salida = tk.Label(menu, text="Numero salida:")
etiqueta_salida.grid(row=1, column=2, padx=10, pady=5, sticky="ew")
output = tk.Text(menu, height=2, width=30, wrap=tk.WORD, state="disabled")
output.grid(row=0, column=2, padx=10, pady=5)

# boton para indicarle al programa que procese los datos en los cuadros de input
boton_para_procesar = tk.Button(menu, text="Convertir", command=procesesar_entrada)
boton_para_procesar.grid(row=4, column=1, columnspan=2, pady=10)

# cuadro de input en donde se escribe la base de entrada
etiqueta2 = tk.Label(menu, text="Base Entrada:")
etiqueta2.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
entrada2 = tk.Entry(menu)
entrada2.grid(row=2, column=1, padx=10, pady=5)

# cuadro de input en donde se escribe la base a la que se quiere convertir el numero
etiqueta3 = tk.Label(menu, text="Base Salida:")
etiqueta3.grid(row=3, column=2, padx=10, pady=5, sticky="ew")
entrada3 = tk.Entry(menu)
entrada3.grid(row=2, column=2, padx=10, pady=5)

# se inicia la ventana
menu.mainloop()
