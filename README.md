# Projet : Détection et Suivi d'Objets par Couleur en Temps Réel avec OpenCV

Ce projet utilise OpenCV et Python pour capturer une vidéo en temps réel depuis une webcam, filtrer les objets en fonction de leur couleur en utilisant l'espace de couleur HSV, et suivre ces objets dans le cadre de la caméra.

---

## Instructions d'Installation

1. **Clonage du Répertoire**

   Clonez ce répertoire GitHub sur votre machine locale en utilisant la commande suivante :

2. **Installation des Dépendances**

Assurez-vous d'avoir Python 3.x installé sur votre système. Installez également les bibliothèques nécessaires en utilisant pip :
pip install opencv-python
pip install numpy


---

## Utilisation du Projet

1. **Exécution du Programme**

Exécutez le script Python `color_object_detection.py` pour démarrer le programme :color_object_detection.py

2. **Interface Utilisateur**

- Une fenêtre nommée "MaFenetre" apparaîtra avec des trackbars pour ajuster les seuils HSV (`Hue min/max`, `Sat min/max`, `Val min/max`).
- Ajustez ces trackbars pour filtrer les objets en fonction de leur couleur dans la vidéo en direct.

3. **Fonctionnalités**

- **Capture Vidéo en Temps Réel** : Utilisation de la webcam de l'ordinateur pour capturer des frames vidéo.
- **Filtrage par Couleur HSV** : Utilisation de trackbars pour ajuster dynamiquement les seuils de couleur HSV.
- **Détection et Suivi d'Objets** : Filtrage des objets en fonction des seuils définis et suivi des objets détectés dans le cadre de la caméra.
- **Affichage des Résultats** : Affichage en temps réel de l'image originale, du masque de couleur et du résultat filtré.

4. **Arrêt du Programme**

- Appuyez sur la touche `q` pour quitter le programme et fermer les fenêtres.

---

## Contributions

Les contributions sous forme de suggestions d'amélioration, de corrections de bugs ou d'extensions de fonctionnalités sont les bienvenues. N'hésitez pas à ouvrir une issue ou une pull request pour discuter et proposer vos changements.

---

En utilisant ce projet, vous pouvez facilement capturer, filtrer et suivre des objets en temps réel en fonction de leur couleur à l'aide d'OpenCV et Python. Profitez-en pour explorer et étendre les fonctionnalités selon vos besoins spécifiques !
