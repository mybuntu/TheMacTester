import subprocess
import re
import os

def load_model_years(file_path):
    # Charge la correspondance entre les identifiants de modèle et les années.
    model_year_map = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Utiliser ";" comme séparateur
                model_id, year, model_market_name = line.strip().split(';')
                model_year_map[model_id] = (year, model_market_name)
    except FileNotFoundError:
        print(f"Erreur : le fichier {file_path} est introuvable.")
    except ValueError:
        print(f"Erreur de format dans le fichier {file_path}. Chaque ligne doit contenir trois colonnes séparées par ';'.")
    return model_year_map

def collect_info(output_file):
    # Récupère les informations système et les écrit dans un fichier texte.
    try:
        # Obtenir les informations système avec system_profiler
        system_info = subprocess.check_output("system_profiler SPHardwareDataType", shell=True).decode('utf-8')

        # Récupérer l'identifiant du modèle et le numéro de série
        model_identifier = re.search(r"Model Identifier:\s*(.+)", system_info)
        serial_number = re.search(r"Serial Number \(system\):\s*(.+)", system_info)

        if model_identifier and serial_number:
            model_id = model_identifier.group(1).strip()
            serial_number_value = serial_number.group(1).strip()

            # Charger la correspondance modèle <-> année
            file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'model_years.txt')
            model_year_map = load_model_years(file_path)

            year, model_market_name = model_year_map.get(model_id, (".................", "................."))

            # Préparer les informations à écrire dans le fichier texte
            result_text = (
                f"===Modèle: {model_market_name}===\n"
                f"Identifiant du modèle: {model_id}\n"
                f"Année: {year}\n"
                f"Numéro de série: {serial_number_value}\n"
            )

            # Écriture dans le fichier texte
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write("=== INFO SYSTÈME ===\n")
                file.write(result_text)
                file.write("\n")

            print(f"Les informations de la machine ont été exportées dans {output_file} avec succès.")
            return serial_number_value  # Retourne le numéro de série
        else:
            print("Identifiant du modèle ou numéro de série non trouvé.")
            return None  # Retourne None si non trouvé

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande system_profiler : {e}")
        return None  # Retourne None en cas d'erreur
