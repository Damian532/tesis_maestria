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

## Flujo de Ejecución

El proyecto debe ejecutarse en el siguiente orden:

### 1. Crear la Base de Análisis
Ejecutar primero:
```
Codigos/Codigo_creacion_base_analisis/Creacion_base_analsis.ipynb
```
**Objetivo**: Procesar datos crudos y generar la base limpia y lista para análisis.

**Salida**:
- `Bases/Base elecciones analsis/base_elecciones_yuc_analsis.csv`

### 2. Ejecutar Análisis de Bootstrap
Una vez generada la base de análisis, ejecutar todos los notebooks que comienzan con `Bootstrap` en la carpeta:
```
Codigos/Codigos_bootstraps_finales/Codigos_bootstraps_f/
```
Se incluyen:
- `Bootstrap_directo_votos.ipynb`
- `Bootstrap_submuestra_votos_metodo_1.ipynb`
- `Bootstrap_submuestra_votos_metodo_2.ipynb`
- `Bootstrap_por_casillas.ipynb` (y variantes)

**Objetivo**: Aplicar diferentes métodos de bootstrapping a los datos electorales y generar métricas estadísticas.

**Salida**:
- Resultados guardados en `Bases finales rep/Bootstrap votos/` (subdivididos por método)
- Resultados guardados en `Bases finales rep/Bootstrap por casillas/`

### 3. Comparar Resultados
Una vez completados todos los bootstraps, ejecutar los análisis de comparación:
```
Codigos/Codigos_bootstraps_finales/Comparaciones_analisis_f/
```

**Objetivo**: Comparar resultados entre diferentes métodos de bootstrapping y generar tablas para reportes.

### Archivos Adicionales
- **Creacion_tablas_latex/**: Notebooks para generar tablas en LaTeX con los resultados finales.
- **Codigos_antiguos/**: Versiones previas y código descontinuado (no ejecutar para análisis final).
- **Analisis ad-hoc/**: Análisis específicos y exploratorios (opcional, depende de necesidades).

## Uso
1. Instalar dependencias: `pip install -r requirements.txt`
2. Ejecutar notebooks siguiendo el flujo indicado arriba.
3. Utilizar las funciones auxiliares de `Funciones_utiles_f/` para replicar bootstraps personalizados.
4. Generar tablas LaTeX desde `Creacion_tablas_latex/` para reportes académicos.

Este repositorio facilita la replicabilidad y verificación de los resultados de la tesis.

