import cv2 as cv

imagen_inicial = cv.imread("./img/Messi.jpeg", cv.IMREAD_COLOR)

# ventana de la imagen original
if imagen_inicial is None:
    print("Error al cargar la imagen")
else:
    roi = imagen_inicial[50:100, 50:100]
    roi[:] = (0, 0, 255)

    roi_copia = roi.copy()
    roi_copia[:] = (255, 0, 0)

    copia = True

    while True:
        cv.imshow("Imagen Original", imagen_inicial)

        if copia:
            cv.imshow("ROI", roi_copia)
        else:
            cv.imshow("ROI", roi)

        key = cv.waitKey(16) & 0xFF

        if key == ord("c"):
            copia = not copia

        if key == ord("q"):
            break

cv.destroyAllWindows()

