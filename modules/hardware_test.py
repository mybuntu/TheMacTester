# # The GUIless Mac Tester   
# ## by Jules David
import os
import cv2
import sounddevice as sd
import numpy as np
import wavio
import tkinter as tk

RECORD_SECONDS = 2
SAMPLE_RATE = 44100
test_results = {}

# Fonction de réponses au rapport de tests
def ask_confirmation(component):
    os.system('cls' if os.name == 'nt' else 'clear')
    response = input(f"Est-ce que {component} fonctionne ? O/n : ").strip()
    if response == '' or response == 'o':
        return "Fonctionnel"
    elif response == 'n':
        return "Défectueux"
    else:
        print("Réponse invalide, par défaut 'Oui' enregistré.")
        return "Fonctionnel"

# Fonction de test de la camera
def test_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erreur : Impossible d'ouvrir la caméra.")
        test_results["Caméra"] = "Défectueux"
        return

    print("Appuyez sur 'q' pour quitter la vidéo.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erreur : Impossible de lire l'image.")
            break
        cv2.imshow('Test de la caméra', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyWindow('Test de la caméra')
    for _ in range(10):
        cv2.waitKey(1)
    test_results["Caméra"] = ask_confirmation("la caméra")

# Test du microphone
def test_microphone():
    print("Test du microphone...")
    print("Enregistrement de l'audio...")
    audio_data = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float64')
    sd.wait()
    wavio.write("test_microphone.wav", audio_data, SAMPLE_RATE, sampwidth=3)
    print("Enregistrement terminé. Vous pouvez écouter le fichier 'test_microphone.wav'.")
    test_results["Microphone"] = ask_confirmation("le microphone")

# Test des hauts-parleurs
def test_speakers():
    print("Test des haut-parleurs...")

    duration = 2
    fs = 44100
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    frequency = 440

    left_channel = 0.5 * np.sin(2 * np.pi * frequency * t)
    right_channel = 0.5 * np.sin(2 * np.pi * frequency * t)
    stereo_sound = np.vstack((left_channel, right_channel)).T

    print("Lecture du haut-parleur gauche...")
    sd.play(np.array([left_channel, np.zeros_like(left_channel)]).T, samplerate=fs)
    sd.wait()
    print("Haut-parleur gauche testé.")
    test_results["Haut-parleur gauche"] = ask_confirmation("le haut-parleur gauche")

    print("Lecture du haut-parleur droit...")
    sd.play(np.array([np.zeros_like(right_channel), right_channel]).T, samplerate=fs)
    sd.wait()
    print("Haut-parleur droit testé.")
    test_results["Haut-parleur droit"] = ask_confirmation("le haut-parleur droit")

    print("Lecture des deux haut-parleurs ensemble...")
    sd.play(stereo_sound, samplerate=fs)
    sd.wait()
    print("Les deux haut-parleurs ont été testés.")
    test_results["Haut-parleurs (stéréo)"] = ask_confirmation("les deux haut-parleurs ensemble")

# Test de l'écran (dead-pixel)
def test_screen():
    print("Test de l'écran pour les pixels morts. Appuyez sur 'q' pour passer au suivant.")
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255)]  # Bleu, Vert, Rouge, Jaune

    # Obtenir la résolution de l'écran avec Tkinter
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.withdraw()  # Masquer la fenêtre Tkinter

    # Configurer la fenêtre OpenCV en plein écran
    cv2.namedWindow("Test de l'écran", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Test de l'écran", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Créer une image avec la taille complète de l’écran
    screen = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)

    for color in colors:
        screen[:, :] = color
        cv2.imshow("Test de l'écran", screen)
        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cv2.destroyWindow("Test de l'écran")
    for _ in range(10):
        cv2.waitKey(1)
    test_results["Écran"] = ask_confirmation("l'écran")

# Ordre des test
def run_tests():
    print("--- Début des tests matériels ---")
    test_screen()
    test_speakers()
    test_microphone()
    test_camera()
    print("--- Fin des tests matériels ---")

    # Enregistrer les résultats dans resultats.txt
    with open("output/resultats.txt", "a", encoding="utf-8") as file:
        file.write("===RESULTATS TESTS MATERIELS===\n")
        for component, status in test_results.items():
            file.write(f"{component}: {status}\n")
        file.write("\n")

    return test_results
