
import pandas as pd

# Los DataFrames son basicamente una lista de arrays columna
fruits = pd.DataFrame({
    'Apples'    : [34, 14],
    'Bananas'   : [58, 35]
}, index=['January', 'February'])
#print(fruits)

## CARGA DE DATOS CSV
                                # read_csv asume que existe cabecera
'''
raisin_data = pd.read_csv('datasets/raisin.csv', header=None)
X = raisin_data.iloc[:, :-1]    # Todas menos la última
y = raisin_data.iloc[:, -1]     # última columna

print("Shape total:", raisin_data.shape)
print("Shape X:", X.shape)
print("Shape y:", y.shape)
print("Número de clases:", y.nunique())
print(y.value_counts())         # Distribución de clases
'''

## INDEXADO: loc and iloc are row-first, column-second
'''
print(X.iloc[0])
print(X.iloc[:, 0])
print(X.iloc[:3, 0])            # Rango de valores
'''
'''
    df.iloc[0:1000] return 1000 entries, 0...999
    df.loc[0:1000] return 1001 entries,  0...1000
'''

## SELECCION CONDICIONAL
reviews = pd.read_csv('datasets/winemag-data_first150k.csv')

# Caso en el que no tienes etiquetas de fila
#   df.loc[ df[0] == 'Italy' ]
'''
reviews.loc[reviews.country == 'Italy']
reviews.loc[reviews.country.isin(['Italy', 'France'])]
reviews.loc[reviews.price.notnull()]
'''
## ASIGNACION DE DATOS
'''
reviews['critic'] = 'everyone'
reviews['index_backwards'] = range(len(reviews), 0, -1)
'''

## SUMMARY FUNCTIONS
#print(reviews.points.describe())
#print(reviews.province.value_counts())

# MAPS
'''
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

# Apply
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
    
star_ratings = reviews.apply(stars, axis='columns')

# Build-In mapping: Menos flexible pero más rápido para operaciones básicas
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean

## GROUPING
reviews.groupby('points').points.count()        # Igual que value_counts()
# Posibilidad de agrupar por varias columnas
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
# Otra forma de agrupar es con 'agg()' te permite ejecutar varias funciones en tu DF
reviews.groupby(['country']).price.agg([len, min, max])
'''
## MULTI-INDEXES
'''
    En muchas operaciones de groupby() acabamos con un multi-índice, lo más sencillo
    es volver a un índice regular después de aplicar groupby:  df.reset_index()
'''
'''
## SORTING
reviews.sort_values(by='len')
reviews.sort_values(by='len', ascending=False)
reviews.sort_index()
reviews.sort_values(by=['country', 'len'])
'''

'''
    EJERCICIO: What combination of countries and varieties are most common? 
    Create a Series whose index is a MultiIndexof {country, variety} pairs.
'''
#country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

## DATA TYPES AND MISSING VALUES
#reviews.dtypes
#reviews.price.dtype
#reviews.points.astype(str)         # Conversión de tipos
#print(reviews.country.isnull().sum())
#reviews.region_2.fillna("Unknown")  # Reemplazar valores nulos
# Reemplazar valores no nulos
#reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
'''
    EJERCICIO: What are the most common wine-producing regions? Create a Series counting the number 
    of times each value occurs in the region_1 field. 
    This field is often missing data, so replace missing values with Unknown. Sort in descending order.
'''
#reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
#reviews_per_region = reviews.region_1.fillna('Unknown').groupby('points').points.count().sort_values(..)

## CONCAT AND JOIN
# Si tienen índice común
#combined_products = pd.concat([gaming_products, movie_products])
# Sino lo mejor es establecer un índice común
#powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))