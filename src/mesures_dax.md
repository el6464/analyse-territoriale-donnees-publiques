Population totale =
SUM(Donnees[Population])
Nombre de ménages =
SUM(Donnees[Menages])
Population précédente =
CALCULATE(
    [Population totale],
    DATEADD(
        Calendrier[Date],
        -1,
        YEAR
    )
)
Evolution population (%) =
DIVIDE(
    [Population totale] - [Population précédente],
    [Population précédente]
)
