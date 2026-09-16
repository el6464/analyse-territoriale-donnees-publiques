import pandas as pd


def calculer_statistiques(df, colonne):
    """
    Calcule quelques statistiques descriptives.
    """

    statistiques = {
        "moyenne": df[colonne].mean(),
        "mediane": df[colonne].median(),
        "minimum": df[colonne].min(),
        "maximum": df[colonne].max(),
        "ecart_type": df[colonne].std()
    }

    return pd.Series(statistiques)


def evolution_indicateur(df, colonne, periode):
    """
    Agrège un indicateur par période.
    """

    return (
        df.groupby(periode)[colonne]
        .sum()
        .reset_index()
    )


def comparaison_territoires(
    df,
    territoire,
    indicateur
):
    """
    Compare un indicateur entre territoires.
    """

    return (
        df.groupby(territoire)[indicateur]
        .agg(
            ["count", "mean", "min", "max"]
        )
        .reset_index()
    )
