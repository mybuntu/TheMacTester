# # The GUIless Mac Tester   
# ## by Jules David
import tkinter as tk
from tkinter import simpledialog
import os

# LISTE DES QUESTIONS
def user_test(output_file):
    issues_detected = {}

    questions = [
        "Connecteur de charge ?",
        "Ports (USB, Thunderbolt, SD-Card slot, HDMI port) ?",
        "Slot RAM ?",
        "Ventilateurs ?",
        "Wifi/Airport ?",
        "Bluetooth ?",
        "Clavier ?",
        "Bouton Power ?",
        "Empreinte Touch ID ?",
        "Indicateur de charge ?",
        "Trackpad ?",
        "Charnière ?",
        "Témoin de mise en veille ?",
        "Touchbar ?",
        "Rétroéclairage Clavier ?",
        "Capteur de luminosité ?"
    ]

    os.system('cls' if os.name == 'nt' else 'clear')

    for question in questions:
        answer = simpledialog.askstring("Test Utilisateur", f"{question}\n([F]onctionnel)/[D]éfectueux/[N]e possède pas): (Enter => [F]onctionnel)")
        if answer and answer.lower() == "d":
            issues_detected[question] = "Défectueux"
        elif answer and answer.lower() == "n":
            issues_detected[question] = "Ne possède pas"
        else:
            issues_detected[question] = "Fonctionnel"

    os.system('cls' if os.name == 'nt' else 'clear')

    # Stocker les résultats dans resultats.txt
    with open(output_file, "a", encoding='utf-8') as file:
        file.write("=== RÉSULTATS DES TESTS UTILISATEUR ===\n")
        for question, status in issues_detected.items():
            file.write(f"{question.split(' au niveau du ')[-1]}: {status}\n")
        file.write("\n")

    # Demander l'état global de l'ordinateur
    etat_options = {
        "1": "Neuf",
        "2": "Très bon état",
        "3": "Bon état",
        "4": "Correct",
        "5": "Usé"
    }

    etat_global = simpledialog.askstring("État Global", "ÉTAT GLOBAL DE L'ORDINATEUR:\n1/ Neuf\n2/ Très bon état\n3/ Bon état\n4/ Correct\n5/ Usé\nSélectionnez une option (1-5): ")
    etat_result = etat_options.get(etat_global, "Non spécifié")

    # Ajouter l'état global à la fin du fichier resultats.txt
    with open(output_file, "a", encoding='utf-8') as file:
        file.write("=== ÉTAT GLOBAL DE L'ORDINATEUR ===\n")
        file.write(f"État: {etat_result}\n\n")

    print("État global de l'ordinateur ajouté dans resultats.txt")
