# Importar las bibliotecas necesarias
import cv2  # OpenCV para procesamiento de imágenes
import tkinter as tk  # Tkinter para la interfaz gráfica
from PIL import Image, ImageTk  # PIL para manejar imágenes en Tkinter

# Inicializar el clasificador de cascada para cada animal
perro_cascade = cv2.CascadeClassifier('cascadePerro.xml')  # Clasificador de cascada para detectar perros
gato_cascade = cv2.CascadeClassifier('cascadeGato.xml')  # Clasificador de cascada para detectar gatos
caballo_cascade = cv2.CascadeClassifier('cascadeCaballo.xml')  # Clasificador de cascada para detectar caballos
pajaro_cascade = cv2.CascadeClassifier('cascadePajaro.xml')  # Clasificador de cascada para detectar pájaros


# Variable para controlar la detección de animales
detection_active = False

# Función para iniciar la detección de animales
def start_detection():
    global detection_active
    detection_active = True
    detect_animals()

# Función para detener la detección de animales
def stop_detection():
    global detection_active
    detection_active = False
    cap.release()  # Liberar el dispositivo de captura de video
    cv2.destroyAllWindows()  # Cerrar todas las ventanas abiertas de OpenCV

# Función para detectar animales
def detect_animals():
    if detection_active:
        ret, frame = cap.read()  # Leer un cuadro del dispositivo de captura de video
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertir la imagen a escala de grises para facilitar el procesamiento

            # Detección de perros
            perros = perro_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=3, minSize=(40, 40))
            for (x, y, w, h) in perros:
                animal_label.config(text="Perro\nDescripción:\n*Come, cuida y es el mejor amigo del hombre\n*Tiene 4 patras\n*Se destaca por su amor hacia el humano")  # Actualizar la etiqueta con la descripción del perro

            # Detección de gatos
            gatos = gato_cascade.detectMultiScale(gray, scaleFactor=10, minNeighbors=15, minSize=(40, 40))
            for (x, y, w, h) in gatos:
                animal_label.config(text="Gato\nDescripción:\n*Come croquetas y es doméstico\nTiene 4 patas\n*Tiene bigotes\n*Es muy independiente")  # Actualizar la etiqueta con la descripción del gato

            # Detección de caballos
            caballos = caballo_cascade.detectMultiScale(gray, scaleFactor=10, minNeighbors=15, minSize=(40, 40))
            for (x, y, w, h) in caballos:
                animal_label.config(text="Caballo\nDescripción:\n*Come pasto y es del campo\n*Tiene 4 patas\n*Es común para cabalgatas")  # Actualizar la etiqueta con la descripción del caballo

            # Detección de pájaros
            pajaros = pajaro_cascade.detectMultiScale(gray, scaleFactor=10, minNeighbors=15, minSize=(40, 40))
            for (x, y, w, h) in pajaros:
                animal_label.config(text="Pajaro\nDescripción:\n*Come granos y vuela por todo el mundo\n*Tiene 2 patas\n*Canta")  # Actualizar la etiqueta con la descripción del pájaro

            # Actualizar la ventana de captura de vídeo
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir la imagen de OpenCV a formato RGB
            img = Image.fromarray(img)  # Crear una imagen PIL desde la matriz de imagen
            img = ImageTk.PhotoImage(image=img)  # Crear una imagen Tkinter desde la imagen PIL
            video_label.imgtk = img  # Mantener una referencia para evitar que la imagen sea recolectada por el recolector de basura
            video_label.configure(image=img)  # Actualizar la etiqueta de video con la nueva imagen

    # Llamar a esta función de nuevo después de 10 ms si la detección está activa
    if detection_active:
        root.after(10, detect_animals)

# Configuración de la interfaz gráfica
root = tk.Tk()  # Crear una ventana de Tkinter
root.title("Detección de animales")  # Establecer el título de la ventana

# Etiqueta para mostrar el video
video_label = tk.Label(root)  # Crear una etiqueta para mostrar el video
video_label.pack()  # Empaquetar la etiqueta en la ventana

# Botón para iniciar la detección
start_button = tk.Button(root, text="Iniciar", command=start_detection, bg="green", fg="white", padx=10, pady=5)  # Crear un botón para iniciar la detección
start_button.pack(side=tk.LEFT, padx=10)  # Empaquetar el botón en la ventana

# Botón para detener la detección y cerrar el programa
stop_button = tk.Button(root, text="Detener y Salir", command=root.quit, bg="red", fg="white", padx=10, pady=5)  # Crear un botón para detener la detección y salir del programa
stop_button.pack(side=tk.LEFT, padx=10)  # Empaquetar el botón en la ventana

# Etiqueta para mostrar el animal detectado y su descripción
animal_label = tk.Label(root, text="", font=("Arial", 12))  # Crear una etiqueta para mostrar el animal detectado y su descripción
animal_label.pack(side=tk.BOTTOM, pady=10)  # Empaquetar la etiqueta en la parte inferior de la ventana

# Iniciar captura de vídeo
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Abrir el dispositivo de captura de video (cámara web)

root.mainloop()  # Iniciar el bucle principal de la aplicación Tkinter
