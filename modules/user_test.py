# The GUIless Mac Tester   
## by Jules Ouanounou
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
        
    
    print("Tests utilisateurs terminés et enregistrés dans resultats.txt")
