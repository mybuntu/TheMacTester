import os
import tkinter as tk
from tkinter import messagebox
from modules import info, specs, battery_test, hardware_test, user_test, report
from modules.user_test import user_test

# Configuration du répertoire de sortie
def set_output_directory():
    user_input = input("Merci d’entrer le nom du propriétaire de la machine ou de l’entreprise (ou « A Mettre en vente »): ")
    main_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'RESULTATS_TESTS')  # Dossier principal sur le bureau
    output_dir = os.path.join(main_dir, user_input)  # Sous-dossier pour cet utilisateur
    os.makedirs(output_dir, exist_ok=True)
    print(f"Dossier de sortie créé : {output_dir}")
    return output_dir

# Initialisation des variables de chemin de sortie
OUTPUT_DIR = set_output_directory()  # Le dossier utilisateur
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'resultats.txt')  # Chemin de resultats.txt

# Fonction pour exécuter chaque test avec les chemins mis à jour
def run_info_test():
    global serial_number  # Utilisez une variable globale pour stocker le numéro de série
    serial_number = info.collect_info(OUTPUT_FILE)
    messagebox.showinfo("Info", "Informations système collectées.")

def run_specs_test():
    specs.export_system_specs(OUTPUT_FILE)
    messagebox.showinfo("Specs", "Spécifications système collectées.")

def run_battery_test():
    battery_test.check_battery_status(OUTPUT_FILE)
    messagebox.showinfo("Batterie", "État de la batterie collecté.")

def run_hardware_test():
    results = hardware_test.run_tests(OUTPUT_FILE, OUTPUT_DIR)
    messagebox.showinfo("Tests matériels", f"Résultats matériels : {results}")

# def run_user_test():
#     user_test(OUTPUT_FILE)
#     messagebox.showinfo("Tests utilisateur", "Résultats des tests utilisateur enregistrés.")
def run_user_test():
    user_test(OUTPUT_FILE)
    messagebox.showinfo("Test utilisateur", "Tests utilisateur complétés.")

def generate_report(serial_number):
    # Vérifiez si un numéro de série est fourni
    if not serial_number:
        serial_number = "inconnu"
    pdf_filename = f"rapport_{serial_number}.pdf"
    report.generate_pdf(OUTPUT_FILE, os.path.join(OUTPUT_DIR, pdf_filename), {})
    messagebox.showinfo("Rapport", "Rapport PDF généré.")

# FONCTION QUITTER
def on_quit():
    print("Fermeture de l'application...")
    root.quit()

# Initialisation de l'interface graphique
root = tk.Tk()
root.title("TheMacTester")
root.geometry("400x400")

# CTA pour chaque test
tk.Button(root, text="Prendre les informations système", command=run_info_test).pack(pady=5)
tk.Button(root, text="Collecter les spécifications système", command=run_specs_test).pack(pady=5)
tk.Button(root, text="Consulter l'état de la batterie", command=run_battery_test).pack(pady=5)
# tk.Button(root, text="Tester les composants matériels", command=run_hardware_test).pack(pady=5)
tk.Button(root, text="Tester les composants matériels", command=lambda: run_hardware_test()).pack(pady=5)
tk.Button(root, text="Consulter ou rapporter d'autres pannes", command=run_user_test).pack(pady=5)
tk.Button(root, text="Générer le rapport PDF", command=lambda: generate_report(serial_number)).pack(pady=5)
tk.Button(root, text="Quitter", command=root.quit).pack(pady=5)

root.mainloop()
