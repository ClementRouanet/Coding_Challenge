import pandas as pd
import json
from time import sleep

from .endpoints import get_employees, get_former_employees, get_employee_details, get_departements


def employees_toDF() :
    """
    Transforme les JSON de tous les employés (futurs, présents et anciens) en DataFrame.

    Returns : 
        dataframe : Le DataFrame des employés.
    """

    # récupère les données des employés de l'entreprise
    employees = get_employees()
    former_employees = get_former_employees()

    # Conservation uniquements des données pertinente des JSON
    employees = employees["data"]["items"]
    former_employees = former_employees["data"]["items"]

    # Champs du futur DataFrame
    columns = ['id', 'name', 'employed']

    # Conversion des JSON en DataFrame Pandas
    employees_df = pd.DataFrame(employees, columns=columns)
    former_employees_df = pd.DataFrame(former_employees, columns=columns)

    # Champ permettant de savoir si un employé estctuellement dans l'entreprise ou non
    employees_df['employed'] = True
    former_employees_df['employed'] = False

    # Assemblage des deux dataFrames (anciens et présents employés) en un seul
    all_employees_df = pd.concat([employees_df, former_employees_df])
    all_employees_df = all_employees_df.sort_values(by='id')
    all_employees_df.reset_index(drop=True, inplace=True)

    return all_employees_df



def employees_details_toDF() :
    """
    Récupère les informations détaillées pour chaque employé.

    Returns :
        dataframe : Le DataFrame avec les infos détaillées de chaque employé.
    """

    # Récupération des employés et de leurs ids en liste
    employees_df = employees_toDF()
    employee_ids = list(employees_df['id'])

    # Champs du futur DataFrame
    columns = ['Id', "Last Name", "First Name", "Gender", "Mail", "Address", "Birth Date", "Nationality", 
               "Contract Start Date", "Contract End Date", "Employee Number", "Job Title", "CSP Id", "Department Id", "Manager Id", "Legal Entity Id"]
    
    # Création du DataFrame vide mais avec les bons champs
    df = pd.DataFrame(columns=columns)

    # récupération des indos de chaque employés pour les mettre dans le DataFrame
    i = 0
    while i < len(employee_ids):
        json, status_code = get_employee_details(employee_ids[i])

        # Si la limite de reqûetes par secondes a été atteinte, on attend
        if status_code == 429 :
            print("Rate limit exceeded. Waiting before retrying...\n")
            sleep(5)

        # Si la limite de reqûetes par secondes n'a pas été atteinte, on récupère les données
        else :
            print(f"Get data for employee {employee_ids[i]}")

            row = [[
                employee_ids[i], 
                json['data'].get('lastName'),
                json['data'].get('firstName'),
                json['data'].get('gender'),
                json['data'].get('mail'),
                json['data'].get('address'),
                json['data'].get('birthDate'),
                json['data'].get('nationality')['name'] if json['data'].get('nationality') else "",
                json['data'].get('dtContractStart'),
                json['data'].get('dtContractEnd'),
                json['data'].get('employeeNumber'),
                json['data'].get('jobTitle'),
                json['data'].get('csp')['name'] if json['data'].get('csp') else "",
                json['data'].get('departmentID'),
                json['data'].get('managerID'),
                json['data'].get('legalEntityID')
            ]]
            
            # Ajout des infos de l'employé au DataFrame
            row_df = pd.DataFrame(row, columns=columns)
            df = pd.concat([df, row_df])

            i += 1

    return df



def get_departements_as_tree() :
    """
    Renvoie le JSON avec la hiérarchie des départements sous forme d'arbre.

    Returns :
        json : Le JSON final
    """

    departements = get_departements()
    departements = departements["data"]

    return departements



def save_into_csv(df, file_path) :
    """
    Enregistre un DataFrame Pandas au format CSV.

    Args:
        df (pd.DataFrame): Le DataFrame à enregistrer.
        file_path (str): Le chemin du fichier où le CSV sera enregistré.
    """

    df.to_csv(file_path, index=False)

    print(f"DataFrame saved into a CSV : {file_path}")



def save_into_json(data, file_path):
    """
    Enregistre un objet JSON dans un fichier.

    Args:
        data (dict): L'objet JSON à enregistrer.
        file_path (str): Le chemin du fichier où le JSON sera enregistré.
    """

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved into a JSON : {file_path}")
