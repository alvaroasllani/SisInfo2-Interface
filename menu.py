import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Olympus Gym")
ventana.geometry("1000x600")


# Función para cerrar sesión
def cerrar_sesion():
    # Aquí puedes añadir el código para cerrar sesión
    ventana.destroy()


# Cargar la imagen de fondo
imagen_fondo = Image.open("gym2.jpg")
imagen_fondo = imagen_fondo.resize((1000, 600), Image.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget Label para la imagen de fondo
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Configurar para que la imagen de fondo esté detrás de todos los demás widgets
fondo_label.lower()

# Crear el título
titulo = tk.Label(ventana, text="Olympus Gym", font=("Arial", 30))
titulo.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

# Crear el botón de cerrar sesión
boton_cerrar_sesion = tk.Button(
    ventana,
    text="Cerrar Sesión",
    bg="#EB984E",
    font=("Arial", 12, "bold"),
    command=cerrar_sesion,
)
boton_cerrar_sesion.grid(row=1, column=0, padx=10, pady=10, sticky="sw")

# Crear el panel de botones
panel_botones = tk.Frame(ventana)
panel_botones.grid(row=1, column=1, padx=10, pady=10, sticky="nse")

# Lista de nombres de botones
nombres_botones = [
    "Horarios",
    "Planes",
    "Clientes",
    "Equipamiento",
    "Salones",
    "Actividades",
    "Instructores",
]

# Crear los botones en el panel
for i, nombre in enumerate(nombres_botones):
    boton = tk.Button(
        panel_botones, text=nombre, bg="#EB984E", font=("Arial", 14, "bold"), width=15
    )
    boton.grid(row=i, column=0, padx=5, pady=5, sticky="e")

# Configurar la geometría de la ventana para ajustarse al contenido y centrarla en la pantalla
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.update_idletasks()  # Actualizar la ventana antes de obtener su tamaño
ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Ejecutar la ventana
ventana.mainloop()
