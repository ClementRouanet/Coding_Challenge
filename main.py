from app.processing import employees_details_toDF, get_departements_as_tree, save_into_csv, save_into_json


CSV_PATH = "data/employees.csv"
JSON_PATH = "data/departements.json"


if __name__ == "__main__":
    employees_df = employees_details_toDF()
    departements = get_departements_as_tree()

    save_into_csv(employees_df, CSV_PATH)
    save_into_json(departements, JSON_PATH)
