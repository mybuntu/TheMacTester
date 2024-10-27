# The Mac Tester (using Tk gui) 
## by Jules Ouanounou
import tkinter as tk
from tkinter import messagebox
from modules import info, specs, battery_test, hardware_test, user_test, report

def run_info_test():
    info.collect_info()
    messagebox.showinfo("Info", "Informations système collectées.")

def run_specs_test():
    specs.export_system_specs()
    messagebox.showinfo("Specs", "Spécifications système collectées.")

def run_battery_test():
    battery_test.check_battery_status("output/resultats.txt")
    messagebox.showinfo("Batterie", "État de la batterie collecté.")

def run_hardware_test():
    results = hardware_test.run_tests()
    messagebox.showinfo("Tests matériels", f"Résultats matériels : {results}")

def run_user_test():
    results = user_test.user_test()
    messagebox.showinfo("Tests utilisateur", f"Résultats des tests utilisateur : {results}")

def generate_report():
    report.generate_pdf("output/resultats.txt", "", {})
    messagebox.showinfo("Rapport", "Rapport PDF généré.")

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Test des Mac")
root.geometry("400x400")

# Boutons pour chaque test
tk.Button(root, text="Prendre les informations système", command=run_info_test).pack(pady=5)
tk.Button(root, text="Collecter les spécifications système", command=run_specs_test).pack(pady=5)
tk.Button(root, text="Consulter l'état de la batterie", command=run_battery_test).pack(pady=5)
tk.Button(root, text="Tester les composants matériels", command=run_hardware_test).pack(pady=5)
tk.Button(root, text="Consulter ou rapporter d'autres pannes", command=run_user_test).pack(pady=5)
tk.Button(root, text="Générer le rapport PDF", command=generate_report).pack(pady=5)
tk.Button(root, text="Quitter", command=root.quit).pack(pady=5)

root.mainloop()
