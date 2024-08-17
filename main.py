# es necesario ejecutar el siguiente comando antes de ejecutar el programa pip install pyttsx3
# Hola profe , este es mi rama
import tkinter as tk
from tkinter import filedialog, Text
import pyttsx3
import os

# inicializar el motor de pyttsx3
engine = pyttsx3.init()

# configurar idioma de la voz 
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')

# configurar opciones de voz 
engine.setProperty('rate', 120)  # velocidad
engine.setProperty('volume', 1)  # volumen 

# funcion principal de leer el texto
def convertir_a_voz():
    texto = text_area.get("1.0", "end-1c")
    texto = texto.strip()  # elimina espacios en blanco al inicio y al final
    texto = ' '.join(texto.split()) # reemplaza multiples espacios y saltos de linea por un solo espacio
    engine.save_to_file(texto, "ultima_voz_creada.mp3")
    engine.runAndWait()
    os.system("start ultima_voz_creada.mp3")

# funcion para subir y leer txt
def cargar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"),))
    if archivo:
        with open(archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, contenido)

# crear la gui
root = tk.Tk()
root.title("texto a voz")

# campos de texto
text_area = Text(root, height=10, width=50)
text_area.pack(pady=20)

# boton convertir
convertir_boton = tk.Button(root, text="convertir a voz", command=convertir_a_voz)
convertir_boton.pack(pady=10)

# boton subir archivo txt
cargar_boton = tk.Button(root, text="cargar archivo", command=cargar_archivo)
cargar_boton.pack(pady=10)

# inicar el programa y mantener activo
root.mainloop()
