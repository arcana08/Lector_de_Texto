import tkinter as tk
from tkinter import filedialog, Text
from gtts import gTTS
import os
#funcion principal de leer el texto
def convertir_a_voz():
    texto = text_area.get("1.0", "end-1c")
    idioma = 'es'
    voz = gTTS(text=texto, lang=idioma, slow=False)
    voz.save("ultima_voz_creada.mp3")
    os.system("start ultima_voz_creada.mp3")
# funcion para subir y leer txt
def cargar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"),))
    if archivo:
        with open(archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, contenido)

# se crea laa gui 
root = tk.Tk()
root.title("Texto a Voz")

# campos d texto
text_area = Text(root, height=10, width=50)
text_area.pack(pady=20)

# btn convertor
convertir_boton = tk.Button(root, text="Convertir a Voz", command=convertir_a_voz)
convertir_boton.pack(pady=10)

# btn subir txt
cargar_boton = tk.Button(root, text="Cargar Archivo", command=cargar_archivo)
cargar_boton.pack(pady=10)

# inicar programa y manter activo
root.mainloop()
