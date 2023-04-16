```plaintext

____________                                    _______________________

__  ___/_  /__________________ _______ ___      ___    |__  __ \___  _/

_____ \_  __/_  ___/  _ \  __ `/_  __ `__ \     __  /| |_  /_/ /__  /  

____/ // /_ _  /   /  __/ /_/ /_  / / / / /     _  ___ |  ____/__/ /   

/____/ \__/ /_/    \___/\__,_/ /_/ /_/ /_/      /_/  |_/_/     /___/   

                                                                       

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



**`Pelicula con mayor duracion`**:

```curl

HTTP GET: /get_max_duration/{anio}/{plataforma}/{dtype}

```

**`Cantidad de películas`**:

```curl

/get_score_count/{plataforma}/{scored}/{anio}

```

**`Cantidad de películas`**:

```curl

/get_count_platform/{plataforma}/{scored}/{anio}

```


