# The GUIless Mac Tester   
## by Jules David
import tk
def user_test():
    issues_detected = {}

    questions = [
        "Connecteur de charge ?",
        "Ports (USB, Thunderbolt, SD-Card slot, HDMI port) ?",
        "Slot RAM ?",
        "Ventilateurs ?",
        "Wifi/Airport ?",
        "Bluetooth ?",
        "clavier ?",
        "Bouton Power ?",
        "Empreinte Touch ID ?",
        "Indicateur de charge ?",
        "Trackpad ?",
        "Charnière ?",
        "Témoin de mise en veille ?",
        "Touchbar ?",
        "Rétroéclairage Clavier ?",
        "Capteur de luminiosité ?"
    ]

    for question in questions:
        answer = input(f"{question} (o/N): (Enter => N)").strip().lower()
        if answer in ["n", "N", ""]:
            issues_detected[question] = "Fonctionnel"
        else:
            issues_detected[question] = "Défectueux"

    # Stocker les résultats dans resultats.txt
    with open("output/resultats.txt", "a") as file:
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

    etat_global = input("ÉTAT GLOBAL DE L'ORDINATEUR:\nA/ Neuf\nB/ Très bon état\nC/ Bon état\nD/ Correct\nE/ Usé\nSélectionnez une option (A(1), B(2), C(3), D(4), E(4): ").strip().lower()

    etat_result = etat_options.get(etat_global, "Non spécifié")

    # Ajouter l'état global à la fin du fichier resultats.txt
    with open("output/resultats.txt", "a") as file:
        file.write("=== ÉTAT GLOBAL DE L'ORDINATEUR ===\n")
        file.write(f"État: {etat_result}\n\n")

    print("État global de l'ordinateur ajouté dans resultats.txt")
