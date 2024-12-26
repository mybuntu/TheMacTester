import os
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
import cv2
from modules import info, other_tests, specs, battery_test, hardware_test, report, notes_supp
#################################################################################################
print(f"Répertoire actuel : {os.getcwd()}")
# Définir le répertoire de travail
if getattr(sys, 'frozen', False):  # Détecter si l'application est empaquetée
    base_path = sys._MEIPASS
else:  # Sinon, en mode développement
    base_path = os.path.abspath(os.path.dirname(__file__))
    print(f"Chemin de base : {base_path}")


os.chdir(base_path)


cap = cv2.VideoCapture(0)  # On tente d'ouvrir la caméra
if cap.isOpened():
    print("Caméra correctement détectée.")
    cap.release()
else:
    print("Erreur : Impossible d'ouvrir la caméra.")

# Définir resource_path pour PyInstaller
def resource_path(relative_path):
    """Obtenir le chemin d'une ressource, compatible avec PyInstaller."""
    try:
        # PyInstaller stocke les ressources dans un répertoire temporaire _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # En mode développement, on utilise le chemin normal
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
#################################################################################################
# Configuration du répertoire de sortie
def set_output_directory():
    user_input = simpledialog.askstring(
        "Nom du propriétaire",
        "Merci d’entrer le nom du propriétaire de la machine ou de l’entreprise.\nPOUR UN RECONDITIONNEMENT\nVeuillez taper 'Recond':"
    )
    if not user_input:
        messagebox.showwarning("Erreur", "Vous devez entrer un nom !")
        return set_output_directory()
    
    main_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'RESULTATS_TESTS')
    output_dir = os.path.join(main_dir, user_input)
    os.makedirs(output_dir, exist_ok=True)
    messagebox.showinfo("Succès", f"Dossier de sortie créé : {output_dir}")
    return output_dir

# Initialisation des variables globales
OUTPUT_DIR = set_output_directory()
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'resultats.txt')

# Fonction pour exécuter chaque test avec les chemins mis à jour
def run_info_test():
    global serial_number
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

def run_user_test():
    other_tests.user_test(OUTPUT_FILE)
    messagebox.showinfo("Test utilisateur", "Tests utilisateur complétés.")

def run_notes_supp():
    notes_supp.add_notes(OUTPUT_FILE)
    messagebox.showinfo("Notes", "Notes supplémentaires enregistrées.")

def generate_report(serial_number):
    # Vérifiez si un numéro de série est fourni
    if not serial_number:
        serial_number = "inconnu"
    pdf_filename = f"rapport_{serial_number}.pdf"
    report.generate_pdf(OUTPUT_FILE, os.path.join(OUTPUT_DIR, pdf_filename), {})
    messagebox.showinfo("Rapport", "Rapport PDF généré.")

# Fonction pour quitter proprement
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
tk.Button(root, text="Tester les composants matériels", command=lambda: run_hardware_test()).pack(pady=5)
tk.Button(root, text="Consulter ou rapporter d'autres pannes", command=run_user_test).pack(pady=5)
tk.Button(root, text="Ajouter des notes supplémentaires", command=run_notes_supp).pack(pady=5)
tk.Button(root, text="Générer le rapport PDF", command=lambda: generate_report(serial_number)).pack(pady=5)
tk.Button(root, text="Quitter", command=root.quit).pack(pady=5)

root.mainloop()
