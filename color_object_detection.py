import cv2
import numpy as np

def callback(a):
    pass

# Initialisation de la capture vidéo depuis la webcam (index 0)
cap = cv2.VideoCapture(0)

# Création de la fenêtre et des trackbars pour ajuster les seuils HSV
cv2.namedWindow('MaFenetre')
cv2.resizeWindow('MaFenetre', 400, 400)
cv2.createTrackbar('Hue min', 'MaFenetre', 0, 179, callback)
cv2.createTrackbar('Hue max', 'MaFenetre', 179, 179, callback)
cv2.createTrackbar('Sat min', 'MaFenetre', 0, 255, callback)
cv2.createTrackbar('Sat max', 'MaFenetre', 255, 255, callback)
cv2.createTrackbar('Val min', 'MaFenetre', 0, 255, callback)
cv2.createTrackbar('Val max', 'MaFenetre', 255, 255, callback)

while True:
    # Capture d'une frame vidéo
    ret, frame = cap.read()
    if not ret:
        break

    # Conversion de la frame en espace de couleur HSV
    imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Lecture des valeurs des trackbars pour les seuils HSV
    Hue_min = cv2.getTrackbarPos('Hue min', 'MaFenetre')
    Hue_max = cv2.getTrackbarPos('Hue max', 'MaFenetre')
    Sat_min = cv2.getTrackbarPos('Sat min', 'MaFenetre')
    Sat_max = cv2.getTrackbarPos('Sat max', 'MaFenetre')
    Val_min = cv2.getTrackbarPos('Val min', 'MaFenetre')
    Val_max = cv2.getTrackbarPos('Val max', 'MaFenetre')

    # Création des seuils inférieurs et supérieurs à partir des valeurs des trackbars
    lower = np.array([Hue_min, Sat_min, Val_min])
    upper = np.array([Hue_max, Sat_max, Val_max])

    # Création du masque pour filtrer les couleurs spécifiques
    mask = cv2.inRange(imageHSV, lower, upper)

    # Application du masque à la frame originale
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Affichage des différentes frames
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Resultat', result)

    # Sortie de la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libération de la capture vidéo et fermeture des fenêtres
cap.release()
cv2.destroyAllWindows()
