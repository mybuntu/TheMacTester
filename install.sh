# Run si t'as la flemme mais ces commandes marchent mieux executées une par une. 
#!/bin/bash
python3 -m venv venv

pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "Install terminée. \ 
Maintenant veuillez copier coller la commande suivante : \
                                    source venv/bin/activate"
