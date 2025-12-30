import cv2 as cv

video = cv.VideoCapture(0)
tecla_activa = -1

while True:
    ret, frame = video.read()

    if not ret:
        print("Error en algun punto del video")
        break

        
    key = cv.waitKey(1) & 0xFF

    if key & 0xFF == ord("q"):
        break

    # Teclas
    teclas = {
        "DO": 0,
        "RE": 1,
        "MI": 2,
        "FA": 3,
        "SOL": 4,
        "LA": 5,
        "SI": 6
    }

    if key & 0xFF == ord("a"):
        tecla_activa = 0
    elif key & 0xFF == ord("s"):
        tecla_activa = 1
    elif key & 0xFF == ord("d"):
        tecla_activa = 2
    elif key & 0xFF == ord("f"):
        tecla_activa = 3
    elif key & 0xFF == ord("g"):
        tecla_activa = 4
    elif key & 0xFF == ord("h"):
        tecla_activa = 5
    elif key & 0xFF == ord("j"):
        tecla_activa = 6     


    # obtener altura y ancho de lo capturado
    h, w, _ = frame.shape

    # calcular altura del teclado y donde dibujarlo
    alto_teclado = int(h / 3)
    y_teclado = h - alto_teclado

    # ancho de cada tecla
    ancho_tecla = int(w / 7)

    # para el x de cada tecla se debe recorrer un bucle del 0 al 6
    # dibujar cada tecla
    for i in range(7):
        if i == tecla_activa:
            color = (0, 255, 0)
        else:
            color = (255, 255, 255)
        cv.rectangle(
            frame,
            (i * ancho_tecla, y_teclado),
            (i * ancho_tecla + ancho_tecla, y_teclado + alto_teclado),
            color,
            1,
        )
    
    # colocar texto para cada tecla
    notas = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
    for i in range(7):
        cv.putText(
            frame,
            notas[i],
            (i * ancho_tecla + 10, y_teclado + 40),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 0),
            2
        )

    cv.imshow("Camera", frame)
    
    # implementar tecla a tocar para cambiar el color
    
video.release()
cv.destroyAllWindows()