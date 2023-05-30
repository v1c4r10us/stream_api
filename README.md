```plaintext
 _____ _                               ___  ______ _____ 
/  ___| |                             / _ \ | ___ \_   _|
\ `--.| |_ _ __ ___  __ _ _ __ ___   / /_\ \| |_/ / | |  
 `--. \ __| '__/ _ \/ _` | '_ ` _ \  |  _  ||  __/  | |  
/\__/ / |_| | |  __/ (_| | | | | | | | | | || |    _| |_ 
\____/ \__|_|  \___|\__,_|_| |_| |_| \_| |_/\_|    \___/ 

[*] Starting deploy...
[*] Deploy ready!
```

Proyecto individual de **MLOps Engineer** con datos de plataformas **streaming** y **modelo de recomendación basado en ratings**.



---



## Intro



Disponemos de los datos de peliculas y series de las 04 principales plataformas de streaming: **Amazon Prime**, **Disney+**, **Hulu** y **Netflix**, así como los ratings de diferentes usuarios en diferentes años. La tarea consta de procesar la información todas las plataformas *(~ 22K de registros)*, así como los ratings *(~ 11M de registros)*.



## Arquitectura

Los datos de películas de las 04 plataformas se procesan directamente en el lado del servidor; sin embargo para el caso de los ficheros rating, que en total suman alrededor de 11M de registros, procesarlos en su totalidad en el lado del servidor demandaría consumo excesivo de **memoria ram** (más de lo que se proporciona de forma gratuita). Para solucionar este inconveniente y mediante el **EDA**, se sintetiza en 02 nuevos ficheros: *rating_global.csv* (para el request en GET_SCORE_COUNT) y *recsys.csv* (para el request en GET_RECOMMENDATION). El siguiente diagrama representa la arquitectura hasta su despliegue en <a href=https://railway.app/>Railway</a>:


<p align="center"><a href="https://lh3.googleusercontent.com/drive-viewer/AFGJ81r9AnNSb2JlrUtHTWfPREkNbWLScheX-iuHBNoK4ypYVQ_lm-JYNzMrj9KZo2xbeegd5auq3-g4QYy7n4e0Y-KmtquZ9A=s1600?source=screenshot.guru"> <img src="https://lh3.googleusercontent.com/drive-viewer/AFGJ81r9AnNSb2JlrUtHTWfPREkNbWLScheX-iuHBNoK4ypYVQ_lm-JYNzMrj9KZo2xbeegd5auq3-g4QYy7n4e0Y-KmtquZ9A=s1600" /></a></p>

## EDA (Exploratory Data Analysis)

+ En base al registro de **ratings** es posible realizar un análisis exploratorio por cada pelicula (global o por cada año), ambas formas fueron requeridas. El resultado se puede ver <a href=https://github.com/v1c4r10us/stream_api/blob/main/ratings/EDA.ipynb>Aquí</a>.

+ Para el caso del modelo de recomendación debido a los recursos de disposición libre de la plataforma de despliegue, se ha optado por generar un objeto serializable (.pkl) con la libreria **pickle** de python en donde se realiza el volcado de las recomendaciones para todos los títulos de películas generando alredor de 22K claves 'title', ello puede revisarse <a href=https://github.com/v1c4r10us/stream_api/blob/main/datasets/model.ipynb>Aquí</a>.

## Herramientas utilizadas



+ Python 3.8: Pandas, scikitLearn, pickle

+ <a href=https://fastapi.tiangolo.com/>FastAPI</a>

+ Conda

+ <a href=https://www.uvicorn.org/>Uvicorn</a>

+ Git



## Endpoints

**`Pelicula con mayor duracion`**
```bash
curl -X 'GET' \
  'https://streamapi-production.up.railway.app/get_max_duration/{year}/{platform}/{duration_type}' \
  -H 'accept: application/json'
```

**`Cantidad de películas por plataforma(con determinado 'score' y 'año')`**
```bash
curl -X 'GET' \
  'https://streamapi-production.up.railway.app/get_score_count/{platorm}/{scored}/{year}' \
  -H 'accept: application/json'
```

**`Cantidad de películas por plataforma`**
```bash
curl -X 'GET' \
  'https://streamapi-production.up.railway.app/get_count_platform/{platform}' \
  -H 'accept: application/json'
```

**`Actor con más apariciones(por plataforma y año)`**
```bash
curl -X 'GET' \
  'https://streamapi-production.up.railway.app/get_actor/{platform}/{year}' \
  -H 'accept: application/json'
```

**`Cantidad de contenidos(por pais y año)`**
```bash
curl -X 'GET' \
  'https://streamapi-production.up.railway.app/prod_per_country/{content_type}/{country}/{year}' \
  -H 'accept: application/json'
```

**`Cantidad de contenidos(por público clasificado)`**
```bash
curl -X 'GET' \
  'https://streamapi-production.up.railway.app/get_contents/{rating_class}' \
  -H 'accept: application/json'
```

**`Obtener recomendación en base a un título`**
```bash
curl -X 'GET' \
  'https://streamapi-production.up.railway.app/get_recommendations/{title}' \
  -H 'accept: application/json'
```
## Deployment

<a href=https://streamapi-production.up.railway.app/docs> AQUÍ</a> se visualiza el deployment de la API Rest.

## Video demo

Enlace a el video demostrativo <a href=https://youtu.be/LE3QT_eFeEM>AQUÍ</a>
