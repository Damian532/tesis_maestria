import numpy as np
import pandas as pd

def inter_prob_l(arr):
    return np.quantile(arr, 0.025)

def inter_prob_u(arr):
    return np.quantile(arr, 0.975)

# Función para crear vectores Dirichlet
def f(x,y, semilla):

    # Semilla para las muestras de la Dirichlet
    rng = np.random.default_rng(semilla)
    return rng.dirichlet(np.ones(x), y)

# Función para crear vectores Dirichlet con distintos valores (no solo unos)
def f_a(x,y, semilla):
    
    # Semilla para las muestras de la Dirichlet
    rng = np.random.default_rng(semilla)

    # Vemos si tiene valores con cero
    if np.where(x==0)[0].size==0:
        z_c=rng.dirichlet(x, y)
    else:
        x_sc=np.delete(x,np.where(x==0)[0])
        # El vector Dirichlet con los valores que no son cero
        z=rng.dirichlet(x_sc, y)
        # Insertar los valores ceros al vector
        indices=np.where(x==0)[0]
        i = indices - np.arange(len(indices))
        z_c=np.insert(arr=z, obj=i, values=0, axis=1)
    return z_c

def dirichlet_sample(alphas, semilla):
    """
    Genera una muestra aleatoria Dirichlet de variables aleatorias Gamma
    """
    # Semilla para las muestras gamma
    rng = np.random.default_rng(semilla)
    
    # Obtenemos las muestras gamma
    r = rng.standard_gamma(alphas)
    return r / r.sum(-1, keepdims=True)

# Funciones para agregar unos
def aggregar_unos(array_ceros, indices):

    # Hacemos el conteo de los índices
    unique, counts = np.unique(indices, return_counts=True)
    
    #array_ceros[indices]=1
    array_ceros[unique]=counts

    return array_ceros

# Función para hacer el conteo del array
def bincount(a):
    y = np.bincount(a)
    ii = np.nonzero(y)[0]
    return np.vstack((ii, y[ii])).T

# Función para obtener totales que sumen un número dado dado las proporciones y el número dado
def obtener_totales(array_proporciones, numero_dado):

    '''
    array_proporciones: Las proporciones por cada estrato (es un np array)
    numero_dado: Número dado que es el tamaño de la muestra
    '''

    # Creamos un vector para los totales
    totales_ti=np.zeros((array_proporciones.shape[0],5))

    # Guardamos el índice de las casillas
    totales_ti[:,0]=np.arange(totales_ti.shape[0])+1

    # Guardamos las proporciones
    totales_ti[:,1]=array_proporciones

    # Guardamos el redondeo hacia abajo
    totales_ti[:,2]=np.floor(totales_ti[:,1]*numero_dado)

    # Guardamos la proporción sin redondear
    totales_ti[:,3]=totales_ti[:,1]*numero_dado
    
    # El residuo por cada estrato
    totales_ti[:,4]=totales_ti[:,3]-totales_ti[:,2]

    # Vemos cuantos falta de la muestra total
    falt_muestra=int(numero_dado-totales_ti[:,2].sum())

    # Ordenamos con respecto al residuo faltante (de menor a mayor)
    totales_ti_ord=totales_ti[totales_ti[:,4].argsort()[::-1]]

    # Agregamos los casos faltantes
    for i in range(falt_muestra):
        totales_ti_ord[i,2]=totales_ti_ord[i,2]+1


    # Ordenamos el array por el número de distrito
    totales_ti_ord=totales_ti_ord[totales_ti_ord[:,0].argsort()]

    # Regresa los totales de las proporciones 
    return totales_ti_ord[:,2]

