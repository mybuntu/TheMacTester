#!/bin/bash

# Vérifier si Python 3 est installé
if ! command -v python3 &>/dev/null; then
    echo "Python 3 n'est pas installé. Installez-le avant de lancer ce script."
    exit 1
fi

# Créer l'environnement virtuel
echo "Création de l'environnement virtuel..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Échec de la création de l'environnement virtuel."
    exit 1
fi

# Activer l'environnement virtuel
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Échec de l'activation de l'environnement virtuel."
    exit 1
fi

# Mettre à jour pip
echo "Mise à jour de pip..."
pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo "Échec de la mise à jour de pip."
    deactivate
    exit 1
fi

# Installer les dépendances
echo "Installation des dépendances..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Échec de l'installation des dépendances."
    deactivate
    exit 1
fi

echo "Installation terminée avec succès. L'environnement virtuel est activé."
echo "Pour réactiver l'environnement, exécutez : source venv/bin/activate"
