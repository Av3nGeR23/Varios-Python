import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from rembg import remove
import os

def remove_background():
    filepath = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    
    if filepath:
        try:
            image_input = Image.open(filepath)
            output = remove(image_input)
            downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
            output_path = os.path.join(downloads_folder, "output.png")
            output.save(output_path)
            print(f"El fondo ha sido removido con éxito. La imagen se ha guardado en: {output_path}")
            messagebox.showinfo("Imagen Lista", "La imagen ha sido procesada y guardada en la carpeta de descargas.")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Remover Fondo de Imagen")
root.geometry("400x200")
root.configure(bg="#2c3e50")

# Título
title = tk.Label(root, text="Remover Fondo de Imagen", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16, "bold"))
title.pack(pady=20)

# Botón para remover el fondo
btn_remove_bg = tk.Button(root, text="Selecciona Imagen", command=remove_background,
                          bg="#3498db", fg="#ecf0f1", font=("Helvetica", 12, "bold"), relief="raised", bd=3)
btn_remove_bg.pack(pady=20)

# Iniciar la interfaz gráfica
root.mainloop()
