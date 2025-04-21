-- Average price by neighborhood
WITH neighborhood_data AS (
    SELECT 
        SalePrice,
        YrSold,
        CASE 
            WHEN Neighborhood_Blmngtn = 1 THEN 'Blmngtn'
            WHEN Neighborhood_Blueste = 1 THEN 'Blueste'
            WHEN Neighborhood_BrDale = 1 THEN 'BrDale'
            WHEN Neighborhood_BrkSide = 1 THEN 'BrkSide'
            WHEN Neighborhood_ClearCr = 1 THEN 'ClearCr'
            WHEN Neighborhood_CollgCr = 1 THEN 'CollgCr'
            WHEN Neighborhood_Crawfor = 1 THEN 'Crawfor'
            WHEN Neighborhood_Edwards = 1 THEN 'Edwards'
            WHEN Neighborhood_Gilbert = 1 THEN 'Gilbert'
            WHEN Neighborhood_IDOTRR = 1 THEN 'IDOTRR'
            WHEN Neighborhood_MeadowV = 1 THEN 'MeadowV'
            WHEN Neighborhood_Mitchel = 1 THEN 'Mitchel'
            WHEN Neighborhood_NAmes = 1 THEN 'NAmes'
            WHEN Neighborhood_NPkVill = 1 THEN 'NPkVill'
            WHEN Neighborhood_NWAmes = 1 THEN 'NWAmes'
            WHEN Neighborhood_NoRidge = 1 THEN 'NoRidge'
            WHEN Neighborhood_NridgHt = 1 THEN 'NridgHt'
            WHEN Neighborhood_OldTown = 1 THEN 'OldTown'
            WHEN Neighborhood_SWISU = 1 THEN 'SWISU'
            WHEN Neighborhood_Sawyer = 1 THEN 'Sawyer'
            WHEN Neighborhood_SawyerW = 1 THEN 'SawyerW'
            WHEN Neighborhood_Somerst = 1 THEN 'Somerst'
            WHEN Neighborhood_StoneBr = 1 THEN 'StoneBr'
            WHEN Neighborhood_Timber = 1 THEN 'Timber'
            WHEN Neighborhood_Veenker = 1 THEN 'Veenker'
        END as neighborhood
    FROM listings
)
SELECT 
    neighborhood,
    ROUND(AVG(SalePrice), 2) as avg_price,
    COUNT(*) as number_of_listings
FROM neighborhood_data
GROUP BY neighborhood
ORDER BY avg_price DESC;

-- Top neighborhoods by price growth
WITH neighborhood_data AS (
    SELECT 
        SalePrice,
        YrSold,
        CASE 
            WHEN Neighborhood_Blmngtn = 1 THEN 'Blmngtn'
            WHEN Neighborhood_Blueste = 1 THEN 'Blueste'
            WHEN Neighborhood_BrDale = 1 THEN 'BrDale'
            WHEN Neighborhood_BrkSide = 1 THEN 'BrkSide'
            WHEN Neighborhood_ClearCr = 1 THEN 'ClearCr'
            WHEN Neighborhood_CollgCr = 1 THEN 'CollgCr'
            WHEN Neighborhood_Crawfor = 1 THEN 'Crawfor'
            WHEN Neighborhood_Edwards = 1 THEN 'Edwards'
            WHEN Neighborhood_Gilbert = 1 THEN 'Gilbert'
            WHEN Neighborhood_IDOTRR = 1 THEN 'IDOTRR'
            WHEN Neighborhood_MeadowV = 1 THEN 'MeadowV'
            WHEN Neighborhood_Mitchel = 1 THEN 'Mitchel'
            WHEN Neighborhood_NAmes = 1 THEN 'NAmes'
            WHEN Neighborhood_NPkVill = 1 THEN 'NPkVill'
            WHEN Neighborhood_NWAmes = 1 THEN 'NWAmes'
            WHEN Neighborhood_NoRidge = 1 THEN 'NoRidge'
            WHEN Neighborhood_NridgHt = 1 THEN 'NridgHt'
            WHEN Neighborhood_OldTown = 1 THEN 'OldTown'
            WHEN Neighborhood_SWISU = 1 THEN 'SWISU'
            WHEN Neighborhood_Sawyer = 1 THEN 'Sawyer'
            WHEN Neighborhood_SawyerW = 1 THEN 'SawyerW'
            WHEN Neighborhood_Somerst = 1 THEN 'Somerst'
            WHEN Neighborhood_StoneBr = 1 THEN 'StoneBr'
            WHEN Neighborhood_Timber = 1 THEN 'Timber'
            WHEN Neighborhood_Veenker = 1 THEN 'Veenker'
        END as neighborhood
    FROM listings
),
max_year AS (
    SELECT MAX(YrSold) as max_yr FROM neighborhood_data
),
price_by_year AS (
    SELECT 
        neighborhood,
        YrSold,
        AVG(SalePrice) as avg_price
    FROM neighborhood_data
    WHERE YrSold >= (SELECT max_yr - 1 FROM max_year)
    GROUP BY neighborhood, YrSold
)
SELECT 
    recent.neighborhood,
    ROUND(recent.avg_price, 2) as recent_avg_price,
    ROUND(old.avg_price, 2) as old_avg_price,
    ROUND(((recent.avg_price - old.avg_price) / old.avg_price * 100), 2) as price_growth_percentage
FROM price_by_year recent
JOIN price_by_year old ON recent.neighborhood = old.neighborhood
    AND recent.YrSold = (SELECT max_yr FROM max_year)
    AND old.YrSold = (SELECT max_yr - 1 FROM max_year)
WHERE old.avg_price > 0
ORDER BY price_growth_percentage DESC
LIMIT 10; 