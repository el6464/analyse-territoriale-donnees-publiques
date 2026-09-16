-- =========================================================
-- Analyse territoriale
-- =========================================================


-- 1. Vérification du nombre d'observations

SELECT COUNT(*) AS nombre_observations
FROM donnees_territoriales;


-- 2. Nombre d'observations par territoire

SELECT
    territoire,
    COUNT(*) AS nombre_observations
FROM donnees_territoriales
GROUP BY territoire
ORDER BY nombre_observations DESC;


-- 3. Agrégation d'un indicateur par territoire

SELECT
    territoire,
    SUM(indicateur) AS total_indicateur,
    AVG(indicateur) AS moyenne_indicateur
FROM donnees_territoriales
GROUP BY territoire
ORDER BY total_indicateur DESC;


-- 4. Evolution d'un indicateur dans le temps

SELECT
    periode,
    SUM(indicateur) AS total_indicateur
FROM donnees_territoriales
GROUP BY periode
ORDER BY periode;


-- 5. Comparaison entre périodes

SELECT
    territoire,
    periode,
    SUM(indicateur) AS total_indicateur
FROM donnees_territoriales
GROUP BY territoire, periode
ORDER BY territoire, periode;
