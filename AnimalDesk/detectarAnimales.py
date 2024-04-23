# Importar la biblioteca necesaria
import cv2

# Inicializar la captura de video desde la cámara web
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Inicializar los clasificadores de cascada para detectar perros, gatos, caballos y pájaros
perro_cascade = cv2.CascadeClassifier('cascadePerro.xml')
gato_cascade = cv2.CascadeClassifier('cascadeGato.xml')
caballo_cascade = cv2.CascadeClassifier('cascadeCaballo.xml')
pajaro_cascade = cv2.CascadeClassifier('cascadePajaro.xml')

# Bucle principal para capturar y procesar continuamente el video
while True:
    # Leer un cuadro del video capturado
    ret, frame = cap.read()

    # Convertir el cuadro a escala de grises para facilitar el procesamiento
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detección de perros en el cuadro
    perros = perro_cascade.detectMultiScale(gray, scaleFactor=9.8, minNeighbors=110, minSize=(70, 78))
    for (x, y, w, h) in perros:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Dibujar un rectángulo alrededor del perro detectado
        cv2.putText(frame, 'Perro', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)  # Etiquetar el animal como perro

    # Detección de gatos en el cuadro
    gatos = gato_cascade.detectMultiScale(gray, scaleFactor=9.8, minNeighbors=110, minSize=(70, 78))
    for (x, y, w, h) in gatos:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Dibujar un rectángulo alrededor del gato detectado
        cv2.putText(frame, 'Gato', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)  # Etiquetar el animal como gato

    # Detección de caballos en el cuadro
    caballos = caballo_cascade.detectMultiScale(gray, scaleFactor=9.8, minNeighbors=99, minSize=(70, 78))
    for (x, y, w, h) in caballos:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)  # Dibujar un rectángulo alrededor del caballo detectado
        cv2.putText(frame, 'Caballo', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)  # Etiquetar el animal como caballo

    # Detección de pájaros en el cuadro
    pajaros = pajaro_cascade.detectMultiScale(gray, scaleFactor=9.8, minNeighbors=99, minSize=(70, 78))
    for (x, y, w, h) in pajaros:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Dibujar un rectángulo alrededor del pájaro detectado
        cv2.putText(frame, 'Pájaro', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)  # Etiquetar el animal como pájaro

    # Mostrar el cuadro con los rectángulos y etiquetas de detección
    cv2.imshow('frame', frame)

    # Esperar la pulsación de una tecla (esc para salir)
    if cv2.waitKey(1) == 27:
        break

# Liberar la captura de video y cerrar todas las ventanas abiertas
cap.release()
cv2.destroyAllWindows()
