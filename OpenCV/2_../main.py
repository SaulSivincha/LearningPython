import cv2 as cv
import numpy as np

imagen_original = cv.imread("./img/Messi.jpeg", cv.IMREAD_COLOR)
imagen_modificada = cv.imread("./img/Messi.jpeg", cv.IMREAD_COLOR)

if imagen_original is None:
    print("Error al cargar la imagen")
else:
    original = False

    print("Inspeccion de propiedades:")
    print(imagen_original.shape)
    print(imagen_original.dtype)

    print("Inspeccion de pixel en especifico:")
    print("Colores en BGR", imagen_original[100,100])

    modificado = False

    # modificando un pixel
    imagen_modificada[1, 1] = (0, 0, 255)
    
    # cambiando a un corazon (implementacion de ia), antes era un cuadrado
    h, w, _ = imagen_modificada.shape
    cx, cy = w // 2, h // 2
    escala = 40  
    y, x = np.ogrid[-cy:h-cy, -cx:w-cx]
    x = x / escala
    y = -y / escala
    mask = (x**2 + y**2 - 1)**3 - x**2 * y**3 <= 0
    imagen_modificada[mask] = (0, 0, 255)


    while True:
        if modificado:
            cv.imshow("Imagen", imagen_modificada)
        else:
            cv.imshow("Imagen", imagen_original)
        
        key = cv.waitKey(16) & 0xFF;

        if key == ord('g'):
            modificado = not modificado

        if key == ord("q"): 
            break

cv.destroyAllWindows()





