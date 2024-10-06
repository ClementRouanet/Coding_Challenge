# Solutions Engineer - Coding Challenge

## Lancement de l'application

- Création de l'environnement virtuel : python3 -m venv env
- Lancement de l'environnement virtuel : .\env\Scripts\activate
- Installation des dépendances : pip3 install -r requirements.txt
- Lancement de l'application : python3 main.py

## Lancement quotidien du job :
    - Utilisation de cron
    - Commande Bash : crontab -e
    - Ajouter la ligne suivate au fichier : mm hh * * * python3 /path/to/main.py
