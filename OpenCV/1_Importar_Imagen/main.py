import cv2 as cv

imagen_color = cv.imread('img/Messi.jpeg', cv.IMREAD_COLOR)
imagen_gray = cv.imread('img/Messi.jpeg', cv.IMREAD_GRAYSCALE)

if imagen_color is None or imagen_gray is None:
    print("Error cargando imagen")
else:
    modo_gray = False

    while True:
        if modo_gray:
            cv.imshow("Imagen", imagen_gray)
        else:
            cv.imshow("Imagen", imagen_color)

        tecla = cv.waitKey(16) & 0xFF

        if tecla == ord('g'):
            modo_gray = not modo_gray 

        if tecla == ord('q') or tecla == 27:
            break

cv.destroyAllWindows()
