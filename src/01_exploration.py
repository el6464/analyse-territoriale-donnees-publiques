import pandas as pd


def explorer_donnees(df):
    """
    Fonction d'exploration générale d'un jeu de données.
    """

    print("=" * 60)
    print("EXPLORATION DES DONNÉES")
    print("=" * 60)

    print("\nDimensions :")
    print(f"Nombre de lignes : {df.shape[0]}")
    print(f"Nombre de colonnes : {df.shape[1]}")

    print("\nTypes des variables :")
    print(df.dtypes)

    print("\nValeurs manquantes :")
    print(df.isnull().sum())

    print("\nDoublons :")
    print(df.duplicated().sum())

    print("\nStatistiques descriptives :")
    print(df.describe(include="all"))


if __name__ == "__main__":

    # Exemple d'utilisation :
    # df = pd.read_csv("chemin_vers_les_donnees.csv")
    # explorer_donnees(df)

    print("Script d'exploration prêt.")
    print("Les données professionnelles restent confidentielles.")
