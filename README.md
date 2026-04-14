# Mini ETL con Pandas – Airbnb NYC

Proyecto sencillo de ETL orientado a practicar carga, exploración, limpieza básica y exportación de datos tabulares con **Pandas**.

## Objetivo

Construir un pipeline reproducible sobre un dataset de Airbnb NYC siguiendo el flujo:

**Extract → Transform → Load**

El proyecto sirve para practicar:

- Lectura de datos desde CSV
- Exploración inicial del dataset
- Tratamiento básico de valores ausentes
- Revisión semántica de variables problemáticas
- Conversión de tipos
- Exportación de datos limpios
- Organización mínima de un proyecto de datos en Python

## Estructura del proyecto

```text
mini-etl-airbnb/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── eda_airbnb.ipynb
└── src/
    └── etl_pipeline.py
```

## Dataset

- **Nombre**: Airbnb NYC 2019
- **Tipo**: dataset tabular de anuncios de Airbnb en Nueva York
- **Ubicación esperada**: `data/AB_NYC_2019.csv`

El dataset contiene información sobre precio, disponibilidad, número de reseñas, localización y otras variables relacionadas con los listings.

## Flujo del proyecto

### 1. Exploración inicial

En el notebook `notebooks/eda_airbnb.ipynb` se realiza una exploración básica del dataset para identificar:

- Dimensiones y tipos de variables
- Columnas con valores ausentes
- Posibles problemas de calidad
- Coherencia entre variables
- Correlaciones entre variables numéricas relevantes

### 2. Transformación

El script `src/etl_pipeline.py` aplica una versión reproducible de la limpieza planteada en el EDA.

Entre las operaciones incluidas o previstas se encuentran:

- eliminación de duplicados
- tratamiento de valores ausentes en variables textuales
- conversión de `last_review` a formato fecha
- revisión del tratamiento de `reviews_per_month`
- exportación del resultado limpio

### 3. Carga

La salida procesada se guarda en:

```text
data/processed/airbnb_nyc_clean.csv
```

En una versión posterior, este flujo puede ampliarse para cargar los datos en SQLite.

## Principales decisiones del EDA

Durante el análisis exploratorio se detectaron valores ausentes en las columnas:

- `last_review`
- `reviews_per_month`
- `host_name`
- `name`

### Decisiones iniciales

- `name` y `host_name` presentan un número muy reducido de valores ausentes, por lo que pueden imputarse con un valor como `"Unknown"` sin impacto relevante sobre el dataset.
- `last_review` se interpreta como una variable de fecha cuyo valor ausente puede reflejar ausencia de reseñas más que un error aleatorio de captura.
- `reviews_per_month` requiere una revisión más cuidadosa, ya que sus valores ausentes podrían estar relacionados con listings sin actividad de reseñas.
- `availability_365 = 0` no se trata automáticamente como error o missing value, ya que puede corresponder a situaciones reales del calendario del listing.

### Criterio seguido

En este proyecto no se busca aplicar una limpieza agresiva ni transformar variables sin contexto. La prioridad ha sido mantener un enfoque simple, reproducible y justificable, evitando decisiones arbitrarias sin conocer todavía el uso final del dataset.

## Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Ejecución

Desde la raíz del proyecto:

```bash
python src/etl_pipeline.py
```

## Dependencias

Ejemplo de contenido para `requirements.txt`:

```txt
pandas
matplotlib
seaborn
jupyter
```

## Posibles mejoras

- Añadir carga a SQLite
- Incorporar validaciones básicas antes de exportar
- Incluir pruebas simples sobre el pipeline
- Ampliar el análisis de coherencia entre variables

## Aprendizajes del proyecto

Este proyecto permite practicar un flujo básico de trabajo en datos:

1. Inspeccionar un dataset real
2. Identificar problemas de calidad
3. Justificar decisiones de limpieza
4. Trasladar esas decisiones a un script reproducible
5. Organizar el trabajo en una estructura mínima de proyecto
