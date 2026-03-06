# Tesis de Maestría: Bootstrap bayesiano aplicado a la elección gubernamental de Yucatán 2024

Este repositorio contiene los códigos, bases de datos y análisis desarrollados para la tesis de maestría, enfocada en la aplicación del bootstrap bayesiano (BB) en la elección gubernamental de Yucatán 2024, utilizando técnicas el BB para estimar varianzas e intervalos de confianza en los conteos de votos.

## Estructura del Repositorio

### Analisis ad hoc/
- Contiene archivos CSV con varianzas calculadas mediante bootstrapping para votos, utilizando el método 2, tanto estratificado como simulado.
  - `Var_bootstrap_votos_met_2_est.csv`: Varianzas bootstrap estratificado.
  - `Var_bootstrap_votos_met_2_sim.csv`: Varianzas bootstrap simulado.

### Bases/
- **Base elecciones analsis/**: Base de datos principal para el análisis de elecciones en Yucatán.
  - `base_elecciones_yuc_analsis.csv`: Archivo CSV con datos electorales procesados.
- **Bases antiguas/**: Versiones anteriores de las muestras de bootstrapping estratificado para votos.
  - Archivos numerados del 1 al 5 con distintas muestras y submuestras.
- **Bases_conteos_yucatan/**: Datos oficiales de conteos por casilla para la gubernatura de Yucatán.
  - `Casilla_por_casilla_gubernatura_280627_YUC.csv`: Datos detallados por casilla.
- **Boostrap por casillas/**: Muestras de bootstrapping realizadas por casillas.
  - Estratificado y sin estratificar.
- **Bootstrap votos/**: Bootstrapping aplicado a los votos, dividido en métodos:
  - **Directo/**: Método directo de bootstrapping.
  - **Metodo 1/**: Primer método alternativo.
  - **Metodo 2/**: Segundo método alternativo.
  - Cada carpeta contiene múltiples archivos CSV con distintas muestras y submuestras.

### Bases finales rep/
- Versiones finales y replicables de las bases de datos generadas.
- **Bootstrap por casillas/**: Archivos finales para bootstrapping por casillas.
- **Bootstrap votos/**: Archivos finales para bootstrapping de votos, organizados por método.

### Codigos/
- **Bootstrap_YUC_inicial.ipynb**: Notebook Jupyter inicial para el desarrollo del bootstrapping en Yucatán.
- **Archivos exportados/**: Versiones exportadas de los notebooks, como HTML.
- **Codigo_creacion_base_analisis/**: Código para crear la base de análisis a partir de los datos crudos.
- **Codigos_antiguos/**: Versiones anteriores de los códigos, incluyendo una versión incorrecta y una en Julia.
- **Codigos_bootstraps_finales/**: Códigos finales para el análisis.
  - **Analisis ad-hoc/**: Análisis específicos adicionales.
  - **Codigos_bootstraps_f/**: Códigos finales de bootstrapping.
  - **Comparaciones_analisis_f/**: Comparaciones entre diferentes bootstrap y análisis de los resultados.
- **Creacion_tablas_latex/**: Notebooks para generar tablas en LaTeX comparando métodos de bootstrapping (casillas vs votos, método 1 vs casillas, etc.).
- **Funciones_utiles/**: Módulo Python con funciones auxiliares para el bootstrapping.
- **Funciones_utiles_f/**: Versiones finales de las funciones auxiliares.

## Metodología
El proyecto compara diferentes enfoques de bootstrapping para el análisis de datos electorales:
- **Directo**: Aplicación directa del método bootstrap.
- **Método 1 y 2**: Variantes personalizadas para mejorar la estimación.
- Estratificado vs no estratificado: Considerando estratos en las casillas o votos.

Los análisis incluyen la creación de intervalos de confianza, varianzas y comparaciones entre métodos para validar la robustez de los resultados electorales.

## Requisitos
- **Python**: 3.8 o superior
- **Dependencias**: Se encuentran listadas en `requirements.txt`

### Instalación de Dependencias
Para instalar las dependencias necesarias, ejecute:

```bash
pip install -r requirements.txt
```

O, si utiliza Conda:

```bash
conda create --name bootstrap_env --file requirements.txt
conda activate bootstrap_env
```

### Paquetes requeridos
- **numpy**: Operaciones numéricas y cálculos estadísticos
- **pandas**: Manipulación y análisis de datos (DataFrames)
- **matplotlib**: Visualización de gráficos
- **seaborn**: Visualización estadística avanzada
- **scikit-learn**: Herramientas de aprendizaje automático (train/test split)
- **jupyter**: Ejecución de notebooks Jupyter interactivos
- **ipython**: Shell interactivo mejorado

### Datos requeridos
- Datos electorales de Yucatán (proporcionados en las carpetas Bases/)

## Uso
1. Ejecutar los notebooks en orden: desde la creación de la base hasta los análisis finales.
2. Utilizar las funciones auxiliares para replicar los bootstraps.
3. Generar tablas LaTeX para reportes académicos.

Este repositorio facilita la replicabilidad y verificación de los resultados de la tesis.

