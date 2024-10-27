# The GUI Mac Tester   
## by Jules Ouanounou

# Pour un environnement virtuel
cd ~/TheMacTester/ \
python3 -m venv venv \
source venv/bin/activate \
pip3 install -r requirements.txt \
python3 main.py 


# Dans un env de test
cd ~/TheMacTester/ \
pip3 install -r requirements.txt \
python3 main.py

Structure:
---------
```plaintext
test_mac/
├── main.py                 # Script principal
├── modules/                # Dossier pour les modules
│   ├── info.py             # Module pour la prise d'informations système
│   ├── specs.py            # Module pour les tests matériels
│   ├── battery_test.py     # Module pour les tests concernant la batterie
│   └── hardware_test.py    # Module pour les tests matériels
│   └── user_test.py        # Module pour générer les tests utilisateurs
│   └── report.py           # Module pour générer le rapport PDF
├── resources/              # Dossier pour les fichiers de ressources (si besoin)
│   └── model_years.txt     # Fichier contenant les modèles et les années
└── output/                 # Dossier pour les fichiers de sortie
    └── resultats.txt       # Fichier texte des résultats, se créer après exécution


Explication : 
main propose un range de choix de tests qui sont des scripts (modules) qui sont rangé dans le dossier (vous le voyez venir ?) modules/ 
Chaque scripts est une fonction mais le but est de rendre le programme de base plus modulable. 
Dans le dossier resoures, vous trouverez un repertoire des mac par modèles et années (incomplète pour l'instant). 
Chaque modules renvoie un resultat dans le fichier output/resultats.txt. 
Le module report.py permet de generer un pdf qui se basera sur le fichier resultats.txt pour rendre un fichier pdf plus lisible. 
Ignorer les modules "impression" & "upload" qui pour l'instant n'ont pas été testé.


