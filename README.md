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



 <p align=center><img src=https://lh3.googleusercontent.com/drive-viewer/AAOQEOSoO4yhBDiT6_7J33K-aMExYdvDinKR7ZYnO5R_RaCkbcFI-GVcZebbEiImS3bvDhcJob1krNHTbT1Wj4FQ3foJAMotAw=s2560><p>



Esta arquitectura describe el proceso realizado para el tratamiento de los datos así como el despliegue en <a href=https://railway.app/>Railway</a>



## Herramientas utilizadas



+ Python 3.8: Pandas, scikitLearn

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

## Deployment

Si desea visualizar el despliegue en producción pulsar <a href=https://streamapi-production.up.railway.app/> AQUÍ</a>