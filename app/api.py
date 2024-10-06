import os

import requests


API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


def request_api(endpoint, params=None):
    """
    Requête GET à l'endpoint de l'API spécifiée pour récupérer les données associées.

    Args :
        endpoint (string) : L'URL relative de l'endpoint à appeler sur l'API.
        params (dict, optional) : Un dictionnaire de paramètres de requête à envoyer avec la requête.
                                  Si aucun paramètre n'est fourni, la valeur par défaut est None.

    Returns :
        json : Les données récupérées au format JSON si la requête est réussie, sinon renvoie le code de l'erreur.
    """

    headers = {
        "Authorization": f"lucca application={API_KEY}",
        "Content-Type": "application/json"
    }
    
    url = f"{BASE_URL}{endpoint}"

    try :
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json(), response.status_code
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        return None, response.status_code
    
    except requests.exceptions.JSONDecodeError as err :
        print(f"Json Error : {err}")
        return None, response.status_code
    
    except requests.exceptions.Timeout as err :
        print(f"TimeOut Error : {err}")
        return None, response.status_code
