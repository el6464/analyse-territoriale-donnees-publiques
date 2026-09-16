import pandas as pd


def nettoyer_donnees(df):
    """
    Préparation générique des données territoriales.
    """

    df = df.copy()

    # Suppression des doublons
    df = df.drop_duplicates()

    # Suppression des espaces inutiles dans les noms de colonnes
    df.columns = df.columns.str.strip()

    # Suppression des lignes entièrement vides
    df = df.dropna(how="all")

    return df


def creer_indicateur_evolution(
    df,
    valeur_initiale,
    valeur_finale
):
    """
    Calcule une évolution en pourcentage.
    """

    df = df.copy()

    df["evolution_pct"] = (
        (df[valeur_finale] - df[valeur_initiale])
        / df[valeur_initiale]
    ) * 100

    return df