# Calcular las métricas del bootstrap
def metricas_bootstrap(prop_reales, inter_prob, est_punt, porcenta_tama):
    '''
    prop_reales: Los datos reales de la elección.
    inter_prob: Los intervalos calculados por el bootstrap (bayesiano).
    est_punt: Las estimaciones puntuales del bootstrap (bayesiano).

    Regresa:

    df_metr_boot: Base con todas las métricas del bootstrap (bayesiano).
    df_error_max: Base con los errores máximos
    df_can_cob: El porcentaje de cobertura de cada candidato
    
    '''
    # Guardamos los resultados reales en un data frame
    resultados_reales=prop_reales.reset_index()
    resultados_reales=resultados_reales.rename(columns={'index':'Candidato', 0:'Porcentaje_real'})

    # Lista auxiliar
    df_lista_esta=[]
    for i in range(int(inter_prob.shape[1]/2)):
        df_lista_inter=pd.DataFrame(inter_prob[:,[i,i+5]], columns=["cuantil_025", "cuantil_975"])
        if i + 5 < inter_prob.shape[1]:
            df_lista_inter=pd.DataFrame(inter_prob[:,[i,i+5]], columns=["cuantil_025", "cuantil_975"])
        else:
            continue
        df_lista_inter["Longitud_intervalo"]=df_lista_inter["cuantil_975"]-df_lista_inter["cuantil_025"]
        df_lista_inter["Estamacion_puntual"]=est_punt[:,i]
        df_lista_inter["Porcentaje_real"]=resultados_reales.loc[i,"Porcentaje_real"]
        df_lista_inter["Candidato"]=resultados_reales.loc[i,"Candidato"]
        df_lista_inter=df_lista_inter.reset_index().rename(columns={'index':'Num_bootstrap'})
        df_lista_inter["Num_bootstrap"]=df_lista_inter["Num_bootstrap"]+1
        df_lista_inter["Error"]=abs(df_lista_inter["Estamacion_puntual"]-df_lista_inter["Porcentaje_real"])
        df_lista_inter["Cobertura"]=np.where(np.logical_and(df_lista_inter["Porcentaje_real"]>=df_lista_inter["cuantil_025"],df_lista_inter["Porcentaje_real"]<=df_lista_inter["cuantil_975"]),1,0)
        df_lista_inter["Porcenta_tama"]=porcenta_tama
        df_lista_esta.append(df_lista_inter)

    # Base con todos los datos
    df_metr_boot=pd.concat(df_lista_esta).reset_index(drop=True)

    # Calulo de error máximo por bootstrap
    df_error_max=df_metr_boot.groupby(["Num_bootstrap"]).agg({'Error':'max'}).reset_index().rename(columns={'Error':'Error_max'})
    df_error_max["Porcenta_tama"]=porcenta_tama
    # Calculamos la cobertura por candidato
    df_can_cob=df_metr_boot.groupby(["Candidato"]).agg({'Cobertura':'sum'}).reset_index().rename(columns={'Cobertura':'Numero_total_cob'})
    df_can_cob["Cobertura"]=df_can_cob["Numero_total_cob"]/df_error_max["Num_bootstrap"].max()
    df_can_cob["Porcenta_tama"]=porcenta_tama
    df_can_cob

    return df_metr_boot, df_error_max, df_can_cob

# Hacer el muestreo estratificado
def muestreo_estratificado_mej(df, strata, sample_size=250, semilla=1):

    # df=df_act_yuc_i.copy()
    population = len(df)

    # Estrato
    strata=["DISTRITO"]

    # Tamaño de la muestra
    # Los estratos como numpy array
    tmp = df[strata]

    # Hacemos los conteos de los estratos
    unique, counts = np.unique(np.array(tmp), return_counts=True)
    # Creamos el vector para guardar las proporciones
    tmp_grpd=np.zeros((unique.shape[0], 6))
    tmp_grpd[:,[0,1]]=np.asarray((unique, counts)).T

    # Los índices de cada estrato en array
    array_index_estrato=np.array(tmp.reset_index()[['index']+ strata])

    # Los pasamos a la lista
    indices_dist=[array_index_estrato[array_index_estrato[:,1]==i][:,0] for i in range(1,unique.shape[0]+1)]

    # Proporciones de los estratos
    tmp_grpd[:,2] = tmp_grpd[:,1]/tmp_grpd[:,1].sum()
    # Obtenemos los valores de las muestras por cada estrato
    tmp_grpd[:,3] = np.floor((sample_size/population)*tmp_grpd[:,1])

    # Las muestras proporcionales (sin redondear)
    tmp_grpd[:,4] = (sample_size/population)*tmp_grpd[:,1]

    # Calculamos el residuo faltante por casilla
    tmp_grpd[:,5]=tmp_grpd[:,4]-tmp_grpd[:,3]

    # Número de casillas faltantes
    cas_falt=int(sample_size-tmp_grpd[:,3].sum())

    # Ordenamos con respecto al residuo faltante (de menor a mayor)
    tmp_grpd_ord=tmp_grpd[tmp_grpd[:,5].argsort()[::-1]]
    
    # Agregamos los casos faltantes
    for i in range(cas_falt):
        tmp_grpd_ord[i,3]=tmp_grpd_ord[i,3]+1

    # Ordenamos el array por el número de distrito
    tmp_grpd_ord=tmp_grpd_ord[tmp_grpd_ord[:,0].argsort()]

    # Lista auxiliar
    lista_aux=[None] * tmp_grpd_ord.shape[0]
    for i in range(tmp_grpd_ord.shape[0]):
        # Semilla para las muestras de la Dirichlet
        rng = np.random.default_rng(semilla+i)
        tmp_df = rng.choice(indices_dist[i],int(tmp_grpd_ord[i,3]),replace=False)
        lista_aux[i] = tmp_df

    # Indices de la muestra
    indices_muestra = np.concatenate(lista_aux)
    # Seleccionamos todos los indices
    df_mue_est_j=df.loc[indices_muestra]

    return df_mue_est_j