import cv2 as cv

video = cv.VideoCapture(0)
show_roi = True

while True:
    ret, frame = video.read()

    if not ret:
        print("No se pudo abrir la camara")
        break

    h, w, _ = frame.shape
    video_roi = frame[h//2:h, 0:w]

    if show_roi:
        cv.putText(
            frame,
            "MODO ROI",
            (30, 40),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
        mostrar = frame 
    else:
        cv.putText(
            frame,
            "Modo Normal",
            (30,40),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255, 0),
            2
        )
        mostrar = frame 

    cv.imshow("Camera", frame)
        
    key = cv.waitKey(1) & 0xFF

    if key & 0xFF == ord("c"):
        show_roi = not show_roi
    
    if key & 0xFF == ord("q"):
        break

video.release()
cv.destroyAllWindows()


        