# The GUIless Mac Tester   
## by Jules David
## ATTENTION TEST ECRAN NE MARCHE POUR L'INSTANT QU'EN GRAPHIQUE...
import os
import sys
import tkinter as tk
from tkinter import messagebox
from modules import info, specs, battery_test, hardware_test, user_test, report

# Ajouter les modules au chemin d'importation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

from modules import info, specs, hardware_test, report, battery_test, user_test

os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\nBienvenue dans le programme de test des Mac.")
    print("Sélectionnez une option :")
    print("1. Prendre les informations système - info.py")
    print("2. Collecter les spécifications système (processeur, RAM, GPU, disque) - specs.py")
    print("3. Consulter l'état de la batterie - battery_test.py")
    print("4. Tester les composants matériel (cam, micro, hauts-parleurs) - hardware_test.py")
    print("5. Consulter ou rapporter d'autres pannes - user_test.py")
    print("6. Générer le rapport PDF - report.py")
    # print("6. Imprimer le rapport PDF - report.py")
    # print("7. Uploader le rapport PDF- report.py")
    print("q. Quitter")

def main():
    terminal_output = ""
    output_file = "output/resultats.txt"
    hardware_results = {}

    while True:
        display_menu()
        choice = input("Entrez votre choix (1-5 ou q) : ")

        if choice == '1':
            print("\n--- Prise d'informations système ---")
            info.collect_info()
        
        elif choice == '2':
            print("\n--- Collecte des spécifications système ---")
            specs.export_system_specs()

        elif choice == '3':
            print("\n--- Consultation de l'état de la batterie ---")
            battery_test.check_battery_status(output_file)

        elif choice == '4':
            print("\n--- Tests des composants matériel ---")
            hardware_results = hardware_test.run_tests()  # Exécute les tests matériels et récupère les résultats

        elif choice == '5':
            print("\n--- Consulter ou rapporter d'autres pannes ---")
            # print("Vous pouvez maintenant quitter le programme avec 'CTR + c' et completer cette étape plus tard.")
            user_test.user_test()  # Appelle simplement la fonction


        elif choice == '6':
            print("\n--- Génération du rapport PDF ---")
            # Passer output_file, terminal_output, et hardware_results
            report.generate_pdf(output_file, terminal_output, hardware_results)

        elif choice == 'q':
            print("A la prochaine fois !")
            break

        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
