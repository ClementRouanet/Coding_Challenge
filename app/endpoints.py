from .api import request_api


def get_employees() :
    """
    Récupère la liste des employés de l'entreprise.

    Returns :
        json : Les données récupérées au format JSON si la requête est réussie, sinon None.
    """

    endpoint = "api/v3/users"
    json, status_code = request_api(endpoint)

    if status_code != 200 :
        print("Error in the get_employees function")
    
    return json



def get_former_employees() :
    """
    Récupère la liste des anciens employés de l'entreprise.

    Returns :
        json : Les données récupérées au format JSON si la requête est réussie, sinon None.
    """

    endpoint = "api/v3/users"
    params = {"dtContractEnd": "notequal,null"}
    json, status_code = request_api(endpoint, params)

    if status_code != 200 :
        print("Error in the get_former_employees function")
    
    return json



def get_employee_details(employee_id) :
    """
    Récupère les détails de l'employé "employee_id" de l'entreprise.

    Args :
        employee_id (int) : index de l'employé auquel on récupère les infos détaillées.

    Returns :
        json : Les données récupérées au format JSON si la requête est réussie, sinon None.
    """

    endpoint = f"api/v3/users/{employee_id}"
    json, status_code = request_api(endpoint)

    if status_code != 200 :
        print("Error in the get_employee_details function")
    
    return json, status_code



def get_departements() :
    """
    Récupère la liste des départements de l'entreprise sous une forme d'arbre.

    Returns :
        json : Les données récupérées au format JSON si la requête est réussie, sinon None.
    """

    endpoint = "api/v3/departments/tree"
    json, status_code = request_api(endpoint)

    if status_code != 200 :
        print("Error in the get_departements function")
    
    return json