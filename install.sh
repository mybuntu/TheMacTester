# Run si t'as la flemme mais ces commandes marchent mieux executées une par une. 
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
source venv/bin/activate
